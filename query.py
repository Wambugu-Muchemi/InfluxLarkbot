
import datetime as datetime
import time
import os
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS
from larkconn import sendalert
import asyncio


load_dotenv() 
token = os.getenv('token')
url = os.getenv('url')

async def queryInflux():
    bucket = 'zmmbucket'
    with InfluxDBClient(url=url, token=token, org="AH", debug=True) as client:
        bucket = 'zmmbucket'
        query_api = client.query_api()
        """
        Query: using Stream
        """
        records = query_api.query_stream('''
        from(bucket:"zmmbucket")
        |> range(start: -10s, stop: now())
        |> filter(fn: (r) => r["_measurement"] == "ping")
        |> filter(fn: (r) => r["_field"] == "percent_packet_loss")
        |> filter(fn: (r) => r["_value"] >= 100)
        |> yield(name: "last")
        |> unique(column: "name")
        ''') 

        for record in records:
            await asyncio.sleep(4)
            rec = f'{record["host"]}  {record["name"]}'
            #print(rec)
            
            #need to implement caching
            
            #adjust to send to chacher or determinant for send alarm
            #delegate send alarm to different function
            await sendalert(rec)
            #send_alarm(rec)
            
            
if __name__ == '__main__':
    asyncio.run(queryInflux())