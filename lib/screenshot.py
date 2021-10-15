import os
from colorama import Fore,Back,Style
import asyncio
from pyppeteer import launch
import json
import time


def time_convert(sec):
  sec = sec % 60
  itTime = sec  
  benchmark.append(itTime)

def initScreenshot(resDir,domain,homeDir):        
    global benchmark
    benchmark = []
    jsonInit = open(resDir,'r')
    jsonData = json.loads(jsonInit.read())
    jsonInit.close()
    try:
        os.mkdir(f"{homeDir}/output/{domain}/report")
    except:
        None
    shit2scan = []
    for i in jsonData:
        statCode = i["sCode"]
        url = i["url"]
        shit2scan.append(f"{url} {statCode}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Benchmarking... ♦\n{Fore.RESET}{Style.NORMAL}")
    url = shit2scan[0]
    url = url.split()
    url = url[0]
    i = 0
    while i <= 5:
        asyncio.get_event_loop().run_until_complete(screenshot(url,homeDir,domain))
        i += 1
    total = 0
    for i in benchmark:
        total += i    
    average = total / len(benchmark)
    totLen = len(shit2scan)
    totScanTime = (int(average) * totLen) / 60
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Estimated {int(average)} second/s per request. ♦\n{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Estimated {round(totScanTime,1)} minute/s to complete screenshots. ♦{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ This number could be COMPLETELY wrong ♦\n{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Beginning subdomain screenshot/s now. ♦\n{Fore.RESET}{Style.NORMAL}")
    i = 0
    for i in shit2scan:
        i2 = i.split()
        asyncio.get_event_loop().run_until_complete(screenshot2(str(i2[0]),homeDir,domain,str(i2[1])))
    
async def screenshot(line,homeDir,domain):
    timeStart = time.time()
    browser = await launch(headless=True)
    page = await browser.newPage()
    url = f"https://{line}"
    await page.goto(str(url))
    await page.screenshot({'path': f'{homeDir}/output/{domain}/{line}.png'})
    await browser.close()
    timeEnd = time.time()
    os.remove(f'{homeDir}/output/{domain}/{line}.png')
    timeLapsed = timeEnd - timeStart
    time_convert(timeLapsed)
        
async def screenshot2(url,homeDir,domain,sCode):
    url2 = "https://" + url
    try:
        os.mkdir(f"{homeDir}/output/{domain}/report/{sCode}")
    except:
        None
    browser = await launch(headless=True)
    page = await browser.newPage()
    #print(f"Shotting {url}")
    try:
        await page.goto(str(url2))
        await page.screenshot({'path': f'{homeDir}/output/{domain}/report/{sCode}/{url}.png'})
        await browser.close()
    except:
        None