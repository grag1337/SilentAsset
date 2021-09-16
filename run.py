#!/usr/bin/python3
# Using AltDNS, Turbolist3r
# You're gonna get jumped with the 100mb chromium install.
from os import system, name

from lxml.html import InputElement
from lib.firstStart import * 
from lib.runScan import *
from lib.getResponse import *
from lib.report import *
from lib.jsonParse import *
from colorama import Fore,Back,Style
import lib.runScan as runScan
import lib.firstStart as firstStart 
import lib.getResponse as getResponse

#Clear Function; in literally all of my python programs. Stay clean kids.
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


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


♦ An asset discovery suite for the masses ♦

♦ Written by yours truly ♦

♦ Feel free to report any issues, suggestions, spelling mistakes, push / pull requests ♦
"""
try:
    clear()
    def inputloop(lastCommand):
        checkFor()
        if firstStart.choiceVar == 1:
            print(f"{Fore.LIGHTRED_EX}\n ♦ Ok! Exiting now... ♦{Fore.RESET}")
            quit()
        else:
            None
        print(f"{Fore.LIGHTRED_EX}{banner}{Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}♦ To get started type {Back.RED}{Fore.WHITE}help{Fore.LIGHTRED_EX}{Back.RESET} ♦ {Style.NORMAL}{Fore.RESET}")
        getStarted = input(f"\n{Fore.LIGHTRED_EX}{lastCommand} ►{Fore.CYAN} ")
        if getStarted == "help" or getStarted == "Help" or getStarted == "h" or getStarted == "H":
            print(f"{Fore.LIGHTYELLOW_EX}\n ♦ Thank you for using Silent Asset! ♦\n\n ♦ These are the current commands: ♦\n ♦ help - show help ♦\n ♦ about - learn about the program and its functionality ♦\n ♦ quit - quit the program ♦\n ♦ scan - initiate scan ♦\n ♦ Press ANY KEY to continue ♦\n {Fore.RESET}")
            input()
            clear()
            inputloop(f"✓ {getStarted}")
        elif getStarted == "quit" or getStarted == "Quit" or getStarted == "Exit" or getStarted == "exit":
            exit()
        elif getStarted.__contains__("scan") or getStarted.__contains__("Scan"):
            runScan.backVar = 0
            initializeScan()
            if runScan.backVar >= 1:
                clear()
                inputloop(f"✓ {getStarted}")
            else:
                initializeReq(runScan.domain,runScan.tOut)
                beforeReport(getResponse.reqDir,getResponse.homeDir,runScan.domain,getResponse.doDir,getResponse.reqFile)
                clear()
                inputloop(f"✓ {getStarted}")
        elif getStarted == "about" or getStarted == "About":
            print("\n\n\n")
            print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT} ◊ ABOUT ◊ \n{Fore.RESET}{Style.NORMAL}")
            print(f"{Fore.LIGHTYELLOW_EX}→ After trying to make-do with a handful of asset discovery tools,\nI decided that it was time to just create something that does what I want, how I want it.\nThis is an ongoing project and features are prone to change / deletion.\nI'm taking any/all suggestions and code additions that assist in creating a tool that can compete with it's pLIGHTRED_EXecessors.\n\n\n\n ♦ ENTER TO RETURN ♦ \n\n\n{Fore.RESET}")
            input()
            clear()
            inputloop(f"✓ {getStarted}")
        else:
            clear()
            inputloop(f"✕ {getStarted}")

    inputloop("")
except KeyboardInterrupt:
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n\n ★ Ctrl+C Detected, exiting cleanly... ★{Style.NORMAL}{Fore.RESET}")