import requests
import json
import time


def send_alarm(data:str):
  url = "https://open.larksuite.com/open-apis/bot/v2/hook/775ac01a-ff80-4a2e-94f1-82bde2db79b8"
  
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
