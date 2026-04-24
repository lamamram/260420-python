from text_analyser.text_cleaner import * 

class Counter:
  # def __init__(self, text: str, cleaner_type: str="normal"):
  #   if cleaner_type =="normal":
  #     self.__cleaner = Cleaner(text)
  #   else:
  #     self.__cleaner = MathCleaner(text)
  #   self.__text = self.__cleaner.process()

  def __init__(self, text: str):
    # utilisation de l'interface de la classe Cleaner
    # => composition d'objets
    self.__cleaner = Cleaner(text)
    self.__text = self.__cleaner.process()

  
  def analyze(self):
    words = self.__text.split()
    occurences = {}
    for word in words:
      if word in occurences:
        occurences[word] += 1
      else:
        occurences[word] = 1
    
    # changer le dictionnaire en une liste de tuples
    # pour trier la liste selon l'occurence (valeur d'indice 1 du tuple)
    # en ordre décroissant
    # on affiche les 5 premiers éléments
    # on reconvertit la liste de tuples en un dictionnaire
    return dict(sorted(
      occurences.items(), 
      key=lambda tup: tup[1], 
      reverse=True
    )[:5])
