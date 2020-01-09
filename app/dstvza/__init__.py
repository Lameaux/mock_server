from flask import Blueprint

dstvza = Blueprint('dstvza', __name__)

from . import endpoints
