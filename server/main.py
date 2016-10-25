import requests
from flask import Flask
webapp = Flask(__name__)

@webapp.route("/")
def home():
    return "Hello World!"

@webapp.route("/device/<device_id>")
def device(device_id):
    data = requests.get('https://api.smartcitizen.me/devices/'+device_id)
    return "Hello SCK "+device_id+"\n"+data.text

if __name__ == "__main__":
    webapp.run()
