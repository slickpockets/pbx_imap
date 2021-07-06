import os
from quart import Quart
from config import config as Config
import redis
from quart_redis import RedisHandler, get_redis

from dotenv import dotenv_values
# config = dotenv_values('.env')
hack_config = dotenv_values('.testing.env')

db = redis.StrictRedis(
    host=hack_config['REDISURL'],
    port=hack_config['REDISPORT'],
    db=hack_config['REDISDB'],
    decode_responses=True
)


def create_db(config):
    #not working yet
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv('QUART_CONFIG', 'testing')

    db = redis.StrictRedis(
        host=Config[config_name]['REDISURL'],
        port=Config[config_name]['REDISPORT'],
        db=Config[config_name]['REDISDB'],
        decode_responses=True
    )
    return db

def create_app(config):
    app = Quart(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv('QUART_CONFIG', 'testing')

    app.config.from_object(Config[config_name])

    Config[config_name].init_app(app)

    from .routes import main as default_blueprint
    app.register_blueprint(default_blueprint)


    return app
#
