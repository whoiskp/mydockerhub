import os


class DefaultConfig(object):
    DEBUG = BUNDLE_ERRORS = DEVELOP = False

    MONGO_URI = 'mongodb://localhost:27017/dev'
    APP_REDIS_URL = 'redis://localhost:6379/0'

    SENTRY_DSN = 'https://5e67be8c67fd4bf29c14134f22f82466@o398745.ingest.sentry.io/5254840'
