import os
import asyncio
import requests
import threading
from multiprocessing import Process
from pyppeteer import launch
from selenium import webdriver
from lxml.html import fromstring
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
            initScreenshot(scanOpt,domain,homeDir)
        else:
            os.chdir(f"{homeDir}/output/{domain}")
            initScreenshot(scanOpt,domain,homeDir)

    def initScreenshot(scanOpt,domain,homeDir):
        if scanOpt == 1:
            workingDir = os.getcwd()
            subFile = f"{workingDir}/{domain}_full.txt"
            oSubFile = open(subFile,"r")
            totSubs = 0
            for i in oSubFile:
                totSubs += 1
            oSubFile.close()
        else:
            workingDir = os.getcwd()
            subFile = f"{workingDir}/{domain}2.txt"
            oSubFile = open(subFile,"r")
            totSubs = 0
            for i in oSubFile:
                totSubs += 1
            oSubFile.close()
        try:
            os.mkdir("images/")
        except:
            None
        try:
            os.mkdir("requests/")
        except:
            None
        oSubFile = open(subFile,"r")
        global scHots
        scHots = 0
        for line in oSubFile:
            print(f"{Fore.RED} ★ [{scHots}\{totSubs}] Hosts Scanned{Fore.RESET}")
            asyncio.get_event_loop().run_until_complete(screenshot(line,homeDir,domain))
            scHots += 1
            
    async def screenshot(line,homeDir,domain):
        print("ASDASDASD")
        browser = await launch(headless=True)
        page = await browser.newPage()
        url = f"https://{line}"
        reqOut = requests.get(url.replace("\n",""))
        sCode = str(reqOut).replace("<Response [","").replace("]>","")
        pTitle = fromstring(reqOut.content)
        pTitle = pTitle.findtext('.//title')
        fData = f"{sCode} ! {str(pTitle)}"
        line2 = line.replace('\n',"")
        reqLoc = open(f"{homeDir}/output/{domain}/requests/{line2}.txt","w")
        reqLoc.write(fData)
        reqLoc.close()
        await page.goto(str(url))
        await page.screenshot({'path': f'images/{line}.png', 'fullPage': True})
        await browser.close()

except KeyboardInterrupt:
    print(f"{Fore.RED}{Style.BRIGHT}\n\n ★ Ctrl+C Detected, exiting cleanly... ★{Style.NORMAL}{Fore.RESET}")