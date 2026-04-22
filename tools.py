from datetime import datetime

DEBUG = True

def parse_template(
    tpl: str, 
    data: dict, 
    delims: tuple=("{{", "}}"), 
    default="N/A",
    **opts
) -> str:
  while delims[0] in tpl:
    index_start = tpl.find(delims[0]) + len(delims[0])
    index_end = tpl.find(delims[1])
    key = tpl[index_start:index_end]
    if "debug" in opts and opts["debug"]:
        print(f"key trouvée: {key}")
    tpl = tpl.replace(delims[0] + key + delims[1], str(data.get(key, default)))

  return tpl

################################ ACCOUNT ########################

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

class Account:

  def __init__(self, balance: str, overdraft: str, client: Client):
    self.__balance = balance
    self.__overdraft = overdraft
    self.__client = client
  
  def get_overdraft(self) -> float: return self.__overdraft
  def get_balance(self) -> float: return self.__balance

  def withdraw(self, amount: float):
      if amount < 0: print(f"Transaction refusée: {amount} négatif")
      elif amount > self.balance + self.overdraft: print(f"Transaction refusée: {amount} fonds insuffisants")
      else:
        self.balance -= amount
        print(f"Transaction acceptée")
  
  def get_client_full_name(self):
     return self.__client.get_full_name()
  
  def bonus_10(self):
    """
    si la date courante est le 10ème anniv du client
    alors le solde est incrémenté de 100
    """
    pass
   

# ici ce bloc empêche le print quand le module est importé
if __name__ == "__main__":
    print(parse_template("blabla {{value}}", {"value": 50}, debug=DEBUG))