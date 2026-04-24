"""
module text_cleaner

class Cleaner: nettoie un texte normal

class MathCleaner: nettoire un texte qui contient du LateX
"""

import re
import string

class Cleaner:
  # REM: utiliser les annotations de type (type hints) 
  # => qui déclenche l'autocomplétion de VSCode
  def __init__(self, text: str):
    self.__text = text
  
  def __clean_punctuation(self):
    self.__text = re.sub(f"[{string.punctuation}]", " ", self.__text)
  
  def __clean_breaks(self):
    # \n = Line Feed (LF) => Linux
    # \r\n = Carriage Return + LF (CRlf) => Windows
    # \r = Carriage Return (CR) => Mac OS
    self.__text = re.sub(f"\\r?\\n", " ", self.__text)

  def __clean_spaces(self):
    self.__text = re.sub(f" +", " ", self.__text)
  
  def __clean_short_words(self):
    words = self.__text.split()
    filtered_words = []
    for word in words:
      if len(word) > 3:
        filtered_words.append(word)
    self.__text = " ".join(filtered_words)

  def process(self):
    self.__clean_punctuation()
    self.__clean_breaks()
    self.__clean_spaces()
    self.__clean_short_words()
    return self.__text.lower()


class MathCleaner:
  def __init__(self, text: str):
    self.__text = text

  # utiliser les mêmes méthodes publiques => même interface 
  def process(self):
    pass