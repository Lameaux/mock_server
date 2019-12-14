from flask import request
from flask_restful import Resource
import time


class DefaultResource(Resource):
    def __init__(self):
        Resource.__init__(self)

        self.status_code = 200
        self.body = {}

    def get(self):
        return self._handle_request()

    def _post(self):
        return self._handle_request()

    def _handle_request(self):
        self._sleep()
        self._status_code()

        return self.body, self.status_code

    def _sleep(self):
        sleep_seconds = request.args.get('sleep_seconds', default=0, type=float)
        time.sleep(sleep_seconds)
        self.body['sleep_seconds'] = sleep_seconds

    def _status_code(self):
        status_code = request.args.get('status_code', default=200, type=int)
        self.body['status_code'] = status_code
        self.status_code = status_code
