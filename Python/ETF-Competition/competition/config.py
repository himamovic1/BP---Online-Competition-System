class Config:
    """ Contains all necessary configuration parameters """
    SECRET_KEY = 'some hard to guess string'  # TODO: Change me!!!
    SERVER_HOST = '127.0.0.1'

    # Database related settings
    SQLALCHEMY_DATABASE_URI = "postgresql://dbadmin:dbadmin@localhost:5432/etf_competition"
    # SQLALCHEMY_BINDS = {
    #     "etfdb": "oracle://BP03:o3tUtwdn@80.65.65.66/etflab"
    # }

    SECRET_KEY = "so secret much wow"
    ASSETS_DEBUG = True

    # Email related settings
    MAIL_SUBJECT_PREFIX = "ETF Competition"
    MAIL_SENDER = "ETF Admin <some.email@etf.unsa.ba>"

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
