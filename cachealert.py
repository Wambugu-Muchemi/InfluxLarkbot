from larkconn import sendalert
import asyncio
import csv
import json
from redis import Redis
redisclient = Redis(db=1)

def cachealert(alrt):
    #print(f'{alrt} will be cached...')
    host = f'{alrt.split()[0]}'
    alarmkey = f"{host+ ':' +alrt.split()[1]}"
    bldgname = f'{alrt}'
    alarmserial = {alarmkey:bldgname}
    with redisclient.pipeline() as pipe:
        if redisclient.hgetall(alarmkey):
            print('Faild cache')
        else:    
            pipe.hmset(alarmkey,alarmserial)
            pipe.execute()
            sendalert(alrt)
    
    print(f'Sending to Prepare & send alert..')
   
    
    
   
    