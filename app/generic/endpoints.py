from flask import request, jsonify

from app.generic.features import sleep_seconds, override_status_code
from . import generic


@generic.route('/generic', methods=['GET', 'POST'])
def default():
    result = {
        'sleep_seconds': sleep_seconds(request),
        'status_code': override_status_code(request)
    }

    return jsonify(result), result['status_code']
