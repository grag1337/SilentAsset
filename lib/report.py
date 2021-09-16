from os import stat, system, name
from colorama import Fore,Back,Style
from lib.runScan import *
import lib.runScan as runScan
import json

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

def beforeReport(reqDir,homeDir,domain,doDir,reqLoc):
    global aSubDom
    global domain2
    domain2 = domain
    aSubDom = 0
    activeDomains = []
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
            urlName = str(line).replace(".txt","")
            activeDomains.append(urlName)
            aSubDom += 1
    tSubDom = 0
    for i in oSubFile:
        tSubDom += 1
    os.mkdir(f"{doDir}report/")
    doReport(reqLoc,doDir)
    template = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>SilentAsset Report</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
      </head>

      <body>

        <main role="main" class="container">
          <h1 class="mt-5">SilentAsset Report</h1>
          <p class="lead">Template for SilentAsset. Scanned: {domain2}</p>
          </main>

        <footer class="footer">
          <div class="container">
            <span class="text-muted">Domains Scanned: {tSubDom} </span>
            <span class="text-muted">Domains Active: {aSubDom}</span>
            <li>
            {sCodeLiMark}
            </li>
          </div>
        </footer>
      </body>
    </html>
    """
    templateLoc = open(f"{doDir}/report/report.html","w")
    templateLoc.write(template)
    templateLoc.close()
    print(f"{Fore.LIGHTRED_EX}♦ Report saved to {doDir}report/report.html ♦{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}♦ Press ENTER to continue... ♦{Fore.RESET}")
    input()
    

def doReport(reqLoc,doDir):
  global sCodeLiMark
  jsonInit = open(reqLoc,'r')
  jsonData = json.loads(jsonInit.read())
  jsonInit.close()
  sCodes = []
  sCodeIt = []
  sCodeLiMark = '<span class="text-muted">Status Codes:</span><br><br>'
  for d in jsonData:
    statusCode = d["sCode"]  
    sCodes.append(statusCode)
    if statusCode not in sCodeIt:
      sCodeIt.append(statusCode)
  for i in sCodeIt:
    os.mkdir(f"{doDir}report/{i}")
    count = sCodes.count(i)
    uSCodes = f'<br><span class="text-muted">Here are the results for: <b>{i}</b></span><br>'
    for d in jsonData:
      statusCode = d["sCode"]
      if statusCode == i:
        uSCodes += f'<br><a href="https://{d["url"]}" class="text-muted">{d["url"]}</a>'
    sCodeTemplate = f"""
      <!doctype html>
      <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
          <title>SilentAsset Report</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
        </head>

        <body>

          <main role="main" class="container">
            <h1 class="mt-5">SilentAsset Report</h1>
            <p class="lead">Status Code List for {i}</p>
            <a href="{doDir}report/report.html" class="text-muted">Back</a>
            </main>

          <footer class="footer">
            <div class="container">
              {uSCodes}
            </div>
          </footer>
        </body>
      </html>
    """
    codeReport = open(f"{doDir}report/{i}/{i}.html","w")
    codeReport.write(sCodeTemplate)
    codeReport.close()
    sCodeLiMark += f'<a href="{i}/{i}.html" class="text-muted">{i}: {count}</a><br>'
