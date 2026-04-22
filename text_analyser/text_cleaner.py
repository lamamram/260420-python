from string import punctuation
import re

class Cleaner:
  def __init__(self, text: str):
    self.__text = text
    # le "tiret" dans une classe regex doit être à droite
    self.__punc = "".join(punctuation.split("-")) + "-"
  
  def __clean_punctuation(self) -> None:
    self.__text = re.sub(f"[{self.__punc}]", " ", self.__text)

  
  def __clean_line_breaks(self) -> None:
    # raw str = r"" ici \ veut dire \ et pas échappement
    self.__text = re.sub(r"\r?\n", " ", self.__text)
  

  def __clean_spaces(self) -> None:
    """ remplacer les suites d'espaces générées précédents  """
    self.__text = re.sub(r"\s+", " ", self.__text)

  def __clean_little_words(self, min_words: int):
    self.__text = " ".join(filter(
      lambda word: len(word) > min_words, 
      self.__text.split()
    ))

  def clean(self, min_words: int=3) -> str:
    self.__clean_punctuation()
    self.__clean_line_breaks()
    self.__clean_spaces()
    self.__clean_little_words(min_words)
    return self.__text.lower()