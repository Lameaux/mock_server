from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .generic import generic as generic_blueprint
    app.register_blueprint(generic_blueprint)

    from .examples import examples as examples_blueprint
    app.register_blueprint(examples_blueprint)

    from .dstvza import dstvza as dstvza_blueprint
    app.register_blueprint(dstvza_blueprint, url_prefix='/dstvza')

    return app
