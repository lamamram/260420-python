# %% un exemple en programmation impérative / procédurale 
# sans programmation orientée objet

## initialisations

# ce dictionnaire représente la strucutre générique d'un compte
account = {
  "balance": 0,
  "overdraft": 0,
}

# créer une fonction init_account qui va mettre à jour les champs d'un dict account en param
# à partir de paramètres balance et overdraft
def init_account(account: dict, balance: float, overdraft: float) -> dict:
  account["balance"] = balance
  account["overdraft"] = overdraft
  return account

# créer une fonction withdraw pour effectuer un retrait d'un montant sur un compte en param.
def withdraw(account: dict, amount: float):
  if amount < 0:
    print(f"Transaction refusée: {amount} négatif")
  elif amount > account["balance"] + account["overdraft"]:
    print(f"Transaction refusée: {amount} fonds insuffisants")
  else:
    account["balance"] -= amount
    print(f"Transaction acceptée")

## programme principal
if __name__ == "__main__":
  # initialiser le dictionnaire account avec un solde de 1000 et un découvert de 200
  personal_account = init_account(account, balance=1000, overdraft=200)
  # saisir un montant, effectuer le retrait et afficher le solde après
  amount = input("Entrez un montant : ")
  amount = int(amount)

  withdraw(personal_account, amount)
  print(f"nouveau solde: {personal_account["balance"]}")
  
# %% --- même exemple en Programmation Orientée Objet (POO) ---------

## REM. Classe  == Type de donnée en python
## les classes sont nommées en PascalCase ou camelCase != snake_case
class Account:

    # "variables internes" => ATTRIBUTS et en particuliuer les attributs de classe
    balance: float = 0
    overdraft: float = 0

    # "fonctions internes" => METHODE == ATTRIBUT de type fonction 
       # account est l'objet lui même 
       # => donc on a pas besoin de l'ajouter quand l'objet instancié appelle la méthode
       # on accède aux éléments internes avec l'opérateur "."

    def withdraw(account, amount: float):
      if amount < 0:
        print(f"Transaction refusée: {amount} négatif")
      elif amount > account.balance + account.overdraft:
        print(f"Transaction refusée: {amount} fonds insuffisants")
      else:
        account.balance -= amount
        print(f"Transaction acceptée")

## programme principal

if __name__ == "__main__":
  
  ## REM. on peut appeler une classe et retourner une variable de type Account 
  ## => le terme exact est instancier (créer) un objet de cette classe
  # 1. créer un objet account à partir de l'instanciation de la classe()
  personal_account = Account()
  # 2. donner 1000 au solde de l'objet account et 200 au découvert d'account
  personal_account.balance = 1000
  personal_account.overdraft = 200
  # 3. faire un retrait
  personal_account.withdraw(500)
  print(f"nouveau solde: {personal_account.balance}")

# %% --------------------- utilisation de la méthode magique __init__() ------------

class Account:

    # en utilisant __init__ on a pas forcément besoin d'attributs de classe
    # balance: float = 0
    # overdraft: float = 0
 
    # self est l'objet lui même
    # un attribut/méthode de forme __xxxx__ est un attribut/méthode MAGIQUE 
    # def init_account(self, balance: float, overdraft: float) -> dict:
    def __init__(self, balance: float, overdraft: float):
      # ici ce sont des attributs d'objets
      self.balance = balance
      self.overdraft = overdraft
      # return self: pas besoin car l'objet est DEJA CREE !!!


    def withdraw(self, amount: float):
      if amount < 0:
        print(f"Transaction refusée: {amount} négatif")
      elif amount > self.balance + self.overdraft:
        print(f"Transaction refusée: {amount} fonds insuffisants")
      else:
        self.balance -= amount
        print(f"Transaction acceptée")

## programme principal

if __name__ == "__main__":
  
  personal_account = Account(1000, 200)
  # personal_account = Account()
  # personal_account.init_account(1000, 200)
  personal_account.withdraw(500)
  print(f"nouveau solde: {personal_account.balance}")


# %% ------------------ encapsulation frauduleuse en python ------------------

class Account:

  def __init__(self, balance, overdraft):
    self.balance = balance
    # préfixer un attribut avec "__" rend l'attribut "privé"
    self.__overdraft = overdraft
  
  def get_overdraft(self) -> float:
    """
    getter pour retourner l'attribut "privé" à partir de l'intérieur de la classe
    """
    return self.__overdraft 

