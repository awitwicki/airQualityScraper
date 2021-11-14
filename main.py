import json
import os
import time
import ssl
from urllib.request import urlopen, Request

token = os.getenv('TOKEN')
city = os.getenv('CITY_NAME', 'kyiv')
interval = int(os.getenv('INTERVAL', '300'))

api_url = f'https://api.waqi.info/feed/{city}/?token={token}'

def influx_query(query_str: str):
    try:
        request_url = 'http://localhost:8086/write?db=bots'
        request_headers = {'Content-Type': 'application/Text'}

        httprequest = Request(
            request_url,
            data=query_str.encode('utf-8'),
            headers=request_headers,
            method="POST"
            )

        urlopen(httprequest)
    except Exception as e:
        print(e)

httprequest = Request(api_url, headers={"Accept": "application/json"})

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        with urlopen(httprequest, context=ctx) as response:
            print(response.status)

            resp = response.read().decode()
            print(resp[:100])

            data = json.loads(resp)['data']['iaqi']

            values = ','.join([f"{f}={data[f]['v']}" for f in data.keys()])

            data_str = f'iot,room=city,device=api,sensor=airquality_api {values}'

            print(data_str)
            influx_query(data_str)

    except Exception as e:
        print(e)

    time.sleep(interval)
