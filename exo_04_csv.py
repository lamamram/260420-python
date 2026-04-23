# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

3. déplacer le fichier csv en dans data/dns.csv
4.. ne faire ce qui précède qui si ce n'est pas déjà fait
hint: module os et pathlib.Path


5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- à chaque paquet de lignes, faire les opérations suivantes:
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""

import sys

import requests
import os
from pathlib import Path
from zipfile import ZipFile

URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
DNS_NAME = "dns.csv"

archive_name = URL.split("/")[-1]
p_archive = Path(f"./{archive_name}")

# if not os.path.exists(f"./{archive_name}")
if not p_archive.exists():
   try:
      # requête http de type GET de l'url qui retourne une réponse http
      response = requests.get(URL)

      # regarde de code de retour de la réponse
      if 200 <= response.status_code < 300:
      # regarde le type de donées
         if "application/zip" in response.headers["content-type"]:
         # response.content contient l'archive en octets
         # wb = création avec contenu binaire
            with open(f"./{archive_name}", mode="wb") as f:
               f.write(response.content)
      # en cas de mauvais code
      else:
         raise ValueError(f"réponse en erreur : {response.status_code}")
   except (requests.ConnectionError, ValueError) as e:
      print(e)
      sys.exit()

p_data = Path("./data")
if not p_data.exists():
  os.mkdir(p_data)

if not (p_data / DNS_NAME).exists():
   with ZipFile(p_archive) as zf:
      names = zf.namelist()
      zf.extract(names[0], path=p_data)
      os.rename(p_data / names[0], p_data / DNS_NAME)

# %%
