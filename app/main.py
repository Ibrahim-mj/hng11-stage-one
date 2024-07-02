import requests

from flask import request, jsonify
from flask.views import View

from config import Config


class GreetUser(View):
    def dispatch_request(self):
        if request.headers.getlist("X-Forwarded-For"):
            client_ip = request.headers.getlist("HTTP_X_FORWARDED_FOR")[0]
        else:
            client_ip = request.access_route[0]

        location_data = requests.get(f"http://ip-api.com/json/{client_ip}").json()
        
        location = location_data.get('city', 'Unknown City')

        longitude = location_data.get('lon')
        latitude = location_data.get('lat')

        visitor_name = request.args.get('visitor_name', 'Guest')



        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={Config.WEATHER_API_KEY}").json()
        temperature = weather_data.get('main', {}).get('temp', 0)

        greeting = f"Hello, {visitor_name.title()}!, the temperature is {temperature} degrees Celcius in {location}"


        response = {
            'client_ip': client_ip,
            'location': location,
            'greeting': greeting
        }
        return jsonify(response)