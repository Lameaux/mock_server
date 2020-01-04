from flask import Blueprint

generic = Blueprint('generic', __name__)

from . import endpoints
