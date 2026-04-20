# %% ---------- définition et appel d'une fonction -----------------------
### une fonction est un objet créé/définie avec: 
### le mot clé def suivi de <nom_de_la_fonction>(): 
###     et après un bloc d'instructions  

# définition d'une fonction ma_fonction() qui contient l'affichage de "coucou"


### pour exécuter le bloc de la définition, on doit appeler la fonction 
### <nom_de_la_fonction>()
### (): opérateur d'appel
### une fonction est un type de donnée dite "callable"

# afficher l'appel de la fonction ma_fonction

# %% ----------- retour d'une fonction ------------------------------

# même définition mais en remplaçant le print("coucou") par le mot clé return et 'coucou'


# afficher l'appel de la fonction

# alternativement, on peut affecter l'appel de la fonction dans une variable

# %% -- définition d'une fonction avec des paramètres et appel des paramètres ---

# définir une fonction qui ajoute 2 entiers en paramètres et qui retourne la somme 


# %% ------------ annotations, documentation et contrôle -------------------


# créer une fonction division de 2 floats qui retourne un float
# 1. en notifiant les types d'entrée et de sortie de la fonction
# 2. documenter la fonction en ajoutant une """doctstring""" au début du bloc
# 3. faire un contrôle sur le dénominateur



# %% --------------- types de paramètres ----------------------------------

# créer une fonction calcul_tva qui prend 2 paramètres le prix ht et le taux
# et retourne la valeur de tva sur ce prix et ce taux
# 1. annotations et documentation
# 2. le prix est arbitraire => paramètre positionnel / obligatoire
# MAIS on considère que la valeur par défaut du taux est 20 => paramètre nommé / optionnel


# appeler la fonction sans paramètres

print(f"""appel positionnel: 199 -> prix_ht, 5.5 -> taux 
       => { "???"}""")
print(f"""appel avec un paramètre optionnel: 199 -> prix ht et rien -> taux
       => { "???" }""")
print(f"""appel nommé: les valeurs sont fléchées vers les paramètres 
       => pas besoin d'ordre => { "???" }""")

# %% ---------------- paramètres "variadiques" *args ---------------------
## *args: permet de définir un nombre variable de paramètres positionnels
## le bloc peut alors utiliser un tuple args

# exemple: print
# on veut afficher tous les mots soudés par "-" à partir de 2 prints
# et les 2 paramètres nommées "sep" et "end"

print("bonjour", "tout", "le", "monde")
print("comment", "allez", "vous")


# créer une fonction addition qui peut ajouter un nombre quelconque de params

# %% paramètres "variadiques" **kwargs
## **kwargs: permet de définir un nombre variable de paramètres nommés
## le bloc peut alors utiliser un dict kwargs

# créer une fonction create_user avec 
# 1. le prénom et le nom obligatoires
# 2. et un nombre quelconque de paramètres nommés/optionnels
# 3. pour créer et retourner un dictionnaire user 
#    avec les paramètres obligatoires et les autres s'ils existent (age, taille...)




