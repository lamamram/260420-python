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
req  = cur.execute("SELECT SQLITE_VERSION()")
row  = cur.fetchone()
print(row)
conn.close()

# %% ----------------- une connexion s'ouvre et se ferme ------------------

with sqlite3.connect("dns.db") as conn:
  conn = sqlite3.connect("dns.db")
  cur  = conn.cursor()
  req  = cur.execute("SELECT SQLITE_VERSION()")
  row  = cur.fetchone()
  print(row)













# %% ----------------- client sqlite3 en poo et gestionnaire de contexte














# %% -------------------- initiation à sqlAlchemy (véritable ORM) ---------------