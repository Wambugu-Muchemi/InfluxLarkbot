
import datetime as datetime
import sys
import time
import os
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS
from larkconn import sendalert
import asyncio
import csv
from cachealert import cachealert
from celery import Celery


app = Celery('tasks',broker='pyamqp://guest@localhost//')


load_dotenv()

token = os.getenv('token')
url = os.getenv('url')
buckets = ['zmmbucket', 'g44bucket', 'g45bucket']


async def queryInflux(bucket):

    with InfluxDBClient(url=url, token=token, org="AH", debug=False) as client:

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
            await asyncio.sleep(1)
            rec = f'{record["host"]} {record["name"]} Building'
            # need to implement caching
            cachealert(rec)
            print(f'{record["host"]}')
        return


