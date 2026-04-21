# %%
###### "matcher une regex"
# match == détecter la regex au début de la cible
import re

pattern = "([013456789][0-9]{4}|2[0-9AB][0-9]{3})"

re.match(pattern=pattern, string="44500")
re.match(pattern=pattern, string="44500 est mon zipcode")
print(re.match(pattern=pattern, string="mon zipcode est 44500"))

# %%
###### chercher le pattern de 1ère occurence dans la cible
import re

pattern = "([013456789][0-9]{4}|2[0-9AB][0-9]{3})"
re.search(pattern=pattern, string="mon zipcode est 44500")
re.search(pattern=pattern, string="mon zipcode est 44500 non 75013")

# %%
####### chercher tous le match d'un pattern dans la cible
import re

pattern = "([013456789][0-9]{4}|2[0-9AB][0-9]{3})"
re.findall(pattern=pattern, string="mon zipcode est 44500 non 75013")

# %%
####### sub(): search & replace du pattern
import re

pattern = "([013456789][0-9]{4}|2[0-9AB][0-9]{3})"
re.sub(pattern=pattern, repl="********", string="mon zipcode est 44500 non 75013")

# %%
