# import entre module/sous package dans un package
# règle => les imports sont résolus à partir du programme principal
from text_analyser.text_cleaner import Cleaner

class Counter:

  # def __init__(self, text: str):
  #   """ classes indép. """
  #   self.__text = text

  # def __init__(self, text: str):
  #   """ 
  #   couplage: Counter sait comment instancier, utilise, ET supprime sa dépendance
  #   inconvénient: bcp de responsabilités | cleaner change son instanciation => counter plante
  #   Avantage: le programme principal est easy
  #   """
  #   self.__text = Cleaner(text).clean()
  
  def __init__(self, cleaner: Cleaner, min_words: str=3):
    self.__text = cleaner.clean(min_words)

  def get_occurences(self, limit: int=5) -> dict:
    occurences = {}
    for word in self.__text.split():
      if word in occurences:
        occurences[word] += 1
      else:
        occurences[word] = 1

    return dict(sorted(
      occurences.items(), 
      key=lambda tup: tup[1], 
      reverse=True
    )[:limit])