from flask import Flask

from config import Config
from app.main import GreetUser

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.add_url_rule('/hello/', view_func=GreetUser.as_view('greet'))

    return app

app = create_app(Config)