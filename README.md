<strong>#InfluxLarkbot</strong>

<h1>Description</h1>
We want to create a service that sends alert messages to a larkbot through webhook.
To achieve this, we need to prepare the data to be sent as a message.
We shall interact with our influxdb service and fetch data from the buckets.
We clean the data and send it as a payload in a POST request to the webhook url.
<br/>
</hr>

<h4>Notes:</h4>

We need to control the alerts to avoid alert panic.
Implement an asyncio pattern and cache influxdb results. We shall check if result in cache  before sending as alarm data to bot- control rate limit.
Implement celery beat to allow us control workflow run behavior.

<h3> Core Implementations</h3>

1. Fetch data from influxdb
    - query influxdb api and pass influx query as payload
    - Call cache function

2. Cache Function
    - Define an alarm key from influx call result
    - Check if key exists in redis db
    - If exists ignore calling sendalert function
    - If ! exists, call sendalert funtion and pass alarm message as payload

2. SendAlert Function
    - based on cache funtion result, send POST request to webhook url
    - pass cache function result as payload


<h2>Celery Implementation</h2>
We shall use Celery as task runner and scheduler. We shall then define a celery beat to control number of runs for our workflow.


