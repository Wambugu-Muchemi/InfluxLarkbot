
import datetime as datetime
import time
import os
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS
from larkconn import sendalert
import asyncio

from cachealert import cachealert


load_dotenv() 
token = os.getenv('token')
url = os.getenv('url')

async def queryInflux():
    bucket = 'zmmbucket'
    with InfluxDBClient(url=url, token=token, org="AH", debug=False) as client:
        bucket = 'zmmbucket'
        query_api = client.query_api()
        """
        Query: using Stream
        """
        records = query_api.query_stream(f'''
        from(bucket:"{bucket}")
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
            #need to implement caching
            cachealert(rec)
            
            #determinant for send alarm
            #check if exist in cache 
            #if not send alarm
            await sendalert(rec)
          
            
if __name__ == '__main__':
    asyncio.run(queryInflux())