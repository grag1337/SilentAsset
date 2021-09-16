import os
import asyncio
import requests
import threading
from multiprocessing import Process, Value
from pyppeteer import launch
from selenium import webdriver
from os import system,name
from colorama import Fore,Back,Style
try:
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

    def initializeScan():
        global tSubDom
        global dScan
        global domain
        global tOut
        global backVar
        backVar = 0
        clear()
        print(f"{Fore.LIGHTRED_EX}{banner}{Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ The time has come to scan! ♦\n{Fore.RESET}{Style.NORMAL}")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ This process is currently completely automated ♦\n♦ Feel free to suggest changes that warrant more user input. ♦\n{Fore.RESET}{Style.NORMAL}")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Inputs marked with asterisks are optional. ♦\n{Fore.RESET}{Style.NORMAL}")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Type {Back.RED}{Fore.WHITE}back{Back.RESET}{Fore.LIGHTRED_EX} to return ♦\n{Fore.RESET}{Style.NORMAL}\n")
        domain = input(f"\n{Fore.LIGHTRED_EX}Domain (e.g ► tesla.com) ►{Fore.CYAN} ")
        if domain == "back" or domain == "Back":
            backVar += 1
            return
        print(f"{Fore.LIGHTRED_EX}✓ Chosen Domain →{Style.BRIGHT} {domain} {Style.NORMAL}{Fore.RESET}")
        threads = input(f"\n{Fore.LIGHTRED_EX}*Threads - Default 20 (e.g ► 20) ►{Fore.CYAN} ")
        if threads == "":
            threads = 20
        elif threads == "back" or threads == "Back":
            backVar += 1
            return
        else:
            backVar += 1
            None
        print(f"{Fore.LIGHTRED_EX}✓ Chosen Thread Count →{Style.BRIGHT} {threads} {Style.NORMAL}{Fore.RESET}")
        dScan = input(f"\n{Fore.LIGHTRED_EX}*Deep Scan? - Default n (y/n) (e.g ► y) ►{Fore.CYAN} ")
        if dScan == "" or dScan != "y" or dScan != "Y" or dScan != "yes" or dScan != "Yes":
            dScan = "n"
        elif dScan == "back" or dScan == "Back":
            backVar += 1
            return
        else:
            None    
        print(f"{Fore.LIGHTRED_EX}✓ Deep Scan →{Style.BRIGHT} {dScan} {Style.NORMAL}{Fore.RESET}")
        try:
            tOut = int(input(f"\n{Fore.LIGHTRED_EX}Request Timeout - Recommended 10 (e.g ► 5) ►{Fore.CYAN} "))
            if tOut == "":
                tOut = 10
            elif tOut == "back" or tOut == "Back":
                backVar += 1
                return
            else:
                None    
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ ERROR: Must be an integer ♦\n{Fore.RESET}{Style.NORMAL}")
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Press ENTER to return back to menu... ♦\n{Fore.RESET}{Style.NORMAL}")
            backVar += 1
            input()
            return

        print(f"{Fore.LIGHTRED_EX}✓ Timeout Chosen →{Style.BRIGHT} {tOut} {Style.NORMAL}{Fore.RESET}")
        print(f"\n\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Press ENTER to begin.{Style.NORMAL}{Fore.RESET}")
        input()
        subScan(domain,threads,dScan)

    def subScan(domain,threads,dScan):
        print(f"\n{Fore.LIGHTRED_EX}♦ Subdomain Scan 1 Initiated ♦{Fore.RESET}")
        homeDir = os.getcwd()
        try:
            os.mkdir("output")
        except FileExistsError:
            None
        try:
            os.mkdir(f"{homeDir}/output/{domain}")
        except FileExistsError:
            None
        os.chdir(homeDir + "/githubRepos/Turbolist3r/")
        system(f"python3 turbolist3r.py -d {domain} -o {homeDir}/output/{domain}/{domain}.txt -q > /dev/null")
        lResults = open(f"{homeDir}/output/{domain}/{domain}.txt",'r')
        subdomainOutput = open(f"{homeDir}/output/{domain}/{domain}2.txt",'w')
        for line in lResults:
            if line.__contains__(".com") == False or line.__contains__("Enumerating") or line.__contains__("Forked"):
                None
            else:
                subdomainOutput.write(line)
        print(f"\n{Fore.LIGHTRED_EX}♦ Subdomain Scan 1 Completed ♦{Fore.RESET}")
        scanOpt = 0
        lResults.close()
        subdomainOutput.close()
        system(f"rm {homeDir}/output/{domain}/{domain}.txt")
        if dScan == 'y' or dScan == 'Y' or dScan == 'yes' or dScan == 'Yes':
            scanOpt += 1
            print(f"\n{Fore.LIGHTRED_EX}♦ Subdomain Scan 2 Initiated ♦{Fore.RESET}")
            print(f"\n{Fore.LIGHTRED_EX}♦ Don't worry if it looks stuck, it's doing its job. ♦{Fore.RESET}")
            os.chdir(f"{homeDir}/output/{domain}/")
            system(f"altdns -i {domain}2.txt -o {domain}_permutations -w {homeDir}/wordlists/subdomains.txt -r -t {threads} -s {domain}_full.txt")
            print(f"\n{Fore.LIGHTRED_EX}♦ Subdomain Scan 2 Completed ♦{Fore.RESET}")
        else:
            None
        os.chdir(homeDir)


except KeyboardInterrupt:
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n\n ★ Ctrl+C Detected, exiting cleanly... ★{Style.NORMAL}{Fore.RESET}")