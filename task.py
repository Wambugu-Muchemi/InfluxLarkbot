from celery import Celery
from celery.schedules import crontab
import time
from queryinflux import queryInflux
import asyncio

app = Celery('task',broker='amqp://guest:guest@172.17.0.3:5672//',result_backend = 'rpc://')
app.conf.timezone = 'Africa/Nairobi'
app.conf.beat_schedule = {
    'fetch  influxquery results':{
        'task': 'MAINTASK',
        'schedule': 300,
    }
}


@app.task(name='MAINTASK')
def main():
    buckets = ['zmmbucket', 'g44bucket', 'g45bucket']
    start_time = time.strftime("%X")
    for bucket in buckets:
        
        queryInflux(bucket)
    
    print(f'started at {start_time}')
    print(f'finished at {time.strftime("%X")}')
    

    