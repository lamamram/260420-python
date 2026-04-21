# %% ------------ import d'un module avec espace de nom ----------------

## un fichier d'extension .py avec du code python est un MODULE
## si ce module ne contient que des définitions de variables, fonctions, classes
##    ce module est une bibliothèque/librairie
## le module qui est exécuté directement par l'interpréteur python ou jupyter
##    est appelé module principal

# 1. créer un module tools qui contient la fonction de l'exercice template
import tools

# 2. importer le module est exécuter la fonction dans le module principal
# tools est une variable de type module qu'on appelle espace de nom du module
tools.parse_template("blabla {{value}}", {"value": 50}, debug=tools.DEBUG)

# %% -- à partir d'un module, importer une fonction => sans espace de nom ----
# idem sans espace de nom

from tools import parse_template, DEBUG

parse_template("blabla {{value}}", {"value": 50}, debug=DEBUG)

# %% -- gérer les conflits de noms => alias
# idem en changeant le nom de la fonction à l'import
from tools import parse_template as parse

parse_template = "qqch d'autre"

parse("blabla {{value}}", {"value": 50}, debug=DEBUG)

# %% --- exemples d'utilisation de modules de la bibliothèque standard ------
# exemple de datetime
# importer l'objet datetime à partir du module datetime

# créer une variable dt représente la date d'aujourd'hui avec la signature de base 


# idem avec une fonction interne

# idem à partir de la chaine de caractère "2026-04-01 15:30" et le format "%Y-%m-%d %H:%M" 

# à partir de la variable, afficher l'année, la date au format "%d/%m/%Y", le nb de secondes à partir le 1er janvier 1970

# afficher la durée entre la fin de la journée et maintenant, en heures, min, s


# %% ------------- import d'un module d'un package ------------------------

## un package est un dossier qui contient un ou des modules ou des sous packahes 
## et qui contient un fichier nommé __init__.py qui peut être vide

# créer un package utils et copier le module tools dans utils
# importer tools à partir de utils

# à partir du module tools dans le package, importer la fonction


# %% ------------ programme principal ------------------

# 1. afficher le nom du programme principal: nom du module courant
# 2. afficher le nom d'un module importé
# 3. comment certifier qu'un code d'un module donné ne s'exécutera que si le module est principal