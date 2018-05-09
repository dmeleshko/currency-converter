from flask import Flask
from flask_redis import FlaskRedis
from mockredis import MockRedis
from oxr import OXR

from app.cli import register as register_cli
from app.rates import Rates
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    if app.config['TESTING']:
        redis_store = FlaskRedis.from_custom_provider(MockRedis)
    else:
        redis_store = FlaskRedis()
    redis_store.init_app(app)
    app.rates = Rates(redis_store, app.config['CURRENCIES'])
    if app.config['OPENEXCHANGE_API_KEY']:
        app.rates_client = OXR(app.config['OPENEXCHANGE_API_KEY'])

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    register_cli(app)

    return app
