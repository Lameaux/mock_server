from flask import render_template, current_app

from . import main


@main.route('/')
def index():
    urls = list(current_app.url_map.iter_rules())
    urls.sort(key=str)
    return render_template('main/index.html', urls=urls)
