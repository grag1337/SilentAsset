import os
import requests
import threading
import json
import lib.runScan as runScan
from colorama import Fore,Back,Style
from os import system, name
from requests.exceptions import ConnectionError
from lxml.html import fromstring


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

def initializeReq(domain):
    global reqDir
    global doDir
    global homeDir
    global domain2
    domain2 = domain
    clear()
    print(f"{Fore.RED}{banner}{Fore.RESET}")
    print(f"{Fore.RED}{Style.BRIGHT}\n♦ Checking for responses ♦\n{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.RED}{Style.BRIGHT}\n♦ Don't worry if it seems frozen. ♦\n{Fore.RESET}{Style.NORMAL}")
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
    for line in suDo:
        t = threading.Thread(target=scanURL,args=(homeDir,domain,line,reqFile,reqDir,doDir)) 
        t.start() 
    t.join()
    
def scanURL(homeDir,domain,line,reqFile,reqDir,doDir):
    try:
        url = f"https://{line}"
        headers = requests.utils.default_headers()
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        reqOut = requests.get(url.replace("\n",""), headers=headers)
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
        jsonStr = {"url" : line2, "sCode" : sCode, "header" : pTitle}
    except ConnectionError as e:
        line2 = line.replace('\n',"")
        jsonStr = {"url" : line2, "sCode" : "No Response"}
    # Gonna do something different here, don't worry about it for the time being.
    #jsonLoc = open(reqFile, "a")
    #jsonLoc.write(str(jsonStr))
    #jsonLoc.close()
    reqLoc = open(f"{reqDir}{line2}.txt","w")
    try:
        reqLoc.write(fData)
        reqLoc.close()
    except UnboundLocalError:
        reqLoc.close()
        system(f"rm {reqDir}{line2}.txt")    


def beforeReport(reqDir,homeDir,domain,doDir):
    global aSubDom
    aSubDom = 0
    if runScan.dScan == "y" or runScan.dScan == "Y" or runScan.dScan == "yes" or runScan.dScan == "Yes":
        subFile = f"{domain}_full.txt"
    else:
        subFile = f"{domain}2.txt"
    oSubFile = open(f"{doDir}{subFile}","r")
    repDir = f"{doDir}requests"
    for line in os.listdir(repDir):
        if line == "requests.json":
            None
        else:
            file = open(f"{doDir}requests/{line}")
            contents = file.read()
            if contents.__contains__("200") or contents.__contains__("401") or contents.__contains__("404") or contents.__contains__("403"):
                aSubDom += 1
    global tSubDom
    tSubDom = 0
    for i in oSubFile:
        tSubDom += 1
    template = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>SilentAsset Report</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
        <!-- Custom styles for this template -->
        <link href="sticky-footer.css" rel="stylesheet">
      </head>

      <body>

        <!-- Begin page content -->
        <main role="main" class="container">
          <h1 class="mt-5">SilentAsset Report</h1>
          <p class="lead">Template for SilentAsset. Scanned: {domain2}</p>
          </main>

        <footer class="footer">
          <div class="container">
            <span class="text-muted">Domains Scanned: {tSubDom} Domains Active: {aSubDom}</span>
          </div>
        </footer>
      </body>
    </html>
    """
    templateLoc = open(f"{doDir}/report.html","w")
    templateLoc.write(template)
    templateLoc.close()


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
            print(f"{Fore.RED} ★ [{scHots}\{totSubs}] Hosts Scanned{Fore.RESET}")
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