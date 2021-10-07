from os import system, name
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

def beforeReport(reqDir,homeDir,domain,doDir,reqLoc,sHotValue,twoSCode,threeSCode,fourSCode,fiveSCode):
    global aSubDom
    global domain2
    domain2 = domain
    aSubDom = 0
    subFile = f"{domain}2.txt"
    oSubFile = open(f"{doDir}{subFile}","r")
    repDir = f"{doDir}requests"
    for line in os.listdir(repDir):
        file = open(f"{doDir}requests/{line}")
        contents = file.read()
    tSubDom = 0
    for i in oSubFile:
        tSubDom += 1
    try:
      os.mkdir(f"{doDir}report/")
    except:
      None
    doReport(reqLoc,doDir,sHotValue,twoSCode,threeSCode,fourSCode,fiveSCode)
    jsonInit = open(reqLoc,'r')
    jsonData = json.loads(jsonInit.read())
    jsonInit.close()  
    for d in jsonData:
      aSubDom += 1
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
    
def doReport(reqLoc,doDir,sHotValue,twoSCode,threeSCode,fourSCode,fiveSCode):
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
    try:
      os.mkdir(f"{doDir}report/{i}")
    except:
      None
    count = sCodes.count(i)
    uSCodes = f'<br><span class="text-muted">Here are the results for: <b>{i}</b></span><br>'
    for d in jsonData:
      statusCode = d["sCode"]
      if statusCode == i:
        if sHotValue == "y":
          if statusCode == "200":
            if twoSCode == "y":
              uSCodes += f'<br><a href="https://{d["url"]}" class="text-muted">{d["url"]} - {d["header"]}</a><br><a target="_blank" href="{d["url"]}.png"><img src="{d["url"]}.png"></a>'
          elif statusCode == "300":
            if threeSCode == "y":
              uSCodes += f'<br><a href="https://{d["url"]}" class="text-muted">{d["url"]} - {d["header"]}</a><br><a target="_blank" href="{d["url"]}.png"><img src="{d["url"]}.png"></a>'
          elif statusCode == "400":
            if fourSCode == "y":
              uSCodes += f'<br><a href="https://{d["url"]}" class="text-muted">{d["url"]} - {d["header"]}</a><br><a target="_blank" href="{d["url"]}.png"><img src="{d["url"]}.png"></a>'
          elif statusCode == "500":
            if fiveSCode == "y":
              uSCodes += f'<br><a href="https://{d["url"]}" class="text-muted">{d["url"]} - {d["header"]}</a><br><a target="_blank" href="{d["url"]}.png"><img src="{d["url"]}.png"></a>'
        else:
          uSCodes += f'<br><a href="https://{d["url"]}" class="text-muted">{d["url"]} - {d["header"]}</a>'
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
          <style>
          img {{
            border: 1px solid #ddd; 
            border-radius: 4px; 
            padding: 5px; 
            width: 150px; 
          }}

          
          img:hover {{
            box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
          }}
          </style>
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
    sCodeLiMark += f'<a href="{i}/{i}.html" class="text-muted">➳ {i}: {count}</a><br>'
