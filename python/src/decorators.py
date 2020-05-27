import pickle
import requests
import re
import json
import traceback

from pprint import pprint
from flask import request
from functools import wraps

from src.extensions import redis
from src.helpers import MyHelper


CACHE_TIMEOUT_FACTOR = 1


def cache_function(timeout=300, key_prefix='common', keep_timeout=False):
    """
    Decorator for caching functions using sentinel, using its arguments as part of the key.
    Returns the cached value, or the function if the cache is disabled
    """
    if timeout is None:
        timeout = 300

    if not keep_timeout:
        timeout *= CACHE_TIMEOUT_FACTOR

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            key = "%s:%s" % (key_prefix, f.__name__)
            key_to_hash = MyHelper.get_key_to_hash(*args, **kwargs)
            key = MyHelper.get_hash_key(key, key_to_hash)
            output = redis.get(key)
            if output:
                # print('Get data to redis UX, done!')
                return pickle.loads(output)
            output = f(*args, **kwargs)
            redis.setex(key, timeout, pickle.dumps(output))
            # print('Set data to redis UX, done!')
            return output
        return wrapper
    return decorator


# @cache_function(3600, key_prefix='user_info')
def get_by_token(token):
    return {
        'user_id': '2709',
        'user_name': 'whoiskp',
    }
    


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return {'message': 'Token is missing.'}, 401
        if len(token) < 10:
            return {'message': 'Token is invalid.'}, 401
        user_info = get_by_token(token)
        
        if not user_info:
            return {'message': 'Your token is wrong, wrong, wrong!!!'}, 401

        return f(user_info=user_info, *args, **kwargs)

    return decorated


def get_user_info(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['Authorization'] if 'Authorization' in request.headers else ''
        user_info = None
        if token and len(token) > 10:
            user_info = get_by_token(token)
        print(user_info, flush=True)
        return f(user_info=user_info, *args, **kwargs)

    return decorated
