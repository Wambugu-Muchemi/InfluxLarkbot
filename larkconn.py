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
          "title": f"{data.split(' ')[0]} 2218 Offline Issue",
          "content": [
            [
              {
                "tag": "text",
                "text": data
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
 
  #requests.request("POST", 'https://open.larksuite.com/open-apis/bot/v2/hook/775ac01a-ff80-4a2e-94f1-82bde2db79b8', headers=headers, data=payload)
  print('Alerted')
  print()

  


  
 
  

  