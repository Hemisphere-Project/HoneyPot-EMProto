# coding=utf-8

import requests
import json
import dateutil.parser

from flask import Flask
webapp = Flask(__name__)

# Dashboard Template
from jinja2 import Environment, PackageLoader
jinja_env = Environment(loader=PackageLoader('server', 'views'))

@webapp.route("/")
def home():

    dashboard = jinja_env.get_template('base.html')

    data = {}

    req = requests.get('https://api.smartcitizen.me/devices/3615').json()

    data['sck_id'] = req['id']
    data['sck_name'] = req['name']
    data['sck_city'] = req['data']['location']['city']
    data['sck_country'] = req['data']['location']['country']
    data['sck_inout'] = req['data']['location']['exposure']

    for sensor in req['data']['sensors']:
        if sensor['id'] == 12: key = 'temp'
        elif sensor['id'] == 13: key = 'humi'
        elif sensor['id'] == 7: key = 'noise'
        elif sensor['id'] == 14: key = 'light'
        else: key = None
        if key:
            data[key] = {'value': round(sensor['value'],2), 'updated': dateutil.parser.parse(req['last_reading_at']).strftime("%d/%m/%Y %H:%M:%S")}


    return dashboard.render(data)


if __name__ == "__main__":
    webapp.run()
