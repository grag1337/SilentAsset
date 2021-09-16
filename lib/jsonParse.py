import json
from colorama import Fore,Back,Style
from os import system,name

banner = """
  ██████  ██▓ ██▓    ▓█████  ███▄    █ ▄▄▄█████▓ | Alpha v1.5
▒██    ▒ ▓██▒▓██▒    ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
░ ▓██▄   ▒██▒▒██░    ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
  ▒   ██▒░██░▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
▒██████▒▒░██░░██████▒░▒████▒▒██░   ▓██░  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░░▓  ░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
░ ░▒  ░ ░ ▒ ░░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░    ░    
░  ░  ░   ▒ ░  ░ ░      ░      ░   ░ ░   ░      
      ░   ░      ░  ░   ░  ░         ░          
                                                
 ▄▄▄        ██████   ██████ ▓█████▄▄▄█████▓ | github.com/grag1337    
▒████▄    ▒██    ▒ ▒██    ▒ ▓█   ▀▓  ██▒ ▓▒     
▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒███  ▒ ▓██░ ▒░     
░██▄▄▄▄██   ▒   ██▒  ▒   ██▒▒▓█  ▄░ ▓██▓ ░      
 ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒████▒ ▒██▒ ░      
 ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒ ░░        
  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ░  ░   ░         
  ░   ▒   ░  ░  ░  ░  ░  ░     ░    ░           
      ░  ░      ░        ░     ░  ░             
"""

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def begParse(reqLoc):
    jsonInit = open(reqLoc,'r')
    jsonData = json.loads(jsonInit.read())
    jsonInit.close()
    print(f"{Fore.LIGHTRED_EX}{banner}{Fore.RESET}")
    print(jsonData["urls"])
    print(jsonData["headers"])