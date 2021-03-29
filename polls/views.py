import json
from collections import OrderedDict

from django.contrib.sites import requests
from django.http import HttpResponse
import coreapi
import asyncio


def async_fun(request):
    r = asyncio.run(main())
    return HttpResponse("Hello,async_fun   = " + str(r))


async def main():
    r1, r2, r3 = await asyncio.gather(first(), sec(), three())
    print((r2 + r2 + r3) / 3)
    return (r2 + r2 + r3) / 3


async def first():
    client = coreapi.Client()
    schema = client.get('https://www.metaweather.com/api/location/44418/2013/4/27/')
    od = OrderedDict(schema[0])
    # print(od['min_temp'])
    return od['min_temp']


async def sec():
    client = coreapi.Client()
    schema = client.get('http://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json')
    j = json.loads(schema)
    if "dataseries" in j:
        r = j["dataseries"]
        d = r[0]
        # print(d['temp2m'])
        return d['temp2m']


async def three():
    client = coreapi.Client()
    schema = client.get('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58')
    print(type(schema))
    s = schema["properties"]
    t = s['timeseries']
    t_new = t[0]

    i = t_new['data']
    ii = i['instant']
    d = ii['details']
    #  print(d['air_temperature'])
    a = d['air_temperature']
    return a


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
