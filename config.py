import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'development'
    DEBUG = True

    POSTS_PER_PAGE = 25

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'testingm235@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'test1q2w3eapp'
    ADMINS = ['testingm235@gmail.com']

    LANGUAGES = ['en', 'es', 'ru']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') or 'ff0aa148ec664ee39b6db407e195cd4a'
