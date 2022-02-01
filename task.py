from celery import Celery
from celery.schedules import crontab
import time
from queryinflux import queryInflux
import asyncio

app = Celery('tasks',broker_url='pyamqp://guest@localhost//')
app.conf.timezone = 'Africa/Nairobi'
app.conf.beat_schedule = {
    'fetch  influxquery results':{
        'task': 'task.main',
        'schedule': 300,
    }
}

# @app.on_after_configure.connect
# def setup_peridic_tasks(sender, **kwargs):
#     sender.add_peridic_task(60,main.s(),name='fetch  influxquery results')

@app.task
async def main():
    start_time = time.strftime("%X")
    await queryInflux('zmmbucket')
    await queryInflux('g44bucket')
    print(f'started at {start_time}')
    print(f'finished at {time.strftime("%X")}')
    
asyncio.run(main(), debug=True)

