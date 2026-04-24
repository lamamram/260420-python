# %% ---------------- code impératif avec sqlite3 -------------
"""
SQLITE3: BDD relationnelle avec un dialecte SQL simple
BDD en un seul fichier ou chargé en RAM
pas de host / port / user / password / droits
le module sqlite3 python est dans la lib standard

sqlite3 utilise la DbAPI python pour tous les clients de BDD en python
- méthode connect() => connexion (création ou connexion sur la bdd)
- méthode cursor()  => prompt sur la connexion
- méthode execute() => exécuter une requête SQL sur le cursor
- méthode fetch()   => faire sortir les enregistrements attendus
- méthode close()   => fermer la cnx
---------------- gérer les transactions -----------------
- méthode begin()   => commence une transaction
- methode commit()  => confitmer une tr
- méthode rollback()=> annuler une tr
"""

import sqlite3

conn = sqlite3.connect("dns.db")
cur  = conn.cursor()
req = "SELECT SQLITE_VERSION()"
cur.execute(req)
row  = cur.fetchone()
print(row)
conn.close()

# %% ----------------- une connexion s'ouvre et se ferme ------------------
import sqlite3

with open("domain_names_sqlite3.sql", "r", encoding="utf-8") as f:
  sql_content = f.read()

with sqlite3.connect("dns.db") as conn:
  # je veux les donées de sortie sous la forme de dicts
  conn.row_factory = sqlite3.Row
  cur  = conn.cursor()
  # exécute le script mais ne retourne pas d'informations
  cur.executescript(sql_content)
  # test
  cur.execute("SELECT * FROM pays")
  rows = cur.fetchall()
  for row in rows:
    print(dict(row))


# %% ----------------------- insérer 100k lignes à partir d'un csv -----------------

import sqlite3
import csv

with open("dns_100k.csv", mode="r", encoding="utf-8") as f:
  with sqlite3.connect("dns.db") as conn:
    reader = csv.reader(f, delimiter=";")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    req = "INSERT INTO domain_name ('name', 'iso2') VALUES (?, ?)"
    next(reader)
    cur.executemany(req, reader)
    print(cur.rowcount)


# %% ----------------- client sqlite3 en poo et gestionnaire de contexte

import sqlite3
import csv
from pathlib import Path
from typing import List, Any
class SqliteClient:
  def __init__(self, db_path: str | Path, factory: Any=sqlite3.Row):
    self.db_path = db_path
    self.factory = factory
  
  def __enter__(self):
    # autocommit=False => c'est à nous de gérer les transanctions, dans l'__exit__
    self.conn = sqlite3.connect(self.db_path, autocommit=False)
    self.conn.row_factory = self.factory
    return self
  
  def __exit__(self, x_typ, x_msg, x_tb):
    if x_typ:
      print(x_msg)
      self.conn.rollback()
    else:
      self.conn.commit()
    self.conn.close()
  
  def init_db(self, script_path: str | Path, encoding="utf-8"):
    with open(script_path, "r", encoding=encoding) as f:
      sql_content = f.read()
    cur = self.conn.cursor()
    cur.executescript(sql_content)
  
  def select(self, table: str):
    cur = self.conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    return list(map(dict, cur.fetchall()))
  
  #  '   truc','bidule','machin        '
  def insert(self, table: str, fields: list, values: List[Any]):
    req = f"INSERT INTO {table} ('{"','".join(fields)}') VALUES (?{(len(fields) - 1) * ",?"})"
    cur = self.conn.cursor()
    cur.executemany(req, values)





if __name__ == "__main__":
  with open("dns_100k.csv", mode="r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)
    reader = list(reader)[:5]
  with SqliteClient("dns.db") as sql:
    sql.init_db("domain_names_sqlite3.sql")
    sql.insert("domain_name", fields=("name", "iso2"), values=reader)
    print(sql.select("domain_name"))
    

# sql.conn.cursor()

# %% -------------------- initiation à sqlAlchemy (véritable ORM) ---------------

# pip install SQLAlchemy

# connexion et session pour pooling
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# définition des modèles
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# champs SQL
from sqlalchemy import String, Enum, Integer, Float, DateTime, Text, ForeignKey, func

from pathlib import Path

# -------------------------------- GLOBALS ------------------------------------

DB_PATH = Path(__file__).parent / "dns.db"
# chaîne de cnx :URI
DB_URI = f"sqlite:///{DB_PATH}"


engine = create_engine(
  DB_URI,
  # par défaut: on peut réutiliser le même thread pour une nouvelle cnx => pooling possible
  connect_args={"check_same_thread": False},
  # voir les requêtes SQL pour debug
  echo=True
)

# factory de sessions
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# --------------------------- MODELES --------------------------------------------

class Base(DeclarativeBase):
  """classe de base pour tous les modèles (tables)"""
  pass

class DomainName(Base):
  __tablename__ = "domain_name"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  iso2: Mapped[str] = mapped_column(String(2), nullable=False)
  name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)

class Pays(Base):
  __tablename__ = "pays"
  iso2: Mapped[str] = mapped_column(String(2), primary_key=True)
  name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

# ------------------------------- init_db --------------------------------------------------


def init_db():
  import re
  import csv

  Base.metadata.create_all(bind=engine)

  with SessionLocal() as session:
    # Import pays depuis le script SQL
    sql_path = Path(__file__).parent / "domain_names_sqlite3.sql"
    with open(sql_path, "r", encoding="utf-8") as f:
      sql_content = f.read()

    match = re.search(r"INSERT INTO `pays` VALUES (.+);", sql_content)
    if match:
      pays_values = re.findall(r"\('([^']+)','([^']+)'\)", match.group(1))
      for iso2, name in pays_values:
        # Pays(iso2=iso2, name=name)  => objet enregistrement de table
        # cet objet a une réalité en python et aussi dans la base
        # il faut synchroniser régulièrement les objet py et sql flush() commit()
        session.merge(Pays(iso2=iso2, name=name))

    # Import domain_name depuis dns_10.csv
    csv_path = Path(__file__).parent / "dns_10.csv"
    with open(csv_path, mode="r", encoding="utf-8") as f:
      reader = csv.DictReader(f, delimiter=";")
      for row in reader:
        session.add(DomainName(name=row["Nom de domaine"], iso2=row["Pays BE"]))

    session.commit()

init_db()
# %% ------------------------- usage ----------------------------------------
from sqlalchemy import select, func

with SessionLocal() as session:
  # SELECT * FROM domain_name
  dns_count = session.execute(select(func.count()).select_from(DomainName)).scalar()
  print(f"Nombre de domaines: {dns_count}")

# %%
