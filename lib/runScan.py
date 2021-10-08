from io import UnsupportedOperation
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

    def initializeScan():
        global tSubDom
        global dScan
        dScan = 0
        global domain
        global tOut
        global backVar
        global twoSCode
        global threeSCode
        global fourSCode
        global fiveSCode
        global sSubDom
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
            None
        print(f"{Fore.LIGHTRED_EX}✓ Chosen Thread Count →{Style.BRIGHT} {threads} {Style.NORMAL}{Fore.RESET}")
        dScan = input(f"\n{Fore.LIGHTRED_EX}*Deep Scan? - Default n (y/n) (e.g ► y) ►{Fore.CYAN} ")
        if dScan == "back" or dScan == "Back":
            backVar += 1
            return
        if dScan == "y" or dScan == "Y" or dScan == "yes" or dScan == "Yes":
            dScan = "y"
        else:
            dScan = "n"
        print(f"{Fore.LIGHTRED_EX}✓ Deep Scan →{Style.BRIGHT} {dScan} {Style.NORMAL}{Fore.RESET}")
        try:
            tOut = int(input(f"\n{Fore.LIGHTRED_EX}Request Timeout - Recommended 15 (e.g ► 5) ►{Fore.CYAN} "))
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
        sSubDom = input(f"\n{Fore.LIGHTRED_EX}*Would you like to screenshot active subdomains? - Default n (y/n) (e.g ► y) ►{Fore.CYAN} ")
        if sSubDom == "back" or sSubDom == "Back":
            backVar += 1
            return
        if sSubDom == "y" or sSubDom == "Y" or sSubDom == "yes" or sSubDom == "Yes":
            sSubDom = "y"
        else:
            sSubDom = "n"
        if sSubDom == "y":
            print(f"{Fore.LIGHTRED_EX}Please select which status codes you would like to screenshot: ")
            twoSCode = input(f"{Fore.LIGHTRED_EX}→ 2XX (y/n) (e.g ► y) ►{Fore.CYAN} ")
            if twoSCode == "y" or twoSCode == "Y" or twoSCode == "yes" or twoSCode == "Yes":
                twoSCode = "y"
            else:
                twoSCode = "n"
            print(f"{Fore.LIGHTRED_EX}✓ Option Chosen →{Style.BRIGHT} {twoSCode} {Style.NORMAL}{Fore.RESET}")
            threeSCode = input(f"{Fore.LIGHTRED_EX}→ 3XX (y/n) (e.g ► y) ►{Fore.CYAN} ")
            if threeSCode == "y" or threeSCode == "Y" or threeSCode == "yes" or threeSCode == "Yes":
                threeSCode = "y"
            else:
                threeSCode = "n"
            print(f"{Fore.LIGHTRED_EX}✓ Option Chosen →{Style.BRIGHT} {threeSCode} {Style.NORMAL}{Fore.RESET}")
            fourSCode = input(f"{Fore.LIGHTRED_EX}→ 4XX (y/n) (e.g ► y) ►{Fore.CYAN} ")
            if fourSCode == "y" or fourSCode == "Y" or fourSCode == "yes" or fourSCode == "Yes":
                fourSCode = "y"
            else:
                fourSCode = "n"
            print(f"{Fore.LIGHTRED_EX}✓ Option Chosen →{Style.BRIGHT} {fourSCode} {Style.NORMAL}{Fore.RESET}")
            fiveSCode = input(f"{Fore.LIGHTRED_EX}→ 5XX (y/n) (e.g ► y) ►{Fore.CYAN} ")
            if fiveSCode == "y" or fiveSCode == "Y" or fiveSCode == "yes" or fiveSCode == "Yes":
                fiveSCode = "y"
            else:
                fiveSCode = "n"                            
            print(f"{Fore.LIGHTRED_EX}✓ Option Chosen →{Style.BRIGHT} {fiveSCode} {Style.NORMAL}{Fore.RESET}")
        else:
            None
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
                line2 = line.replace("www.","")
                subdomainOutput.write(line2)
        subdomainOutput.close()
        
        print(f"\n{Fore.LIGHTRED_EX}♦ Subdomain Scan 1 Completed ♦{Fore.RESET}")
        scanOpt = 0
        lResults.close()
        system(f"rm {homeDir}/output/{domain}/{domain}.txt")
        if dScan == 'y' or dScan == 'Y' or dScan == 'yes' or dScan == 'Yes':
            #try:
            subdomainOutput = open(f"{homeDir}/output/{domain}/{domain}2.txt",'r')
            subby = []
            for i in subdomainOutput:
                subby.append(i)
            subdomainOutput.close()
            subdomainOutput = open(f"{homeDir}/output/{domain}/{domain}2.txt",'a')
            scanOpt += 1
            print(f"\n{Fore.LIGHTRED_EX}♦ Subdomain Scan 2 Initiated ♦{Fore.RESET}")
            print(f"\n{Fore.LIGHTRED_EX}♦ Don't worry if it looks stuck, it's doing its job. ♦{Fore.RESET}")
            os.chdir(f"{homeDir}/output/{domain}/")
            system(f"/{homeDir}/githubRepos/findomain-linux -t {domain} -q > {domain}3.txt")
            system(f"/{homeDir}/githubRepos/gobuster dns -d {domain} -w {homeDir}/wordlists/subdomains.txt -q -t {threads} -z > {domain}4_temp.txt")
            tempWrite = open(f"{domain}3.txt","a+")
            tempRead = open(f"{domain}4_temp.txt","r")
            for i in tempRead:
                i2 = i.replace("Found: ","")
                if i2 in tempWrite:
                    None
                else:
                    tempWrite.write(i2)
            tempRead.close()
            tempWrite.close()
            system(f"rm {domain}4_temp.txt")
            print(f"\n{Fore.LIGHTRED_EX}♦ Subdomain Scan 2 Completed ♦{Fore.RESET}")
            permSub = open(f"{domain}3.txt","r")
            for i in permSub:
                if i in subby:
                    None
                else:
                    subdomainOutput.write(i)
            subdomainOutput.close()
            permSub.close()
            os.chdir(homeDir)
            """
            except:
                print(f"{Fore.RED}{Style.BRIGHT}♦ An error during the second subdomain scan has occured...\n Defaulting to Scan 1's subdomain list... ♦{Style.NORMAL}{Fore.RESET}")
                print(f"{Fore.RED}♦ ENTER to continue... ♦ {Fore.RESET}")
                input()
                scanOpt = 0
                return
            """
        else:
            None
        os.chdir(homeDir)


except KeyboardInterrupt:
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n\n ★ Ctrl+C Detected, exiting cleanly... ★{Style.NORMAL}{Fore.RESET}")