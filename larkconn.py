import requests
import json
import time
import os
from dotenv import load_dotenv
import asyncio
from redis import Redis

redisclient = Redis(db=1)

load_dotenv() 

webhookurl = os.getenv('webhookurl')


def sendalert(data):
  payload = json.dumps({
    "msg_type": "post",
    "content": {
      "post": {
        "en_us": {
          #"title": f"{data.split(' ')[0]} 2218 Offline Issue",
          "title":"2218 OFFLINE ISSUE",
          "content": [
            [
              {
                "tag": "text",
                "text": f"""{data}"""
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
 
  yield requests.request("POST", webhookurl, headers=headers, data=payload)
  
  #print(data)
  #print(f'Alerted {data}')
  

  


  
 
  

  