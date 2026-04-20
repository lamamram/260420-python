# %% ----------- gestion d'erreur avec une exception -------------------

# recréer la fonction division du cours des fonctions sans contôle

## REM: en peut entourer un bout de code entre 
## l'entête try: 
##      alors le bloc du try s'exécute jusqu'à qu'une erreur survienne
##      s'il n'ya pas d'erreur le bloc try s'exécute jusq'au bout
## ET l'entête except
##       s'il y a erreur, le bloc try s'interromp et exécute le bloc except

number, num, denom = 10, 5, 10
# number, num, denom = 10, 5, 0
resultat = division(num, denom)
print(f"application d'un ratio à un nombre: {number * resultat}")

# gérer le pb de dénominateur avec une exception

# %% ---------- capturer les erreurs individuellement ------------------

# idem mais avec plusieurs pbs: 
#    ZeroDivisionError est traitée singulièrement
#    TypeError et KeyError sont traitées collectivement

produit, num, denom = {"prix":10}, 5, 10     # pas de pb
# produit, num, denom = {"prix":10}, "5", 10 # TypeError 
# produit, num, denom = {"prix":10}, 5, 0    # ZeroDivisionError
# produit, num, denom = {"price":10}, 5, 10  # KeyError

resultat = division(num, denom)
print(f"application d'un ratio à un nombre: {number * resultat}")

## REM except: capture tout mais sans information sur le type de pb
## except <classe>: capture une erreur de sa classe 
## except (<classe1>, <classe2>) : capture la 1ère erreur liée au tuple de classes d'exception 
## except <classe> as e: //
##                       et injecte un objet exception e dans le bloc


## TIP: quand on veut protéger un code donnée
# 1/ on commence en mettant Exception qui capture tout
# 2/ à l'usage, on voit les erreurs fréquentes et on individualise les traitements de erreurs
# 3/ si l'on voit des types d'erreurs qui seront gérées de la même façon, alors on peut les capturer en même temps

# %% --- lever une exception nous même quand on a un pb "métier" ---------

# 1. créer une liste de  notes de 0 -> 20 avec deux valeurs aberrantes -4 et 22
# 2. créer la fonction average qui calcule la moyenne
#    et calculer la moyenne de la liste de notes
# 3. utiliser le mot clé raise <classe>() qui génère une erreur si la note est aberrante
#    tip: trouver une erreur native de python de type XxxxxError
# 4. protéger le calcul de la moyenne des notes


