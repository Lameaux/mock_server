import time
from flask import request, jsonify
from . import main


def _sleep_seconds(body):
    sleep_seconds = request.args.get('sleep_seconds', default=0, type=float)
    time.sleep(sleep_seconds)
    body['sleep_seconds'] = sleep_seconds


def _status_code(body):
    status_code = request.args.get('status_code', default=200, type=int)
    body['status_code'] = status_code
    return status_code


@main.route('/')
def index():
    return 'Welcome to Mock HTTP Server'


@main.route('/default', methods=['GET', 'POST'])
def default():
    response_body = {}

    _sleep_seconds(response_body)
    status_code = _status_code(response_body)

    return jsonify(response_body), status_code

