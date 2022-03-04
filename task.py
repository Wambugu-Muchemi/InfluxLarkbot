from celery import Celery
from celery.schedules import crontab
import time
from queryinflux import queryInflux
import asyncio
from celery import chain

app = Celery('task',broker='amqp://guest:guest@172.17.0.3:5672//',result_backend = 'rpc://')
#app.conf.timezone = 'Africa/Nairobi'
app.conf.beat_schedule = {
    'fetch  influxquery results':{
        'task': 'MAINTASK',
        'schedule': 420,
    }
}

buckets = ['zmmbucket','g44bucket','g45bucket']
@app.task(name='MAINTASK')
def main():    
    for bucket in buckets:
        queryInflux(bucket)
    return None