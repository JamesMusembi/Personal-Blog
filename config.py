
import os


class Config:
    BLOG_API_BASE_URL='http://quotes.stormconsultancy.co.uk/quotes.json'
    BLOG_API_KEY='http://quotes.stormconsultancy.co.uk/quotes.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:james@localhost/blogs'
   

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI ='postgresql://mxhwjrztvelttj:f78c638ad02dbae50ef11ca5e8acab88b2bdc1a3ae0e1fa274ff3186213aa009@ec2-107-22-238-112.compute-1.amazonaws.com:5432/de50v5u7j3bip6'
    DEBUG=True

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:james@localhost/test_user'
    pass

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:james@localhost/blogs'
   DEBUG = True


config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}