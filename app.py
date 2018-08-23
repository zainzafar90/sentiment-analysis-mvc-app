#!/usr/bin/env python3

from flask import Flask

def create_app(config):
    # create app and load config
    app = Flask(__name__)
    app.config.from_object(config)


    # bind views
    from view import index, by_query
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/search', view_func=by_query)

    return app