if __name__ == "__main__":
  acc = Account(1000, 200)
  # par défaut les attributs sont publics
  print(acc.balance)
  
  amount = 500
  # AttributeError: on ne peut pas lire les attributs de type "__"
  # limit = acc.balance + acc.__overdraft
  # WTF: écriture sur un attribut "__" ???
  acc.__overdraft = 400
  limit = acc.balance + acc.__overdraft
  
  if amount <= limit:
    acc.balance -= amount
    print(f"nouveau solde: {acc.balance}", f"nouveau découvert: {acc.get_overdraft()}")
    print(f"attributs REELS de l'objet acc: {dir(acc)}")
    # l'attribut "prive" crée dans __init__ s'appelle en réalité '_Account__overdraft'
    print(acc._Account__overdraft, acc.__overdraft)
    # le fameur attribut __overdraft n'existe dans le programme principal
    # MAIS si je le créé => ligne 141, je peux l'utiliser MAIS il n'est pas _Account__overdraft !!!

##### MORALE DE L'HISTOIRE ##################
"""
il n'ya pas en réalité d'attributs privés => pas d'encapsulation effective
par contre, on peut l'utiliser pour STRUCTURER VOS CLASSES
protected en python c'est _var => public mais n'est pas spécifié dans la documentation
"""

# %% ------------- en python: TOUT EST OBJET ---------------------
# instancier un objet t d'une classe Truc vide
class Truc:
  pass # un mot clé et une instruction qui ne fait rien pour créer un bloc vide !!!

t = Truc()

dico = dict(k1=1, k2=2)

print(type(t), type(dico))
print(isinstance(t, Truc), isinstance(dico, dict))

# créer un dictionnaire d à partir de la fonction dict et des paramètres nommés

# afficher le type de t et de d
# vérifier que t est d'instance de Truc  et d instance de dict avec isinstance()


# %% ------------------------ exemple client ---------------------------------

# créer une classe client qui contient firstname, name, et date_joint
# et 2 méthodes: 
#     get_full_name: retourne le prénom capitalisé et le nom en majuscule
#     get_date_joint: retourne la date dans le format voulu en paramètre

from datetime import datetime
class Client:

  def __init__(self, firstname: str, name: str, date_joint: str, format: str="%Y-%m-%d"):
    self.firstname = firstname
    self.name = name
    self.date_joint: datetime = datetime.strptime(date_joint, format)

  def get_full_name(self) -> str:
    return f"{self.firstname.capitalize()} {self.name.upper()}"

  def get_date_joint(self, format: str="%Y-%m-%d") -> str:
    return self.date_joint.strftime(format)

if __name__ == "__main__":
  client = Client("john", "doe", "2024-01-01")
  print(client.get_full_name())
  print(client.get_date_joint("%d/%m/%Y"))



# %% -------------------------- héritage simple -----------------------------

# reprendre l'exemple précédent sachant qu'un client EST une personne avec un prénom et un nom
## person est considérée comme classe parente de client
## client est //                      enfant de personne , hérite de personne

## la classe enfant peut réutiliser directement les méthodes parentes
## la classe enfant peut également créer ses propres méthodes
## super().<methode>() permet d'exécuter une méthode de la classe PARENT 
## dans la classe ENFANT et sur l'objet ENFANT

# classe personne
#    utilise prénom et nom

# classe client est une personne
#    utilise prénom, nom et date_joint      

class Person:
  
  def __init__(self, firstname: str, name: str):
    self.firstname = firstname
    self.name = name

  def get_full_name(self) -> str:
    return f"{self.firstname.capitalize()} {self.name.upper()}"
  
class Client(Person):

  def __init__(self, firstname: str, name: str, date_joint: str, format: str="%Y-%m-%d"):
    # super() permet d'appeler une méthode de la classe parente
    super().__init__(firstname, name)
    self.date_joint: datetime = datetime.strptime(date_joint, format)

  def get_date_joint(self, format: str="%Y-%m-%d") -> str:
    return self.date_joint.strftime(format)

if __name__ == "__main__":
  client = Client("john", "doe", "2024-01-01")
  print(client.get_full_name())
  print(client.get_date_joint("%d/%m/%Y"))

# %% ------------------------- injection de dépendances -----------------------------

# relation de type AVOIR entre une classe "utilisateur" et une autre qui est une dépendance
# l'utilisateur mange sa dépendance à l'instanciation et utilise LA SIGNATURE PUBLIQUE de cette dépendance

from tools import Account, Client

cl = Client("john", "doe", "2016-04-22")
acc = Account(1000, 200, cl)

print(acc.get_client_full_name())

acc.bonus_10()
print(acc.get_balance())

# %%
