import requests
import json
import time
import os
from dotenv import load_dotenv
import asyncio

load_dotenv() 

webhookurl = os.getenv('webhookurl')

async def sendalert(data):
  payload = json.dumps({
    "msg_type": "post",
    "content": {
      "post": {
        "en_us": {
          "title": "2218 Offline Issue",
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
  response = requests.request("POST", webhookurl, headers=headers, data=payload)
  print(response.text)
  return data
 
  

  