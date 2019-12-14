from flask import Flask
from flask_restful import Api
from .default_resource import DefaultResource

app = Flask(__name__)
api = Api(app)

api.add_resource(DefaultResource, '/default')


@app.route("/")
def root():
    return 'Welcome to Mock HTTP Server'
