# %% ----------- gestion d'erreur avec une exception -------------------

# recréer la fonction division du cours des fonctions sans contôle

def division(a: float, b: float) -> float:
       """cette fonction retourne le résultat de la division de a par b"""
      #  if b == 0:
      #         return "division par zéro impossible"
       return a / b

## REM: en peut entourer un bout de code entre 
## l'entête try: 
##      alors le bloc du try s'exécute jusqu'à qu'une erreur survienne
##      s'il n'ya pas d'erreur le bloc try s'exécute jusq'au bout
## ET l'entête except
##       s'il y a erreur, le bloc try s'interromp et exécute le bloc except
if __name__ == "__main__":

  try:
    # number, num, denom = 10, 5, 10
    number, num, denom = 10, 5, 0
    resultat = division(num, denom)
    print(f"application d'un ratio à un nombre: {number * resultat}")
  except:
      print("il ya un pb")

# gérer le pb de dénominateur avec une exception

# %% ---------- capturer les erreurs individuellement ------------------

def division(a: float, b: float) -> float:
    """cette fonction retourne le résultat de la division de a par b"""
    #  if b == 0:
    #         return "division par zéro impossible"
    return a / b

# idem mais avec plusieurs pbs: 
#    ZeroDivisionError est traitée singulièrement
#    TypeError et KeyError sont traitées collectivement

try:
  produit, num, denom = {"prix":10}, 5, 10     # pas de pb
  # produit, num, denom = {"prix":10}, "5", 10 # TypeError 
  # produit, num, denom = {"prix":10}, 5, 0    # ZeroDivisionError
  # produit, num, denom = {"price":10}, 5, 10  # KeyError

  resultat = division(num, denom)
  print(f"application d'un ratio à un nombre: {produit["prix"] * resultat}")
except ZeroDivisionError as e:
    print(e, type(e))
except (TypeError, KeyError) as e:
    print(e, type(e))
except Exception as e:
    print(e, type(e))

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
from typing import Any
class RangeError(Exception):
    def __init__(self, interval: tuple, value: Any, *args):
        super().__init__(*args)
        self.interval = interval
        self.value = value
    
    def __str__(self):
        return f"{self.value} n'est pas entre {self.interval[0]} et {self.interval[1]}"
        

def average(notes: list) -> float:
    for n in notes:
        if not (0 <= n <= 20):
            # considération "métier"
            # raise ValueError(f"{n} n'est pas entre 0 et 20")
            raise RangeError((0, 20), n)
    return sum(notes) / len(notes)


if __name__ == "__main__":

  try:
      # notes = []
      # notes = [2, 7, 8, 20, 17]
      notes = [2, 7, 8, 22, 17, -4]
      avg = average(notes)
  except (ValueError, RangeError) as e:
      print(e, type(e))
  # le bloc else ne sera exécuté que si le try se termine sans erreur
  else:
      print(f"moyenne de {notes}: {avg}")
  # quelque soient les cas SURTOUT avant de planter 
  finally:
      print("quelque soient les cas SURTOUT avant de planter")
      
  
# 1. créer une liste de  notes de 0 -> 20 avec deux valeurs aberrantes -4 et 22
# 2. créer la fonction average qui calcule la moyenne
#    et calculer la moyenne de la liste de notes
# 3. utiliser le mot clé raise <classe>() qui génère une erreur si la note est aberrante
#    tip: trouver une erreur native de python de type XxxxxError
# 4. protéger le calcul de la moyenne des notes



# %%
