from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    WEATHER_API_KEY = config('WEATHER_API_KEY')