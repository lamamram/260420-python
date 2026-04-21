# %% ------------------- créer un dictionnaire: dict ----------------------

#       {         paire      , paire    }
#       { clé       : valeur , clé  : valeur}
user =  {"firstname": "roger", "age": 56}

## REM: les clés sont uniques et peuvent être n'importe quel type immutable
# créer un dict ayant 
# des clés de type tuple à 2 éléments qui représentent la latitude et la longitude
# et des valeurs qui sont les noms des villes liés à ces coordonnées 
points = {(48.8566, 2.3522): "Paris", (40.7128, -74.0060): "New York", (35.6895, 139.6917): "Tokyo"}

# %% -------------- accéder à la valeur d'une clé -------------
user =  {"firstname": "roger", "age": 56}

# afficher la valeur liée à la clé 'firstname'
print(user["firstname"], points[(48.8566, 2.3522)])
# afficher le nom d'une ville liée à un point


# %% --------- remplacer une valeur, créer une clé, ... --------
user =  {"firstname": "roger", "age": 56}
# remplacer le prénom

user["firstname"] = "jean"
# ajouter un email

user['email'] = "me@example.com"

# supprimer age du dict
del user["age"]

# afficher la taille de user si la clé existe dans user 
# ou afficher une valeur par défaut N/A

taille = user['taille'] if 'taille' in user else "N/A" # l'opérateur in fonctionne avec les clés avec les dicos
taille = user.get('taille', "N/A") # la méthode get permet de faire la même chose que l'opérateur in mais de manière plus concise


# %% ---------------- itérer sur un dictionnaire -----------------
user = {"firstname": "roger", "age": 56}

# tester si un dictionnaire est un itérable
for k in user:
    print(k)

# afficher la conversion d'un dictionnaire en liste
print(list(user))

print("-"*10 + "avec les valeurs" + "-"*10)

# afficher la liste des valeurs d'un dictionnaire
# itérer sur les valeurs d'un dictionnaire
for v in user.values(): print(v)
print(list(user.values())) # liste des valeurs


print("-"*10 + "avec les items: clés & valeurs" + "-"*10)

# afficher la conversion d'un dictionnaire en une liste de tuples à 2 éléments
# itérer sur les clés & les valeurs d'un dictionnaire
for k, v in user.items(): print(f"{k} : {v}")
print(list(user.items())) # liste de tuples (clé, valeur)

# %% -- recréer un dict à partir d'une liste de clés et une liste de valeurs --
user = {"firstname": "roger", "age": 56}


# créer la liste des clés
keys = list(user.keys())
# créer la liste des valeurs
values = list(user.values())
# zipper les 2 listes
z = zip(keys, values)
# convertir cet "objet" en liste
# print(list(z))
# convertir cet "objet" en dict
# warning: zip est un itérateur, une fois converti en liste, il ne peut plus être itéré
print(dict(z))
 

# %% -------------- gestion des sets -----------------

fruits = {"pomme", "poire", "banane"}

# fruits[0] # les sets ne sont pas indexables

print("pomme" in fruits) # tester si un élément est dans un set
fruits.add("orange") # ajouter un élément à un set
fruits.remove("poire") # supprimer un élément d'un set + exception si l'élément n'existe pas
fruits.discard("poire") # supprimer un élément d'un set + ne fait rien

for f in fruits: print(f) # itérer sur un set

doublons  = list(fruits) + ["pomme", "banane"]
print(set(doublons)) # supprimer les doublons d'une liste en la convertissant en set
# %%
