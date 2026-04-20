# %% un exemple en programmation impérative / procédurale 
# sans programmation orientée objet

## initialisations

# ce dictionnaire représente la strucutre générique d'un compte
account = {
  "balance": 0,
  "overdraft": 0,
}

# créer une fonction init_account qui va mettre à jour les champs d'un dict account en param
# à partir de paramètres blance et overdraft


# créer une fonction withdraw pour effectuer un retrait d'un montant sur un compte en param.


## programme principal

# initialiser le dictionnaire account avec un solde de 1000 et un découvert de 200

# saisir un montant, effectuer le retrait et afficher le solde après

  
# %% --- même exemple en Programmation Orientée Objet (POO) ---------

## REM. Classe  == Type de donnée en python
## les classes sont nommées en CamelCase != snake_case

    
    # "variables internes" => ATTRIBUTS


    # "fonctions internes" => METHODE == ATTRIBUT de type fonction
       # un attribut/méthode de forme __xxxx__ est un attribut/méthode MAGIQUE 
       # self est l'objet lui même
       # on accède aux éléments internes avec l'opérateur "."

## programme principal

## REM. on peut appeler une classe et retourner une variable de type Account 
## => le terme exact est instancier (créer) un objet de cette classe

# 1. créer un objet account à partir de l'instanciation de la classe()

# 2. donner 1000 au solde de l'objet account et 200 au découvert d'account

# 3. faire un retrait

# 4. refaire et 2. 3. avec la méthode __init__


# %% ------------- en python: TOUT EST OBJET ---------------------

# instancier un objet t d'une classe Truc vide

# créer un dictionnaire d à partir de la fonction dict et des paramètres nommés

# afficher le type de t et de d
# vérifier que t est d'instance de Truc  et d instance de dict avec isinstance()


# %% ------------------------ exemple client ---------------------------------

# créer une classe client qui contient firstname, name, et date_joint
# et 2 méthodes: 
#     get_full_name: retourne le prénom capitalisé et le nom en majuscule
#     get_date_joint: retourne la date dans le format voulu en paramètre


# %% -------------------------- héritage simple -----------------------------

# reprendre l'exemple précédent sachant qu'un client EST un personne avec un prénom et un nom
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