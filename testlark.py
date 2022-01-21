import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv() 

webhookurl = os.getenv('webhookurl')
def send_alarm(data:str):
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
              # {
              #   "tag": "text",
              #   "text": "POSTMANTEST",
              #   "href": "GRAFANA RECORD"
              # }
            ]
          ]
        }
      }
    }
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
