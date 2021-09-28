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

def initScreenshot(resDir,twoSCode,threeSCode,fourSCode,fiveSCode,domain,homeDir):        
    global benchmark
    benchmark = []
    jsonInit = open(resDir,'r')
    jsonData = json.loads(jsonInit.read())
    jsonInit.close()  
    sCodes = []
    checkCodes = []
    twoHunUrl = []
    threeHunUrl = []
    fourHunUrl = []
    fiveHunUrl = []
    totBenchAdd = 0
    if twoSCode == "y":
        checkCodes.append("200")
        totBenchAdd += 1
    if threeSCode == "y":
        checkCodes.append("300")
        totBenchAdd += 1
    if fourSCode == "y":
        checkCodes.append("400")
        totBenchAdd += 1
    if fiveSCode == "y":
        checkCodes.append("500")
        totBenchAdd += 1
    for d in jsonData:
        statusCode = d["sCode"]
        url = d["url"]
        sCodes.append(statusCode + "::" + url)
    for i in sCodes:
        for i2 in checkCodes:
            if "200" in i2:
                if i2 in i:
                    i3 = i.split("::")
                    twoHunUrl.append(i3[1])
            if "300" in i2:
                if i2 in i:
                    i3 = i.split("::")
                    threeHunUrl.append(i3[1])
            if "400" in i2:
                if i2 in i:
                    i3 = i.split("::")
                    fourHunUrl.append(i3[1])
            if "500" in i2:
                if i2 in i:
                    i3 = i.split("::")
                    fiveHunUrl.append(i3[1])
    
    try:
        os.mkdir(f"{homeDir}/output/{domain}/report")
    except:
        None
    
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Benchmarking... ♦\n{Fore.RESET}{Style.NORMAL}")
    url = twoHunUrl[0]
    i = 0
    while i <= 5:
        asyncio.get_event_loop().run_until_complete(screenshot(url,homeDir,domain,"benchmark"))
        i += 1
    total = 0
    for i in benchmark:
        total += i    
    average = total / len(benchmark)
    totLen = len(twoHunUrl)
    totLen += len(threeHunUrl)
    totLen += len(fourHunUrl)
    totLen += len(fiveHunUrl)
    totScanTime = (int(average) * totLen) / 60
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Estimated {int(average)} second/s per request. ♦\n{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Estimated {round(totScanTime,1)} minute/s to complete screenshots. ♦{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ This number could be COMPLETELY wrong ♦\n{Fore.RESET}{Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n♦ Beginning subdomain screenshot/s now. ♦\n{Fore.RESET}{Style.NORMAL}")
    if not twoHunUrl:
        None
    else:
        for line in twoHunUrl:
            asyncio.get_event_loop().run_until_complete(screenshot(line,homeDir,domain,"200"))
    if not threeHunUrl:
        None
    else:
        for line in threeHunUrl:
            asyncio.get_event_loop().run_until_complete(screenshot(line,homeDir,domain,"300"))
    if not fourHunUrl:
        None
    else:
        for line in fourHunUrl:
            asyncio.get_event_loop().run_until_complete(screenshot(line,homeDir,domain,"400"))
    if not fiveHunUrl:
        None
    else:
        for line in fiveHunUrl:
            asyncio.get_event_loop().run_until_complete(screenshot(line,homeDir,domain,"500"))
        
async def screenshot(line,homeDir,domain,sCode):
    if sCode == "benchmark":
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
    else:
        try:
            os.mkdir(f"{homeDir}/output/{domain}/report/{sCode}")
        except:
            None
        browser = await launch(headless=True)
        page = await browser.newPage()
        url = f"https://{line}"
        #print(f"Shotting {url}")
        await page.goto(str(url))
        await page.screenshot({'path': f'{homeDir}/output/{domain}/report/{sCode}/{line}.png'})
        await browser.close()

    