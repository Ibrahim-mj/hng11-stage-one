import requests

from flask import request, jsonify
from flask.views import View

from config import Config


class GreetUser(View):
    def get_ip(self):
        try:
            return request.headers['X-Real-IP']
        except KeyError:
            # Handle case where X-Real-IP header is not present
            return request.remote_addr
            
    def get_location(self):
        client_ip = self.get_ip()
        # response = requests.get(f'http://ip-api.com/json/{client_ip}').json()
        response = requests.get(f'https://ipapi.co/{client_ip}/json/').json()
        print(f'response:{response}')

        longitude = response.get('longitude')
        latitude = response.get('latitude')

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={Config.WEATHER_API_KEY}").json()
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
