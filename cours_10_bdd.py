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














# %% ----------------- client sqlite3 en poo et gestionnaire de contexte














# %% -------------------- initiation à sqlAlchemy (véritable ORM) ---------------