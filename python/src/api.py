import requests
import traceback
import sentry_sdk
from bson import ObjectId
from flask import (Blueprint, request, jsonify, abort)

from src.helpers import MyHelper
from src.constants import *

bp = Blueprint(__name__, __name__, url_prefix='/')


@bp.route('')
def index():
    print('success')
    return MyHelper.make_cross_response({
        'msg': 'Your server is running',
        'constant': YOUR_CONSTANTS
    })


@bp.route('/sentry')
def debug_sentry():
    try:
        error = 1/0
    except Exception as e:
        traceback.print_exc()
        sentry_sdk.capture_exception(e)

    return MyHelper.make_cross_response({
        'msg': 'Check sentry url for detail of errors.',
    })
