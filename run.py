import os
import subprocess
from quart import Quart, g, request
from quart.helpers import make_response
from app import create_app, create_db


app = create_app(os.getenv('QUART_CONFIG') or 'development')


if __name__ == '__main__':
    Quart.run(app, debug=True)
