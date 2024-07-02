import requests

from flask import request, jsonify
from flask.views import View

from config import Config


class GreetUser(View):
    def dispatch_request(self):

        visitor_name = request.args.get('visitor_name', 'Guest')
        if request.headers.getlist("X-Forwarded-For"):
            client_ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            client_ip = request.remote_addr


        location_service_url = f"http://ip-api.com/json/{client_ip}"
        location_data = requests.get(location_service_url).json()
        
        city = location_data.get('city', 'Unknown City')
        longitude = location_data.get('lon')
        latitude = location_data.get('lat')

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={Config.WEATHER_API_KEY}").json()
        temperature = weather_data.get('main', {}).get('temp', 0)

        greeting = f"Hello, {visitor_name.title()}!, the temperature is {temperature} degrees Celcius in {city}"


        response = {
            'client_ip': client_ip,
            'location': city,
            'greeting': greeting
        }
        return jsonify(response)