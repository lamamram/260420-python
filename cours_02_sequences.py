#################### séquence: str, list, tuple ############################
# %% ---------- chaines de caractères: str: concaténation ---------------

prenom = "john"
nom = "doe"

# afficher nom complet: john doe

print(prenom + " " + nom) # surcharge de l'opérateur + : concaténation de str
print(prenom + str(2) + nom) # pas de conversion implicite en python
# %% ---------- fonctions internes d'une variable selon son type : ici str ----

######### <variable>.<fonction>()

prenom = "john"
nom = "doe"

# afficher le nom complet : John DOE
print(prenom.capitalize() + " " + nom.upper()) # capitalize : 1ère lettre en majuscule, upper : tout en majuscules

# %% ------------ indéxer une séquence ------------------------------------
nom_complet = "Joe DOE"

# prendre la longueur d'une str
print(len(nom_complet))

######## <variable>[n]: caractère de la variable à la position n 

# afficher le 1er caractère de la str, le 1er car. du 2ème mot, le dernier car.
print(nom_complet[0], nom_complet[4], nom_complet[len(nom_complet) -1], nom_complet[-1])


# %% ------------- SLICING d'une séquence ----------------------------------- 

civilite_nom_complet = "Mr. Joe DOE"

######## slicing : <variable>[<index de début compris>:<index de fin non compris>]
######## slicing avec pas: <var>[deb:fin:pas]

# afficher la civilité, le prénom, le nom à partir de civilite_nom_complet

# slicing: indice de début compris: indice de fin non compris, début == 0 ou rien, fin => rien si dernier
print(civilite_nom_complet[:3], civilite_nom_complet[4:7], civilite_nom_complet[8:])
# afficher une chaine contenant chaque 1er car. de chaque mot //
print(civilite_nom_complet[::4])
# retourner civilite_nom_complet
print(civilite_nom_complet[::-1])


# %% -------------- retourner l'indice d'une str ---------------------------

civilite_nom_complet = "Mr. Joe DOE"

# afficher la civilité, le prénom, le nom à partir des indices de J et D
premier_espace = civilite_nom_complet.index(" ")
deuxieme_espace = civilite_nom_complet.index(" ", premier_espace + 1)
print(civilite_nom_complet[:premier_espace], civilite_nom_complet[premier_espace +1: deuxieme_espace], civilite_nom_complet[deuxieme_espace + 1:])

# même chose mais en remettant les valeurs slicées en minuscules
print(civilite_nom_complet[:premier_espace].lower(), civilite_nom_complet[premier_espace +1: deuxieme_espace].lower(), civilite_nom_complet[deuxieme_espace + 1:].lower())

# %% -------------- list: indexation, concaténation, slicing -------------

mots = ["appeler", "un", "chat"]

# afficher chat à partir de mots

mots[2]

# modifier mots en concaténant ["il", "faut"] , mots et ["un", "chat"]

mots = ["il", "faut"] + mots + ["un", "chat"]

# remettre mots dans sa valeur initiale à partir de sa valeur courante

mots = mots[2:5]
print(mots)

# %% -------------- transformation de liste <=> chaîne de caractères ----------

civilite_nom_complet = "Mr. Joe DOE"

# créer la liste mots, des mots de civilite_nom_complet => split

mots = civilite_nom_complet.split(" ")

# recréer civilite_nom_complet à partir de mots
# en soudant les élements de mots avec un " " => join

civilite_nom_complet = " ".join(mots)

# %% ---------------- fonctions internes exclusives aux listes -----------------
mots = ["appeler", "un"]

# ajouter "chat" à droite avec [] ou autrement
# mots[2] = "chat" # [] : IndexError

mots.append("chat") # append : ajoute un élément à la fin de la liste

# ajouter ["chat", "un", "chat", "gris"] à droite
mots.extend(["chat", "un", "chat", "gris"]) # extend : ajoute les éléments d'une liste à la fin de la liste courante

# ajouter "il" à gauche
mots.insert(0, "il") # insert : ajoute un élément à une position donnée dans la liste, 0 : début de la liste

# ajouter "faut" à gauche d'"appeler"

mots.insert(1, "faut")

# supprimer le dernier élement de mots et retourne sa valeur

mots.pop() # pop : supprime et retourne le dernier élément de la liste

# supprimer le premier élément //

mots

# supprimer la 1ère occurence de chat 

mots

# %% --------------- listes et tuples / str : mutabilité et immutabilité ------------
mots = ["nommer", "un", "chien"]

# remplacer "chien" en "chat" dans mots avec []
mots[2] = "chat"


mots = tuple(mots)

# remplacer "nommer" en "appeler" dans mots
# mots[0] = "appeler" # TypeError : 'tuple' object does not support item assignment

# transformer mots en une str phrase et mettre le 1er car. en majuscule
mots = " ".join(mots)

# mots[0] = mots[0].upper() # str immuable
mots = mots.capitalize() # façon immuable de changer une variable


# %% --------------- opérateur in : test d'appartenance -----------------------

phrase = "appeler un chat"

# savoir si "chat" est dans phrase

"chat" in phrase

# savoir si "chien" n'est pas dans phrase

"chien" not in phrase

# idem en transformant phrase en mots

mots = phrase.split(" ")
print("chat" in mots)