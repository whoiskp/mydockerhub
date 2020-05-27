import os
import urllib3
from flask import Flask
from bson import ObjectId
import json
import datetime

import sentry_sdk
from sentry_sdk.integrations.flask import \
    FlaskIntegration
from .api import bp as DEFAULT_BLUEPRINT
from .extensions import (redis, mdb)
from .configs import DefaultConfig

# for import *
__all__ = ['create_app']


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


def create_app():
    app = Flask('your_app_name')
    # init config
    app.config.from_object(DefaultConfig)
    app.json_encoder = JSONEncoder

    # init extension
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    mdb.init_app(app)
    redis.init_app(app, config_prefix='APP_REDIS')
    SENTRY_DSN = app.config.get('SENTRY_DSN')
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[FlaskIntegration()]
    )
    print(SENTRY_DSN)
    # init blueprint
    app.register_blueprint(DEFAULT_BLUEPRINT)

    return app
