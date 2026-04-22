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

# ici ce bloc empêche le print quand le module est importé
if __name__ == "__main__":
    print(parse_template("blabla {{value}}", {"value": 50}, debug=DEBUG))