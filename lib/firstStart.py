import os
from os import system,name
from colorama import Fore,Back,Style
banner = """
  ██████  ██▓ ██▓    ▓█████  ███▄    █ ▄▄▄█████▓ | v1.0 
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

def checkFor():
    global choiceVar 
    choiceVar = 0
    if os.path.isdir(os.getcwd()+"/githubRepos") == False:
        print(f"{Fore.RED}{banner}{Fore.RESET}")
        print(f"{Fore.RED}\n♦ Thanks for using Silent Asset for the first time! ♦\n ♦ We're going to have to do some setup before you begin ♦\n ♦ Would you like to do this now? ♦\n{Fore.RESET}")
        choice = input(f"{Fore.RED} (y/n) ►{Fore.CYAN} ")
        if choice == "y" or choice == "Y" or choice == "Yes" or choice == "yes" :
            setup()
        else:
            choiceVar += 1
    else:
        None
def setup():
    try:
        homeDir = os.getcwd()
        repos = ["https://github.com/fleetcaptain/Turbolist3r"]
        os.mkdir("githubRepos")
        os.chdir(f"{homeDir}/githubRepos")
        for i in repos:
            system(f"git clone {i}")
        os.chdir(homeDir)
    except KeyboardInterrupt:
        system("rm -r githubRepos")
        print(f"{Fore.RED}{Style.BRIGHT} ★ Ctrl+C Detected - Aborting Setup ★{Style.NORMAL}{Fore.RESET}")