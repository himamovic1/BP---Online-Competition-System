import os


class Config:
    """ Contains all necessary configuration parameters """
    SECRET_KEY = "so secret much wow"  # TODO: Change me!!!
    SERVER_HOST = '127.0.0.1'
    ASSETS_DEBUG = True

    # Database related settings
    SQLALCHEMY_DATABASE_URI = "postgresql://dbadmin:dbadmin@localhost:5432/etf_competition"
    # SQLALCHEMY_BINDS = {
    #     "etfdb": "oracle://BP03:o3tUtwdn@80.65.65.66/etflab"
    # }

    # Email related settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    REQUIRED_MAIL_SERVICE = '@etf.unsa.ba'
    MAIL_ADMIN = os.environ.get('ETF_FLASK_MAIL_USERNAME', None)
    MAIL_USERNAME = os.environ.get('ETF_FLASK_MAIL_USERNAME', None)
    MAIL_PASSWORD = os.environ.get('ETF_FLASK_MAIL_MAGIC_WORD', None)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ Contains configuration parameters used during the development """
    DEBUG = True
    SERVER_HOST = '0.0.0.0'

    ASSETS_DEBUG = True


class TestConfig(Config):
    """ Contains configuration parameters used during the testing process """
    pass


class ProductionConfig(Config):
    """ Contains configuration parameters used after the app went live """
    ASSETS_DEBUG = False
    pass


# Dictionary with all available configurations
config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
