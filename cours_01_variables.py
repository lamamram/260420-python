# %% ----------- affectation --------------------------
# "x <- 10 : on met 10 dans x")
# "1. on créé la variable x")
# "2. on place la valeur litérale 10 de type entier")
# "3. dans x")
## REM: = opérateur d'affection



## REM en python on ne DECLARE par le type de la variable
## donc on peut changer la valeur de x avec une valeur d'un autre type de donées



# %% --------------- types built-in et politique de nommage -----------

# entier              (type int)
# nombre flottant     (type float)
# chaine de caractère (type str)
# snake_case
# convention => CONSTANTE
# liste               (type list): ensemble d'éléments ordonnables de types quelconque
# tuple               (type tuple): // non modifiables 
# dictionnaire        (type dict): ensemble de paires clé: valeur
# booléen             (type bool)
# rien                (type NoneType)

# %% --------------- manipulation des variables ------------------------------

x = 10

print("incrémenter x: ajouter 1 à x et réaffecter x avec cet ajout")

print("créer y avec 5 et z avec la soustraction de x entre y")


# %% ------------- fonctions globales entrée / sortie ----------------------
## input(): saisir un âge et un prénom à partir du clavier 
##        : et RETOURNER la valeur saisie


print("type(): voir le type de l'âge")


print("int(): conversion en entier")
## REM: il y a une fonction de conversion pour chaque type de donnée 

print("créer une varible user qui contient à la fois le prénom et l'âge")


## print(): nombre de paramètres quelconque


# %% ---------- valeurs litérales, variables, expressions ---------------

## prendre un entier au clavier et afficher la valeur x + 2

# %% ---------- MINI-EXO: opérateurs arithmétiques -------------------------
# 1. saisir un entier au clavier => compris entre 0 et 86400 (nb de secondes dans une journée)
# 2. convertir la sortie précédente en entier
# 3. décomposer ce nombre en nb en heure, minutes, secondes
# 4. affichier le résulat <nb_hour>h <nb_min>m <nb_sec>


# %% ------------------- même affichage mas en formatant mieux ---------------

## version 1 avec un template
# 02d: je veux 2 digits pour afficher l'entier, 
# et s'il n'ya qu'un chiffre, je rajoute un zéro à gauche
# padding avec des zéros


## version 2 avec f-string

