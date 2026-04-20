#################### séquence: str, list, tuple ############################
# %% ---------- chaines de caractères: str: concaténation ---------------

prenom = "john"
nom = "doe"

# afficher nom complet: john doe


# %% ---------- fonctions internes d'une variable selon son type : ici str ----

######### <variable>.<fonction>()

prenom = "john"
nom = "doe"

# afficher le nom complet : John DOE

# %% ------------ indéxer une séquence ------------------------------------
nom_complet = "Joe DOE"

# prendre la longueur d'une str


######## <variable>[n]: caractère de la variable à la position n 

# afficher le 1er caractère de la str, le 1er car. du 2ème mot, le dernier car.



# %% ------------- SLICING d'une séquence ----------------------------------- 

civilite_nom_complet = "Mr. Joe DOE"

######## slicing : <variable>[<index de début compris>:<index de fin non compris>]
######## slicing avec pas: <var>[deb:fin:pas]

# afficher la civilité, le prénom, le nom à partir de civilite_nom_complet
# afficher une chaine contenant chaque 1er car. de chaque mot //
# retourner civilite_nom_complet


# %% -------------- retourner l'indice d'une str ---------------------------

civilite_nom_complet = "Mr. Joe DOE"

# afficher la civilité, le prénom, le nom à partir des indices de J et D


# même chose mais en remettant les valeurs slicées en minuscules


# %% -------------- list: indexation, concaténation, slicing -------------

mots = ["appeler", "un", "chat"]

# afficher chat à partir de mots

# modifier mots en concaténant ["il", "faut"] , mots et ["un", "chat"]

# remettre mots dans sa valeur initiale à partir de sa valeur courante

# %% -------------- transformation de liste <=> chaîne de caractères ----------

civilite_nom_complet = "Mr. Joe DOE"

# créer la liste mots, des mots de civilite_nom_complet => split

# recréer civilite_nom_complet à partir de mots
# en soudant les élements de mots avec un " " => join


# %% ---------------- fonctions internes exclusives aux listes -----------------
mots = ["appeler", "un"]

# ajouter "chat" à droite avec [] ou autrement

# ajouter ["chat", "un", "chat", "gris"] à droite

# ajouter "il" à gauche

# ajouter "faut" à gauche d'"appeler"

# supprimer le dernier élement de mots et retourne sa valeur

# supprimer le premier élément //

# supprimer la 1ère occurence de chat 

# %% --------------- listes et tuples / str : mutabilité et immutabilité ------------
mots = ["nommer", "un", "chien"]

# remplacer "chien" en "chat" dans mots avec [] et une fonction interne

mots = tuple(mots)

# remplacer "nommer" en "appeler" dans mots


# transformer mots en une str phrase et mettre le 1er car. en majuscule


# %% --------------- opérateur in : test d'appartenance -----------------------

phrase = "appeler un chat"

# savoir si "chat" est dans phrase

# savoir si "chien" n'est pas dans phrase

# idem en transformant phrase en mots