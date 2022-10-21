import requests
import json
import time
import os
from dotenv import load_dotenv
import asyncio
from redis import Redis
from worklist import *

redisclient = Redis(db=1)

load_dotenv() 

webhookurl = os.getenv('webhookurl')


def sendalert(data):

  modifieddata = data
  payload = json.dumps({
    "msg_type": "post",
    "content": {
      "post": {
        "en_us": {
          #"title": f"{data.split(' ')[0]} 2218 Offline Issue",

          "title":"OFFLINE BUILDINGS AS PER IAP PING STATUS",

          "content": [
            [
              {
                "tag": "text",
                #"text": f"""{data}"""
                "text": f"""{modifieddata}"""
              }, 
              
            ]
          ]
        }
      }
    }
  })
  headers = {
    'Content-Type': 'application/json'
  }
  if len(data) == 0:
        print('Nothing to send')
  else: 
    
    #print(data)
    return requests.request("POST", webhookurl, headers=headers, data=payload)
  
  #print(data)
  #print(f'Alerted {data}')
  

  


  
 
  

  