# %% --------------------- créer un fichier ------------------------

# ".": dossier courant
# "..": dossier parent
# "~" : dossier utilisateur
# mode "w" : création si le fichier existe ET écrasement du contenu s'il existe
# attention souvent sous windows/Excell on peut avoir des fichiers encodés en iso-8859-1

# creér (ouvrir en mode création) le fichier "mon_fichier.txt" en encodage utf-8

f = open("./mon_fic.txt", "w", encoding="utf-8")


# écriture de deux lignes avec les sauts de lignes
f.write("1ère ligne\n")
f.write("2ème ligne\n")


# important! il faut fermer ce qu'on a ouvert
f.close()

# %% ----------------- lire le contenu d'un fichier ---------------------

# ouvrir le fichier en lecture et même encodage
f = open("./mon_fic.txt", "r", encoding="utf-8")

# lire une ligne (avec \n)
# print rajoute un 2ème  \n
print(f.read(11))

# lire tout
print(f.read())

## REM. notion de curseur: la deuxième lecture reprend 
## depuis la fin de la première ligne
f.close()

# %% ------------- écriture à la fin du fichier (append) -------------------
f = open("./mon_fic.txt", "a", encoding="utf-8")
# écrire une 3ème ligne dans le fichier 
f.write("3ème ligne\n")


# vérifier que le contenu existant n'a pas été supprimé
f.close()

# %% --------------------- readlines / writlelines --------------
f = open("./mon_fic.txt", "r", encoding="utf-8")
print(f.readlines(11))
f.close()

f = open("./mon_fic.txt", "a", encoding="utf-8")
f.writelines(["4ème ligne\n", "5ème ligne\n"])
f.close()

# %% ------------------- modes avancés ------------------------------
# remplacer la ligne n
f = open("./mon_fic.txt", "r+", encoding="utf-8")
# r+: on a un curseur au début en lecture
#   : on a également un curseur à la fin en écriture (a priori)
#   : on peut replacer le curseur d'écriture

n = 3

# la lecture après sera en erreur car le curseur est positionné sur la moitué d'un caractère
# f.seek(2) # UnicideDecodeError

# je lis 1 ligne du fichier pour positionner le curseur de lecture
for _ in range(n- 1):
  f.readline()

## rem f.tell() : position du curseur d'écriture/lecture
# la 1ère ligne est composé de 11 caractère
# tell() retourne est nb d'octet lié à l'encodage => 13
# utf-8 : 1 octer pour les caractère ASCII et 2 octets avec les autres (è, \n)

pos = f.tell()
## f.seek(pos) : positionne les curseurs d'écriture/lecture à la position pos
f.seek(pos)
f.write("bonjour\n")
## attention : read et write utilise des caractère 
##           : alors que tell et seek utilise des octets !!!

# positionner tous les curseurs sur la position du curseur de lecture

# écrire un nouveau contenu + \n

# supprimer le reste du fichier après le curseur
f.truncate()
# je me repositionne au début du fichier pour lire le contenu
f.close()

# %% -- faciliter les ouvertures/fermetures: gestionnaires de contexte: with --

## with <ouverture>() as <var>:
  # fichier ouvert
  # ....

with open("./mon_fic.txt", "r", encoding="utf-8") as f:
  print(f.read())


# ici fichier fermé


# %% ----------- un fichier est un itérable de lignes ----------------------

with open("./mon_fic.txt", mode="r", encoding="utf-8") as f:
  for line in f:
    print(line)

# %% --------- suppression de la ligne n avec for ----------

n = 2

l = []
# lire toutes les lignes du fichier dans une liste sauf la ligne à supprimer
with open("./mon_fic.txt", mode="r", encoding="utf-8") as f:
  for i, line in enumerate(f, start=1):
    if i != n:
      l.append(line)

with open("./mon_fic.txt", mode="w", encoding="utf-8") as f:
  f.write("".join(l))
# écraser le fichier avec les lignes de liste

# %% -----------------  création d'un csv -----------------------------


# importer le module standard csv de la bibliothèque standard
import csv

users = [
  {"firstname":"Joe", "lastname": "Doe", "age": 22, "height": 1.75, "comment": "blablab ... ; blabliblo"},
  {"firstname": "Jane", "lastname": "Austen", "age": 34, "height": 1.79, "comment": "blabla"},
]

# ouvrir le fichier users.csv en création en utf-8
with open("./users.csv", "w", encoding="utf-8") as f:
  writer = csv.writer(f, delimiter=";")
  writer.writerow(users[0].keys())
  for d in users:
    writer.writerow(d.values())
# créer un writer issu du module csv, utilisant le fichier
# utiliser le writer pour écrire le header du csv à partir des clés des dict
# //                             les données du csv //         valeurs du dict

# %% ------------------- idem mais avec le bon outil -------------------------
import csv

users = [
  {"firstname":"Joe", "lastname": "Doe", "age": 22, "height": 1.75, "comment": "blablab ... ; blabliblo"},
  {"firstname": "Jane", "lastname": "Austen", "age": 34, "height": 1.79, "comment": "blabla"},
]

with open("./users.csv", "w", encoding="utf-8") as f:
  d_writer = csv.DictWriter(
    f, fieldnames=users[0].keys(),
    delimiter=";",
    lineterminator="\n"
  )
  d_writer.writeheader()
  d_writer.writerows(users)


# %% --------------- lire les lignes de csv ---------------

import csv

users = []

with open("./users.csv", mode="r", encoding="utf-8") as f:
  reader = csv.reader(f, delimiter=";")
  header = next(reader)
  for row in reader:
    users.append(dict(zip(header, row)))

print(users)
# idem mais en lecture
# protéger l'ouverture du fichier s'il le fichier existe
# tip: on peut itérer de façon manuelle un itérable avec la fonction next()
#    : pour récolter le header en première ligne


# %% ----------------------- écriture en JSON ----------------------

import json

# idem avec json 
# sachant que les objets et les dictionnaires python sont très proches
# méthodes pour écrire: json.dump et json.dumps
# écrire le json de façon comprimée ou dépliée (sep, indent)

users = [
  {"firstname":"Joe", "lastname": "Doe", "age": 22, "height": 1.75, "comment": "blablab ... ; blabliblo"},
  {"firstname": "Jane", "lastname": "Austen", "age": 34, "height": 1.79, "comment": "blabla"},
]

with open("users.json", mode="w", encoding="utf-8") as f:
  json.dump(users, f)

# %% --------------- lire un json ---------------------------

# idem en lecture avec json.load ou json.loads
try:
  with open("users.json", mode="r", encoding="utf-8") as f:
    users = json.load(f)
except FileNotFoundError as e:
  print(e)
else:
  print(users)




# %%
