import os
import sys
import redis

PYTHON_VERSION = sys.version_info[0]
if PYTHON_VERSION == 3:
    import urllib.parse
else:
    import urlparse

basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import dotenv_values
default_config = dotenv_values('.env')
testing_config = dotenv_values('.testing.env')


class Config:
    APP_NAME = default_config['APP_NAME']
    SECRET_KEY = default_config['SECRET_KEY']
    #### IMAP CONFIG
    IMAP_USERNAME = default_config['IMAP_USERNAME']
    IMAP_PASSWORD = default_config['IMAP_PASSWORD']
    IMAP_SERVER = default_config['IMAP_SERVER']

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    REDISPASS=default_config["REDISPASS"]
    REDISURL = default_config["REDISURL"]
    REDISPORT = default_config["REDISPORT"]
    REDISDB = default_config["REDISDB"]
    REDIS_URI = "redis://{}@{}:{}/{}".format(REDISPASS, REDISURL, REDISPORT, REDISDB)
    # REDISPASS= os.environ.get('REDISPASS', None)
    # REDISURL = os.environ.get('REDISURL', '192.168.1.7')
    # REDISPORT = os.environ.get('REDISPORT', 6379)
    # REDISDB = os.environ.get('REDISDB', 0)
    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')

class TestingConfig(Config):
    DEBUG = True
    REDISPASS=testing_config["REDISPASS"]
    REDISURL = testing_config["REDISURL"]
    REDISPORT = testing_config["REDISPORT"]
    REDISDB = testing_config["REDISDB"]
    REDIS_URI = "redis://{}@{}:{}/{}".format(REDISPASS, REDISURL, REDISPORT, REDISDB)

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
