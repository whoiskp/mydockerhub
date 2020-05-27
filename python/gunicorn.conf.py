# file gunicorn.conf.py
# coding=utf-8
# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import os
import multiprocessing

loglevel = 'info'
# errorlog = '/var/log/api-error.log'
# accesslog = '/var/log/api-access.log'
# errorlog = "-"
# accesslog = "-"

# bind = 'unix:%s' % '/var/run/gunicorn.sock'
bind = '0.0.0.0:5000'
workers = 3
# workers = multiprocessing.cpu_count() * 2 + 1

timeout = 3 * 60  # 3 minutes
keepalive = 24 * 60 * 60  # 1 day

capture_output = True
