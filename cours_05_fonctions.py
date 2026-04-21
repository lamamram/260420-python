# %% ---------- définition et appel d'une fonction -----------------------
### une fonction est un objet créé/définie avec: 
### le mot clé def suivi de <nom_de_la_fonction>(): 
###     et après un bloc d'instructions  

# définition d'une fonction ma_fonction() qui contient l'affichage de "coucou"
def ma_fonction():
    print("coucou")

### pour exécuter le bloc de la définition, on doit appeler la fonction 
### <nom_de_la_fonction>()
### (): opérateur d'appel
### une fonction est un type de donnée dite "callable"

# afficher l'appel de la fonction ma_fonction
print("appel de ma_fonction() => ", ma_fonction())
# %% ----------- retour d'une fonction ------------------------------

# même définition mais en remplaçant le print("coucou") par le mot clé return et 'coucou'
def ma_fonction():
  return "coucou"
  x = 5 # cette ligne ne sera jamais exécutée car elle est après le return

# afficher l'appel de la fonction
print("appel de ma_fonction() => ", ma_fonction())
# alternativement, on peut affecter l'appel de la fonction dans une variable
ret = ma_fonction()
# %% -- définition d'une fonction avec des paramètres et appel des paramètres ---

# définir une fonction qui ajoute 2 entiers en paramètres et qui retourne la somme 
# a, b dans la définition de la focntions sont des paramètres formels
def addition(a, b):
    c = 2 # c est une variable locale à la fonction
    return a + b + c

a, b = 5, 10 # a et b sont des variables globaes du programme
# injection des variables globales en tant que paramètres d'appel: passage en référence
print(f"appel de addition({a}, {b}) => ", addition(a, b))
# print(f"appel de addition("ff", "rr") => ", addition("ff", "tt")) ERROR
# %% ------------ annotations, documentation et contrôle -------------------


# créer une fonction division de 2 floats qui retourne un float
def division(a: float, b: float) -> float:
       """cette fonction retourne le résultat de la division de a par b"""
       if b == 0:
              return "division par zéro impossible"
       return a / b

# les annotations ne sont pas des contrôles, ce ne sont que des indications
def division(a: float, b: float) -> tuple:
       """DOCSTRING: cette fonction retourne le résultat de la division de a par b"""
       retour, erreur = 0, ""
       if b == 0:
              erreur = "division par zéro impossible"
       else:
             retour = a / b
       return retour, erreur

ret, err = division(5, 0)
print(f"résultat: {ret} et erreur: {err}")
# 1. en notifiant les types d'entrée et de sortie de la fonction
# 2. documenter la fonction en ajoutant une """doctstring""" au début du bloc
# 3. faire un contrôle sur le dénominateur

# %% --------------- passage en référence de types mutables et immutables ------------------

def test_immmutable(x: int):
      x += 1
      print(x, id(x))
      return x

x = 5
test_immmutable(x)
print(x, id(x)) # x global n' a pas changé car x est immutable => le x local ne peut pas être référencé à x global

def immmutable(l: list, elem: int):
      l.append(elem)
      print(l, id(l))
      return l

l = [1, 2, 3]
immmutable(l, 4)
print(l, id(l)) # l global a changé car l est mutable => le l local

# %% --------------- types de paramètres ----------------------------------

# créer une fonction calcul_tva qui prend 2 paramètres le prix ht et le taux
# et retourne la valeur de tva sur ce prix et ce taux
# 1. annotations et documentation
# 2. le prix est arbitraire => paramètre positionnel / obligatoire
# MAIS on considère que la valeur par défaut du taux est 20 => paramètre nommé / optionnel

# def calcul_tva(taux: float=20, prix_ht: float) -> float: # erreur: positionnel et après nommés
def calcul_tva(prix_ht: float, taux: float = 20) -> float:
    """cette fonction retourne la valeur de tva sur un prix ht et un taux"""
    return prix_ht * taux / 100

# appeler la fonction sans paramètres

print(f"""appel positionnel: 199 -> prix_ht, 5.5 -> taux 
       => { calcul_tva(199, 5.5) }""")
print(f"""appel avec un paramètre optionnel: 199 -> prix ht et rien -> taux
       => { calcul_tva(199) }""")
print(f"""appel nommé: les valeurs sont fléchées vers les paramètres 
       => pas besoin d'ordre => { "???" }""")

# calcul_tva(taux=5.5, 199) # erreur: d'abord positionnel puis nommé
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




