# https://dictionaryapi.dev/ # API Utilised
import os; # To run terminal commands
#os.system('cls'); # Clear the terminal before the programme runs
import requests as r; # To retrieve API data

while True: # User can query as many words as they like without needing to re-start the programme each time
    wordChoice = input("Enter word:\n"); #
    try: contents = r.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + wordChoice.lower()).json()[0]; # Retrieve the raw API data
    except: print("Error 404 Word not found!"); continue # Try again if malformed input is received.

    options = ""; # 
    for a in contents: 
        if (a != "sourceUrls" and a != "license"): options += a + ", "; # Aquire all dictionary keys

    group = input("\nOptions:\n" + options[6:len(options)-2] + '\n'); # The dictionary key the user wants

    if (group == "phonetic"):
        print(contents[group])
        continue; 

    try: rawText = contents[group][:-(len(contents[group])-1)][0] # I have no idea whats going on but this somehow deletes like 100 useless characters off the end of the information so DONT TOUCH IT; ITS DEEP MAGIC
    except: print("Contents inextractable!"); continue # Not going to deal with it if its not the most common case

    print();  # For aesthetics, obviously, we need to be 可愛い～！
    if (type(rawText) == dict):
        for a in rawText: # Iterate through all the dictionary keys~
            if (a != "license"): # No-one cares about the license!
                print(a + ':', rawText[a]); 
    else:
        print(rawText)
                


    if input("\nSatisfied? (Y/n)\n") == 'Y': break; # Escape!!!!!!