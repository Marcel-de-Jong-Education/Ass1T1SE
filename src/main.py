# https://dictionaryapi.dev/ # API Utilised
import os; # To run terminal commands
os.system('cls'); # Clear the terminal before the programme runs
import requests as r; # To retrieve API data
from colorama import Fore

print( # Idk why but the code breaks without this
    r"""   ,--"""",--.__,---[],-------._         """ + '\n' +
    r"""  ,"   __,'            \         \--""""""==;- """+ '\n' +
    r"""    ," _,-"  "/---.___     \       ___\   ,-''," """+ '\n' +
    r"""     /,-'      / ;. ,.--'-.__\  _,-"" ,| `,'   / """+ '\n' +
    r"""    /``""""-._/,-|:\       []\,' ```-/:;-. `. / """+ '\n' +
    r"""              `  ;:::      ||       /:,;  `-.\ """+ '\n' +
    r"""                 =.,'__,---||-.____',.= """+ '\n' +
    r"""                 =(:\_     ||__    ):)= """+ '\n' +
    r"""                 =(:\_     ||__    ):)= """+ '\n' +
    r"""                ,"::::`----||::`--':::"._ """+ '\n' +
    r"""              ,':::::::::::||::::::::::::'. """+ '\n' +
    r"""     .__     ;:::.-.:::::__||___:::::.-.:::\     __, """+ '\n' +
    r"""           -;:::( O )::::>_|| _<::::( O )::::-""" + '\n' + 
    r"""    =======;:::::`-`:::::::||':::::::`-`:::::\======= """+ '\n' +
    r"""     ,--"";:::_____________||______________::::""----.          , , """+ '\n' +
    r"""          ; ::`._(    |    |||     |   )_,'::::\_,,,,,,,,,,____/,'_, """+ '\n' +
    r"""        ,;    :::`--._|____[]|_____|_.-'::::::::::::::::::::::::);_ """+ '\n' +
    r"""       ;/ /      :::::::::,||,:::::::::::::::::::::::::::::::::::/ """+ '\n' +
    r"""      /; ``''''----------/,'/,__,,,,,____:::::::::::::::::::::," """+ '\n' +
    r"""      ;/                :);/|_;| ,--.. . ```-.:::::::::::::_," """+ '\n' +
    r"""     /;                :::):__,'//""\\. ,--.. \:::,:::::_," """+ '\n' +
    r"""    ;/              :::::/ . . . . . . //""\\. \::":__," """+ '\n' +
    r"""    ;/          :::::::,' . . . . . . . . . . .:`::\ """+ '\n' +
    r"""    ';      :::::::__,'. ,--.. . .,--. . . . . .:`::` """+ '\n' +
    r"""    ';   __,..--'''-. . //""\\. .//""\\ . ,--.. :`:::` """+ '\n' +
    r"""    ;    /  \\ .//""\\ . . . . . . . . . //""\\. :`::` """+ '\n' +
    r"""    ;   /       . . . . . . . . . . . . . . . . .:`::` """+ '\n' +
    r"""    ;   (          . . . . . . . . . . . . . . . ;:::` """+ '\n' +
    r"""    ,:  ;,            . . . . . . . . . . . . . ;':::` """+ '\n' +
    r"""    ,:  ;,             . . . . . . . . . . . . .;`::: """+ '\n' +
    r"""    ,:   ;,             . . . . . . . . . . . . ;`::;` """+ '\n' +
    r"""     ,:  ;             . . . . . . . . . . . . ;':::;` """+ '\n' +
    r"""      :   ;             . . . . . . . . . . . ,':::; """+ '\n' +
    r"""       :   '.          . . . . . . . .. . . .,':::;` """+ '\n' +
    r"""        :    `.       . . . . . . . . . . . ;::::;` """+ '\n' + 
    r"""         '.    `-.   . . . . . . . . . . ,-'::::; """+ '\n' +
    r"""           `:_    ``--..___________..--'':::::;'` """+ '\n' +
    r"""              `._::,.:,.:,:_ctr_:,:,.::,.:_;'` """+ '\n' +
    r"  ________________`" + '"' + str("\\") + "/" + '"' + str("\\") + '/' + str("\\") + '/' + """ '"""" """ + '`' + str("\\") + "/" + '"' + str("\\") + "/" + '"' + '"' + str("\\") + "/" + '"' + "____________________________ "
    ,end = "\n\n\n\n"
    )

while True: # User can query as many words as they like without needing to re-start the programme each time
    print(
        Fore.LIGHTMAGENTA_EX +
        "Query History:\n✨————————————————✧—♥—✧————————————————✨" # Powershell is utf-8 encoded, this is totally fine!
        + open(os.getcwd()[:-3] + "\\user_history\\guest_history.txt",'r').read(),
        end="\n✨————————————————✧♥✧————————————————✨\n"
        )

    wordChoice = input("Enter word:\n" + Fore.WHITE); #
    open(os.getcwd()[:-3] + "\\user_history\\guest_history.txt",'a').write('\n'+wordChoice) # Will save requests even if they're invalid. and thats okay!! <3
         
    try: contents = r.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + wordChoice.lower()).json()[0]; # Retrieve the raw API data
    except: print(Fore.RED + "Error 404 Word not found!" + Fore.WHITE); continue # Try again if malformed input is received.

    options = ""; # 
    for a in contents: 
        if (a != "sourceUrls" and a != "license"): options += a + ", "; # Aquire all dictionary keys

    group = input(Fore.LIGHTMAGENTA_EX + "\nOptions:\n" + options[6:len(options)-2] + '\n' + Fore.WHITE); # The dictionary key the user wants

    if (group == "phonetic"):
        print(Fore.LIGHTMAGENTA_EX + contents[group])
        if input("\nSatisfied? (Y/n)\n" + Fore.WHITE) == 'Y':break; # Escape!!!!!!
        continue; 

    try: rawText = contents[group][:-(len(contents[group])-1)][0] # I have no idea whats going on but this somehow deletes like 100 useless characters off the end of the information so DONT TOUCH IT; ITS DEEP MAGIC
    except: print(Fore.RED + "Contents inextractable!" + Fore.WHITE); continue # Not going to deal with it if its not the most common case

    print(Fore.LIGHTMAGENTA_EX);  # For aesthetics, obviously, we need to be 可愛い～！
    if (type(rawText) == dict):
        for a in rawText: # Iterate through all the dictionary keys~
            if (a != "license"): # No-one cares about the license!
                print(a + ':', rawText[a]); 
    else:
        print(rawText)

    
                


    if input("\nSatisfied? (Y/n)\n" + Fore.WHITE) == 'Y':break; # Escape!!!!!!