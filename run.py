#!/usr/bin/env python2.7.9

from app import create_app

if __name__ == "__main__":
    app = create_app('config.DevelopmentConfig')
    app.run()
