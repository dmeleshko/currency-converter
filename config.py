import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    OPENEXCHANGE_API_KEY = os.environ.get('OPENEXCHANGE_API_KEY')
    CURRENCIES = os.environ.get('CURRENCIES') or ['USD', 'CZK', 'EUR', 'PLN']
