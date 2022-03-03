from larkconn import sendalert
import asyncio
import csv
import json
from redis import Redis
redisclient = Redis(db=1)
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

allalarms = []
def cachealert(alrt):
   # print(f'{alrt} will be cached...')
    itema = unique(alrt)
    #print(itema)
    cacher(itema)
    

def unique(listel):
    x = np.array(listel)
    
    return np.unique(x)

def cacher(itemms):
    
    ts = itemms.tolist()
    for d in ts:
        host = f'{d.split()[0]}'
        alarmkey = f"{host+ ':' + d.split()[1]}"
        bldgname = f'{d.split()[1]}'
        alarmserial = {alarmkey:bldgname}
        
        with redisclient.pipeline() as pipe:
            if redisclient.hgetall(alarmkey):
                print('incahe')
                
            else:
                  
                pipe.hmset(alarmkey,alarmserial)
                pipe.expire(alarmkey,1800)
                pipe.execute()
                allalarms.append(alarmkey)
        redisclient.close()
    if allalarms:
        sendalert(allalarms)
        allalarms = []
    else:
        return None
        
   
   
    
    
    

    
    
   
    