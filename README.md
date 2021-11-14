# airQualityScraper
Docker based api scrapper.

It parse air quality data from the [aqicn.org](https://aqicn.org/data-platform/token/#/) API and puts data to [Influxdb](https://www.influxdata.com/) database.

## Install

1. Get the API key from [aqicn.org](https://aqicn.org/data-platform/token/#/)
2. Create file `.env` and fill it with this template:

    * `TOKEN={YOUR_TOKEN}` - aqicn token

        (other variables is not necessary and have default values)
    * `CITY_NAME=kyiv` - check you entered the right city name that aqicn.org knows about it!
    * `INTERVAL=300` - interval between requests

3. Then run in console command: `docker-compose up -d`
