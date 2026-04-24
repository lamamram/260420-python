# %% ------ utilisation du module standard subprocess ----------
"""
subprocess permet de créer un processus enfant à partir du processus
parent, i.e, le processus python en exécution.

on l'utilise dans le cas d'une commande qu'on ne peut pas faire avec 
les outils de bases de python => commandes très complexes !!!
=> vous avez os, sys, et autres avec pip
"""

import subprocess
import shlex

# je veux savoir les noms des fichiers .py dans le dossier courant

# 1. je vais lancer une commande bash ls -1 *.py ou ls -1 | grep .py
# 2. et je veux voir la réponse

cmd = "ls -1 *.py"
tokens = ["ls", "-1", "*.py"]
lex_tokens = shlex.split(cmd)
# WARN 1. attention pas de shell pas d'excutable on exécute dans un tty
# WARN 2. il est recommandé d'écrire la commande en tant que TOKENS 
# ==> interdit certaines injections de commandes
# WARN 3. en cas de commnandes complexes avec options complexes MAIS SANS PIPE
# ==> utiliser shlex (analyseur lexical)

result = subprocess.run(
  lex_tokens,
  # sortie en texte: ajouter un flux de sortie stdout
  capture_output=True,
  text=True)

# return code: 0 == OK , non-zero == ERREUR
print(result.returncode)
print(result.stdout.splitlines())


# %% -------------- idem avec os -------------------

import os


print(list(filter(lambda p: p.endswith(".py"), os.listdir("."))))

# for p in os.listdir("."):
#   if p.endswith(".py"):
#     print(p)

# %%
