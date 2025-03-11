# https://dictionaryapi.dev/ # API Utilised
import os # To run terminal commands
os.system('cls') # Clear the terminal before the programme runs
import requests as r # To retrieve API data

while True: # User can query as many words as they like without needing to re-start the programme each time
  wordChoice = input("Enter word:\n") #
  try: contents = r.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + wordChoice.lower()).json()[0] # Retrieve the raw API data
  except: print("Error 404 Word not found!"); continue # Try again if malformed input is received.

  options = "" # 
  for a in contents: options += a + ", " # Aquire all dictionary keys

  group = input("Options:\n" + options[6:len(options)-2] + '\n') # The dictionary key the user wants

  things = []
  appTo = False
  tol = 0
  rawG = str(contents[group])
  for i in range(len(rawG)):
      rawGinx = rawG[-(i+1)] # todo: make better

      if appTo:
          things[-1] += rawGinx

      if rawGinx == ':':
          appTo = True
          things.append("")
      elif rawGinx == "'":
          tol += 1
          if tol == 2:
              appTo = False
              tol = 0
          
  for thing in things:
      print(thing[::-1], end=", ")

  wantToFind = input("\nFind..?\n")
  result = rawG[rawG.find(wantToFind) + len(wantToFind) + 4:]
  for a in result:
      #if a == "'": break
      print(a, end='')

  
  if input("\nSatisfied? (Y/n)\n") == 'Y': break