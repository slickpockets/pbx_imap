from quart import Blueprint, abort, request, jsonify, url_for, redirect
import json
from app import db

main = Blueprint('main', __name__)

endpoints = {
    "urls": {
        "/": "nothing yet"
    }
}

def key_check(key):
    if db.exists(key) == 1:
        return(True)
    else:
        return(False)

def key_type_check(*args):
    print("args:", args, flush=True)
    empty = {}
    for i in args.pop():

        empty.update({i:  db.type(i)})

    return(empty)


@main.route("/")

@main.route('/')
def index():
    return(jsonify(endpoints))



@main.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
