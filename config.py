
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
    SQLALCHEMY_DATABASE_URI ='postgresql://diksgaxlzlppdk:d7b7af485faaf0370a084df7c5b262d558d6f275e3636c823312c39e033c3557@ec2-54-204-56-171.compute-1.amazonaws.com:5432/dcm4kvjah3mvdb'
    DEBUG=True

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:james@localhost/test_user'
    pass

class DevConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:james@localhost/blogs'
   DEBUG = True
   pass


config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}