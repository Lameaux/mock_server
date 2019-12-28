import time
import random
from flask import request, jsonify
from . import examples


@examples.route('/timestamp')
def current_time():
    return jsonify(time=time.time())


@examples.route('/random')
def next_random():
    return jsonify(random=random.random())
