import os
import requests
import threading
#import json
import socket
import lib.runScan as runScan
from time import sleep
from colorama import Fore,Back,Style
from os import system, name
from requests.exceptions import ConnectionError, ReadTimeout
from lxml.html import fromstring



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

def initializeReq(domain,tOut):
    global reqDir
    global doDir
    global homeDir
    global domain2
    global reqFile
    urlList = []
    sCodeList = []
    pTitleList = []
    domain2 = domain
    clear()
    print(f"{Fore.LIGHTRED_EX}{banner}{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Checking for responses ♦\n{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Don't worry if it seems frozen. Requests have a {tOut} second timeout. ♦\n{Fore.RESET}{Style.NORMAL}")
    if runScan.dScan == "y" or runScan.dScan == "Y" or runScan.dScan == "yes" or runScan.dScan == "Yes":
        subFile = f"{domain}_full.txt"
    else:
        subFile = f"{domain}2.txt"
    homeDir = os.getcwd()
    doDir = f"{homeDir}/output/{domain}/"
    reqDir = f"{homeDir}/output/{domain}/requests/"
    reqFile = f"{homeDir}/output/{domain}/requests/requests.json"
    suDo = open(f"{doDir}{subFile}","r")
    try:
        if os.path.isdir(reqFile) == False:
            os.mkdir(f"{doDir}requests")
        else:
            None
    except FileExistsError:
        None
    threads = []
    for line in suDo:
        #scanURL(homeDir,domain,line,reqFile,reqDir,doDir)
        t = threading.Thread(target=scanURL,args=(homeDir,domain,line,reqFile,reqDir,doDir,tOut,urlList,sCodeList,pTitleList)) 
        threads.append(t)
    for x in threads:        
        x.start()
    for x in threads:
        x.join()
    airgap1 = " "
    airgap2 = "     "
    jsonLoc = open(reqFile, "a")
    jsonLoc.write(f'{{\n{airgap1}"urls": \n{airgap1}{{\n')
    jsonLoc.write(f'\n{airgap2}"{urlList[0]}":"{sCodeList[0]}"')
    for i in urlList[1:]:
        try:
            sCodeLoc = urlList.index(i)
            jsonLoc.write(f',\n{airgap2}"{i}":"{sCodeList[sCodeLoc]}"')
        except IndexError:
            None
    jsonLoc.write(f'{airgap1}}},\n')
    jsonLoc.write(f'{airgap1}"headers": \n{airgap1}{{\n')
    pTitleForm = pTitleList[0]
    pTitleForm = pTitleForm.strip().replace("\n","")
    jsonLoc.write(f'\n{airgap2}"{urlList[0]}":"{pTitleForm}"')
    for i in urlList[1:]:
        try:
            pTitleLoc = urlList.index(i)
            try:
                pTitleForm = pTitleList[pTitleLoc]
                pTitleForm = pTitleForm.strip().replace("\n","")
            except AttributeError:
                pTitleForm = ""
                None
            jsonLoc.write(f',\n{airgap2}"{i}":"{pTitleForm}"')
        except IndexError:
            None
    jsonLoc.write(f"\n{airgap2}}}\n{airgap1}}}")


def scanURL(homeDir,domain,line,reqFile,reqDir,doDir,tOut,urlList,sCodeList,pTitleList):
    try:
        url = f"https://{line}"
        headers = requests.utils.default_headers()
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        reqOut = requests.get(url.replace("\n",""), headers=headers,timeout=int(tOut))
        sCode = str(reqOut).replace("<Response [","").replace("]>","")
        try:
            pTitle = fromstring(reqOut.content)
        except:
            pTitle = ""
            None
        if pTitle == "":
            None
        else:
            pTitle = pTitle.findtext('.//title')
        fData = f"{sCode} ! {str(pTitle)}"
        line2 = line.replace('\n',"")
        urlList.append(line2)
        sCodeList.append(sCode)
        pTitleList.append(pTitle)
    except TimeoutError:
        line2 = line.replace('\n',"")
        urlList.append(line2)
        sCodeList.append(sCode)
    except ReadTimeout:
        try:
            line2 = line.replace('\n',"")
            urlList.append(line2)
            sCodeList.append(sCode)
        except UnboundLocalError:
            None
    except ConnectionError as e:
        line2 = line.replace('\n',"")
    reqLoc = open(f"{reqDir}{line2}.txt","w")
    try:
        reqLoc.write(fData)
        reqLoc.close()
    except UnboundLocalError:
        reqLoc.close()
        system(f"rm {reqDir}{line2}.txt")    

"""
Screenshot Function (:
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
            print(f"{Fore.LIGHTRED_EX} ★ [{scHots}\{totSubs}] Hosts Scanned{Fore.RESET}")
            asyncio.get_event_loop().run_until_complete(screenshot(line,homeDir,domain))
            scHots += 1
            
    async def screenshot(line,homeDir,domain):
        print("ASDASDASD")
        browser = await launch(headless=True)
        page = await browser.newPage()
        url = f"https://{line}"
        await page.goto(str(url))
        await page.screenshot({'path': f'images/{line}.png', 'fullPage': True})
        await browser.close()
"""