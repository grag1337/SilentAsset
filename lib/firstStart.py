import os
from os import system, name
from colorama import Fore, Back, Style
import subprocess
BANNER = """
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

def checkFor():
    global choiceVar
    choiceVar = 0
    try:
        checkF = open("/usr/bin/p7zip","r")
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}\n♦ P7ZIP NOT FOUND! ♦{Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}\n♦ Please install p7zip before you run this program again. ♦{Fore.RESET}")
        input()
        choiceVar += 1
        return
    if os.path.isdir(os.getcwd()+"/githubRepos") == False:
        print(f"{Fore.LIGHTRED_EX}{BANNER}{Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}\n♦ Thanks for using Silent Asset for the first time! ♦\n ♦ We're going to have to do some setup before you begin ♦\n ♦ Would you like to do this now? ♦\n{Fore.RESET}")
        choice = input(f"{Fore.LIGHTRED_EX} (Y/n) ►{Fore.CYAN} ")
        if choice == "n" or choice == "N" or choice == "No" or choice == "no" :
            choiceVar += 1
        else:
            setup()
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

        system("wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux && chmod +x findomain-linux")
        system("wget https://github.com/OJ/gobuster/releases/latest/download/gobuster-linux-amd64.7z")
        system("p7zip -d gobuster-linux-amd64.7z")
        system("chmod +x gobuster-linux-amd64/gobuster && mv gobuster-linux-amd64/gobuster .")
        system("rm -r gobuster-linux-amd64 -f")
        os.chdir(homeDir)

    except KeyboardInterrupt:
        system("rm -r githubRepos")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT} ★ Ctrl+C Detected - Aborting Setup ★{Style.NORMAL}{Fore.RESET}")