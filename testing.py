import os
import subprocess
#from quart import Quart, g, request
from app.imap import setup_login
from app.imap import *
from dotenv import dotenv_values
import redis
hack_config = dotenv_values('.testing.env')

db = redis.StrictRedis(
    host=hack_config['REDISURL'],
    port=hack_config['REDISPORT'],
    db=hack_config['REDISDB'],
    decode_responses=True
)
imap = setup_login(
    server=hack_config['IMAP_SERVER'],
    username=hack_config['IMAP_USERNAME'],
    password=hack_config['IMAP_PASSWORD']
)
