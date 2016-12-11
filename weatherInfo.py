import requests
import json

def relevant_weather_data():
	json = requests.get(callUrl())

def call_url():
	url = "api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}"
	config_values = {}
	with open('config.json') as file:
		data = file.read()
		config_values = json.loads(data)

	url.format(config_values.get("city"), config_values.get("token"))
		
