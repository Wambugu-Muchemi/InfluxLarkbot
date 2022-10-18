from larkconn import sendalert
import asyncio
import csv
import json
from redis import Redis

from dotenv import load_dotenv
from collections import  Counter

import requests
import json
import time
import os

import asyncio
import numpy as np


load_dotenv() 

webhookurl = os.getenv('webhookurl')
redisclient = Redis(db=1)

#use as factory function
def cachealert(alrt):
   # print(f'{alrt} will be cached...')
    itema = unique(alrt)
    #print(itema)
    return cacher(itema)
    
#only get unique from list
def unique(listel):
    x = np.array(listel)
    
    return np.unique(x)

allalarms= []
#allofflines = None
def cacher(itemms):
    ts = itemms.tolist()
    with open('G44.txt', 'a+') as f:
        f.write("\\n The following Buildings are offline in G44: \\n") 
    with open('ZMM.txt', 'a+') as f:
        f.write("\\n The following Buildings are offline in ZMM: \\n") 
    with open('G45.txt', 'a+') as f:
        f.write("\\n The following Buildings are offline in G45: \\n")
    with open('HTR.txt', 'a+') as f:
        f.write("\\n The following Buildings are offline in HTR: \\n") 
    with open('ROY.txt', 'a+') as f:
        f.write("\\n The following Buildings are offline in RM: \\n")  
    for d in ts:
        host = f'{d.split()[0]}'
        alarmkey = f"{host+ ':' + d.split()[1]}"
        bldgname = f'{d.split()[1]}'
        alarmserial = {alarmkey:bldgname}
        
        if redisclient.hgetall(alarmkey):
            print('incache')
        else:    
            pipe = redisclient.pipeline()
            print('caching')
            pipe.hmset(alarmkey,alarmserial)
            pipe.expire(alarmkey,1800)
            print('Cached')
            pipe.execute()
            print(alarmkey)
            # if host == 'G44-FIBER':
            #     with open('G44.txt', 'a+') as f:
            #         f.write(f"{bldgname}, ") 
            # if host == 'ZMM-FIBER':
            #     with open('ZMM.txt', 'a+') as f:
            #         f.write(f"{bldgname}, ") 
            # if host == 'G45-FIBER':
            #     with open('G45.txt', 'a+') as f:
            #         f.write(f"{bldgname}, ") 
            # if host == 'HTR-FIBER':
            #     with open('HTR.txt', 'a+') as f:
            #         f.write(f"{bldgname}, ") 
            # if host == 'ROY-FIBER':
            #     with open('ROY.txt', 'a+') as f:
            #         f.write(f"{bldgname}, ") 

            # with open ('G44.txt', 'rt') as file:
            #     content = file.read()
            #     with open('Offlinedata.txt', 'a+') as f:
            #             f.write(content) 
            # with open ('ZMM.txt', 'rt') as file:
            #     content = file.read()
            #     with open('Offlinedata.txt', 'a+') as f:
            #             f.write(content)
            # with open ('G45.txt', 'rt') as file:
            #     content = file.read()
            #     with open('Offlinedata.txt', 'a+') as f:
            #             f.write(content)
            # with open ('HTR.txt', 'rt') as file:
            #     content = file.read()
            #     with open('Offlinedata.txt', 'a+') as f:
            #             f.write(content)
            # with open ('ROY.txt', 'rt') as file:
            #     content = file.read()
            #     with open('Offlinedata.txt', 'a+') as fl:
            #             fl.write(content)
            # with open('Offlinedata.txt', 'rt') as fl: 
            #     allofflines = fl.read()
            print(alarmkey)
            allalarms.append(alarmkey)
            # allalarms.append(allofflines)
            # # allalarms.append(f"Offline building G44{zmmdata}")
            # # allalarms.append(f"Offline building G44{g45data}")
            # # allalarms.append(f"Offline building G44{htrdata}")
            # # allalarms.append(f"Offline building G44{roydata}")
            
    sendalert(allalarms)
    print(f'Before clear..{allalarms}')
    
    try:
        fileVariable = open('G44.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()

        fileVariable = open('ZMM.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()

        fileVariable = open('G45.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()

        fileVariable = open('HTR.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()

        fileVariable = open('ROY.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()

        fileVariable = open('Offlinedata.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()

        allalarms.clear()
        print(f'After clear...{allalarms}')
        return None 
    except  Exception as e:
        print(e)
   
                

   
    