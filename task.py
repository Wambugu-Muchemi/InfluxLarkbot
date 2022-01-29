from celery import Celery
import time
from queryinflux import queryInflux
import asyncio

app = Celery('tasks',broker='pyamqp://guest@localhost//')


@app.task
async def main():
    start_time = time.strftime("%X")
    await queryInflux('zmmbucket')
    await queryInflux('g45bucket')
    print(f'started at {start_time}')
    print(f'finished at {time.strftime("%X")}')

asyncio.run(main(), debug=True)

