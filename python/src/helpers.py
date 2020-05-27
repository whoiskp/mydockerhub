import hashlib

from flask import make_response, jsonify, request


class MyHelper(object):
    @staticmethod
    def get_key_to_hash(*args, **kwargs):
        """ Return key to hash for *args and **kwargs."""
        key_to_hash = ""
        # First args
        for i in args:
            key_to_hash += ":%s" % i
        # Attach any kwargs
        for key in sorted(kwargs):
            key_to_hash += ":%s" % kwargs[key]

        return key_to_hash

    @staticmethod
    def get_hash_key(prefix, key_to_hash):
        """ Return hash for a prefix and a key to hash."""
        key_to_hash = key_to_hash.encode('utf-8')
        key = prefix + ":" + hashlib.md5(key_to_hash).hexdigest()
        return key

    @staticmethod
    def make_cross_response(data, response_code=200):
        response = make_response(jsonify(data), response_code)
        # set headers for response CORS
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS'
        # response.headers['Access-Control-Allow-Headers'] = 'AUTHORIZATION, If-none-match'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Max-Age'] = 1728000
        response.headers['Access-Control-Expose-Headers'] = 'ETag, X-TOKEN'

        return response

    @staticmethod
    def response_customize(data, response_code=200):
        return make_response(jsonify(data), response_code)
