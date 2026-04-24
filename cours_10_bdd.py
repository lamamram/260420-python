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
    self.conn = sqlite3.connect(self.db_path)
    self.conn.row_factory = self.factory
    return self
  
  def __exit__(self, exc_type, exc, tb):
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