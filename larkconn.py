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
 
  requests.request("POST", webhookurl, headers=headers, data=payload)
  print('Alerted')
  print()

  


  
 
  

  