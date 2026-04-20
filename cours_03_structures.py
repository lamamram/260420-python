# %% ------------------ structure conditionnelle : le if ----------------------

balance = 1000
overdraft = 200

amount = input("Entrez un montant : ")
amount = int(amount)
# si le montant est négatif => afficher "Transaction refusée: {montant} négatif"

if amount < 0:
    print(f"Transaction refusée: {amount} négatif")
elif amount > balance + overdraft:
    print(f"Transaction refusée: {amount} fonds insuffisants")
else:
    print("Transaction acceptée")

# sinon mais si le montant trop important => "Transaction refusée: {montant} fonds insuffisants" 

# sinon => le retrait est effectué et "Transaction acceptée"


# %% ----------------- opérateur ternaire ---------------------------------

reponse = input("2+2 ?")
message = ""

# si la réponse est 4 => message vaut "bingo"
# sinon               => message vaut "perdu"
if reponse == "4":
    message = "bingo"
else:
    message = "perdu"
print(message)

# version sur une seule phrase
message = "bingo" if reponse == "4" else "perdu"
print(message)

# %% ---------------- opérateurs comparaison et logique ------------------

# prendre un int. savoir si l'entier est négatif ou nul
x = int(input("saisir un entier: "))
if x <= 0: print(f"{x} est négatif ou nul")


# savoir çà ET si c'est impair (idem en remplaçant ET par OU)
if x <= 0 and x % 2 != 0: print(f"{x} est négatif ou nul ET impair")
if x <= 0 or x % 2: print(f"{x} est négatif ou nul OU impair")  

# %% --------------- valeur fausses des built-ins et négation --------------

# prendre un str et la convertir en bool
x = input("saisir une str: ")
y = bool(x)
# idem avec une str vide 

# savoir si une str n'est pas vide
if x: print(f"{x} n'est pas vide")
# idem si elle est vide

# %% -------------------------- boucle for -----------------------------------
## REM: le for classique en informatique c'est: for(initialisaton; condition d'arrêt; changement)
## MAIS pour boucler en python avec le for, on DOIT itérer/consommer un ITERABLE
## ITERABLE == n'importe quelle variable qu'on peut mettre dans un for

mots = ["appeler", "un", "chat"]
# pour mot dans mots: afficher mot
for mot in mots:
    print(mot)


print("-"*20)

nom_complet = "John DOE"
# pour lettre dans nom_complet: afficher lettre 
for lettre in nom_complet:
    print(lettre)

# %% --------- générer une "série d'entiers" avec range() -------------------------

# pour i dans une range de 5 entiers depuis 0: afficher i


print("-"*20)

# pour i dans une range entre 2 et 5: afficher i

print("-"*20)

# pour i dans une range de 5 jusqu'à 0: afficher i


# %% ---------- transformation de liste en préservant la liste d'origine ------

fruits = ["pomme", "poire", "framboise"]

# afficher une liste des fruits en majuscule sans modifier fruits



# %% ----------- idem en modifiant directement de la liste d'origine --------

fruits = ["pomme", "poire", "framboise"]

# itérer sur les indices de la liste

print(fruits)


# %% -------------- idem avec la fonction - enumerate() -------------------

fruits = ["pomme", "poire", "framboise"]

# itérer à la fois avec les indices et les valeurs dans la boucle

print(fruits)


# %% --- interrompre l'exécution d'une boucle : break, continue, else ---

# prendre une range 5 pour afficher i et on s'arrête à 3
print("-"*10 + "break" + "-"*10)


# prendre une range 5 pour afficher i, sans afficher 3
print("-"*10 + "continue" + "-"*10)


# saisir j par le clavier. prendre une range 5 pour afficher i
# dans la boucle, casser la boucle si i==j
# en sortant de la boucle, tester si la boucle est sortie à cause du break ou non 
print("-"*10 + "else après for" + "-"*10)




# %% boucle while : tant qu'une condition est vraie: le bloc est exécutée

temp = int(input("saisir une temperature en °C: "))

# tant que la temp est sous 100°C: 
#     on roule donc on perd 10°C
#     afficher la temp
#     si la temp est sous 25°C:
#         on remet une pelettée de charbon dans la cheminée
#         donc on resaisit temp à partir du clavier
# afficher boom quand on sort de la boucle


# %% --------------- boucle infinie: condition toujours vraie --------------------------

# idem avec une boucle infinie