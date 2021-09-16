import os
import asyncio
import requests
import threading
from multiprocessing import Process
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
        clear()
        print(f"{Fore.RED}{banner}{Fore.RESET}")
        print(f"{Fore.RED}{Style.BRIGHT}\n♦ The time has come to scan! ♦\n{Fore.RESET}{Style.NORMAL}")
        print(f"{Fore.RED}{Style.BRIGHT}\n♦ This process is currently completely automated ♦\n♦ Feel free to suggest changes that warrant more user input. ♦\n{Fore.RESET}{Style.NORMAL}")
        domain = input(f"\n{Fore.RED}Domain (e.g ► tesla.com) ►{Fore.CYAN} ")
        print(f"{Fore.RED}✓ Chosen Domain →{Style.BRIGHT} {domain} {Style.NORMAL}{Fore.RESET}")
        threads = input(f"\n{Fore.RED}Threads - Default 20 (e.g ► 20) ►{Fore.CYAN} ")
        if threads == "":
            threads = 20
        else:
            None
        print(f"{Fore.RED}✓ Chosen Thread Count →{Style.BRIGHT} {threads} {Style.NORMAL}{Fore.RESET}")
        dScan = input(f"\n{Fore.RED}Deep Scan? - Default n (y/n) (e.g ► y) ►{Fore.CYAN} ")
        if dScan == "":
            dScan = "n"
        else:
            None    
        print(f"{Fore.RED}✓ Deep Scan →{Style.BRIGHT} {dScan} {Style.NORMAL}{Fore.RESET}")
        tOut = input(f"\n{Fore.RED}Request Timeout - Default 10 (e.g ► 5) ►{Fore.CYAN} ")
        if tOut != int or tOut == "":
            tOut = 10
        else:
            None    
        print(f"{Fore.RED}✓ Timeout Chosen →{Style.BRIGHT} {tOut} {Style.NORMAL}{Fore.RESET}")
        print(f"\n\n{Fore.RED}{Style.BRIGHT}Press ENTER to begin.{Style.NORMAL}{Fore.RESET}")
        input()
        subScan(domain,threads,dScan)

    def subScan(domain,threads,dScan):
        print(f"\n{Fore.RED}♦ Subdomain Scan 1 Initiated ♦{Fore.RESET}")
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
        print(f"\n{Fore.RED}♦ Subdomain Scan 1 Completed ♦{Fore.RESET}")
        scanOpt = 0
        lResults.close()
        subdomainOutput.close()
        system(f"rm {homeDir}/output/{domain}/{domain}.txt")
        if dScan == 'y' or dScan == 'Y' or dScan == 'yes' or dScan == 'Yes':
            scanOpt += 1
            print(f"\n{Fore.RED}♦ Subdomain Scan 2 Initiated ♦{Fore.RESET}")
            print(f"\n{Fore.RED}♦ Don't worry if it looks stuck, it's doing its job. ♦{Fore.RESET}")
            os.chdir(f"{homeDir}/output/{domain}/")
            system(f"altdns -i {domain}2.txt -o {domain}_permutations -w {homeDir}/wordlists/subdomains.txt -r -t {threads} -s {domain}_full.txt")
            print(f"\n{Fore.RED}♦ Subdomain Scan 2 Completed ♦{Fore.RESET}")
        else:
            None
        os.chdir(homeDir)


except KeyboardInterrupt:
    print(f"{Fore.RED}{Style.BRIGHT}\n\n ★ Ctrl+C Detected, exiting cleanly... ★{Style.NORMAL}{Fore.RESET}")