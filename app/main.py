import requests

from flask import request, jsonify
from flask.views import View

from config import Config


class GreetUser(View):
    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]
    def get_location(self):
        client_ip = self.get_ip()
        response = requests.get(f'https://ipapi.co/{client_ip}/json/').json()

        longitude = response.get('lon')
        latitude = response.get('lat')

        WEATHER_API_KEY='ad50fd5c91caf6b8dbb497b6b9886b30'
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}").json()
        location_data = {
            "client_ip": client_ip,
            "city": response.get("city"),
            "temperature": weather_data.get('main', {}).get('temp', 0)
        }
        return location_data
    def dispatch_request(self):

        location_data = self.get_location()

        client_ip = location_data.get('client_ip')
        
        location = location_data.get('city', 'Unknown City')

        temperature = location_data.get('temperature', 0)


        visitor_name = request.args.get('visitor_name', 'Guest')

        greeting = f"Hello, {visitor_name.title()}!, the temperature is {temperature} degrees Celcius in {location}"


        response = {
            'client_ip': client_ip,
            'location': location,
            'greeting': greeting
        }
        return jsonify(response)
