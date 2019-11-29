from flask import Flask, request
import time

app = Flask(__name__)


@app.route("/")
def root():
    return 'Welcome to Mock HTTP Server'


@app.route("/sleep")
def sleep():
    sleep_time_in_seconds = request.args.get('seconds', default=0, type=float)
    time.sleep(sleep_time_in_seconds)
    return f'Slept for {sleep_time_in_seconds} seconds.'


@app.route("/status")
def http_status():
    code = request.args.get('code', default=200, type=int)
    return f'HTTP code: {code}.', code
