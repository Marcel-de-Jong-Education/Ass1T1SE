# https://dictionaryapi.dev/ #
import os
os.system('cls')
import requests as r

while True:
  wordChoice = input("Enter word:\n")
  try: contents = r.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + wordChoice.lower()).json()[0]
  except: print("Error 404 Word not found!"); continue

  options = ""
  for a in contents: options += a + ", "

  group = input("Options:\n" + options[6:len(options)-2] + '\n')

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