# https://dictionaryapi.dev/ #
import requests as r
contents = r.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello").json()[0]

for x in contents:
  print(contents[x]) 
