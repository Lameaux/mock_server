import random
import time

from flask import jsonify

from . import examples


@examples.route('/timestamp')
def current_time():
    return jsonify(timestamp=time.time())


@examples.route('/random')
def next_random():
    return jsonify(random=random.random())
