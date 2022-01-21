
import datetime as datetime
import time
import os
from dotenv import load_dotenv



from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS
from testlark import send_alarm


load_dotenv() 
token = os.getenv('token')
url = os.getenv('url')

def queryInflux():
    with InfluxDBClient(url=url, token=token, org="AH", debug=True) as client:

        query_api = client.query_api()
        """
        Query: using Stream
        """
        records = query_api.query_stream('''
        from(bucket:"zmmbucket")
        |> range(start: -20s, stop: now())
        |> filter(fn: (r) => r["_measurement"] == "ping")
        |> filter(fn: (r) => r["_field"] == "percent_packet_loss")
        |> filter(fn: (r) => r["_value"] >= 100)
        |> yield(name: "last")
        |> unique(column: "name")
        ''')

        for record in records:
            time.sleep(4)
            rec = f'Source:{record["host"]}  {record["name"]} is  Offline'
            send_alarm(rec)
            
            
            

if __name__ == '__main__':
    queryInflux()
