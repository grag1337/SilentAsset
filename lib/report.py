from os import system, name
from colorama import Fore,Back,Style
from lib.runScan import *
import lib.runScan as runScan

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

def beforeReport(reqDir,homeDir,domain,doDir):
    global aSubDom
    global domain2
    domain2 = domain
    aSubDom = 0
    if runScan.dScan == "y" or runScan.dScan == "Y" or runScan.dScan == "yes" or runScan.dScan == "Yes":
        subFile = f"{domain}_full.txt"
    else:
        subFile = f"{domain}2.txt"
    oSubFile = open(f"{doDir}{subFile}","r")
    repDir = f"{doDir}requests"
    for line in os.listdir(repDir):
        file = open(f"{doDir}requests/{line}")
        contents = file.read()
        if contents.__contains__("200") or contents.__contains__("401") or contents.__contains__("404") or contents.__contains__("403"):
            aSubDom += 1
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
            <span class="text-muted">Domains Scanned: {tSubDom} </span>
            <span class="text-muted">Domains Active: {aSubDom}</span>
          </div>
        </footer>
      </body>
    </html>
    """
    templateLoc = open(f"{doDir}/report.html","w")
    templateLoc.write(template)
    templateLoc.close()
    print(f"{Fore.LIGHTRED_EX}♦ Report saved to {doDir}report.html ♦{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}♦ Press ENTER to continue... ♦{Fore.RESET}")
    input()