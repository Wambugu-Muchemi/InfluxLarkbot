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
  try:
        requests.request("POST", webhookurl, headers=headers, data=payload)
  except print('error handling send to lark bot'):
  #print(response.text)
  
    return None


  
 
  

  