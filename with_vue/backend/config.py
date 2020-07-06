import os
class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///myspa.db'
    # cookieを暗号化する秘密鍵
    SECRET_KEY = os.urandom(24)