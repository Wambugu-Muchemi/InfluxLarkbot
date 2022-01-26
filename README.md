#InfluxLarkbot

<h3>Description</h3>
We want to create a service that sends alert messages to a larkbot through webhook.
To achieve this, we need to prepare the data to be sent as a message.
We shall interact with our influxdb service and fetch data from the buckets.
We clean the data and send it as a payload in a POST request to the webhook url.
<br/>
</hr>

<h4>Notes:</h4>

We need to control the alerts to avoid alert panic.
Implement an asyncio pattern and await before sending data to bot- control rate limit.
Implement a caching mechanism to allow us control sendalarm heartbeat.

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


