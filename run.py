#!/usr/bin/python3
# Using Witnessme, AltDNS, Turbolist3r
# You're gonna get jumped with the 100mb chromium install.
from os import system, name
from lib.firstStart import * 
from lib.runScan import *
import lib.firstStart as firstStart
from colorama import Fore,Back,Style

#Clear Function; in literally all of my python programs. Stay clean kids.
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


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


♦ An asset discovery suite for the masses ♦

♦ Written by yours truly ♦

♦ Feel free to report any issues, suggestions, spelling mistakes, push / pull requests ♦
"""
try:
    clear()
    def inputloop(lastCommand):
        checkFor()
        if firstStart.choiceVar == 1:
            print(f"{Fore.RED}\n ♦ Ok! Exiting now... ♦{Fore.RESET}")
            quit()
        else:
            None
        print(f"{Fore.RED}{banner}{Fore.RESET}")
        print(f"{Fore.RED}{Style.BRIGHT}♦ To get started type {Back.RED}{Fore.WHITE}help{Fore.RED}{Back.RESET} ♦ {Style.NORMAL}{Fore.RESET}")
        getStarted = input(f"\n{Fore.RED}{lastCommand} ►{Fore.CYAN} ")
        if getStarted == "help" or getStarted == "Help" or getStarted == "h" or getStarted == "H":
            print(f"{Fore.YELLOW}\n ♦ Thank you for using Silent Asset! ♦\n\n ♦ These are the current commands: ♦\n ♦ help - show help ♦\n ♦ about - learn about the program and its functionality ♦\n ♦ quit - quit the program ♦\n ♦ scan - initiate scan ♦\n ♦ Press ANY KEY to continue ♦\n {Fore.RESET}")
            input()
            inputloop(f"✓ {getStarted}")
        elif getStarted == "quit" or getStarted == "Quit" or getStarted == "Exit" or getStarted == "exit":
            quit()
        elif getStarted.__contains__("scan") or getStarted.__contains__("Scan"):
            initializeScan()
            inputloop(f"✓ {getStarted}")
        elif getStarted == "about" or getStarted == "About":
            inputloop(f"✓ {getStarted}")
        else:
            inputloop(f"✕ {getStarted}")

    inputloop("")
except KeyboardInterrupt:
    print(f"{Fore.RED}{Style.BRIGHT}\n\n ★ Ctrl+C Detected, exiting cleanly... ★{Style.NORMAL}{Fore.RESET}")