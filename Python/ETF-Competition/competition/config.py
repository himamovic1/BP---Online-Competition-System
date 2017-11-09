class Config:
    """ Contains all necessary configuration parameters """
    SECRET_KEY = 'some hard to guess string'  # TODO: Change me!!!
    SERVER_HOST = '127.0.0.1'

    # Database related settings
    SQLALCHEMY_DATABASE_URI = "postgresql://dbadmin:dbadmin@localhost:5432/etf_competition"
    SQLALCHEMY_ETFDB_URI = "oracle://username:password@server/db"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ Contains configuration parameters used during the development """
    DEBUG = True
    SERVER_HOST = '0.0.0.0'


class TestConfig(Config):
    """ Contains configuration parameters used during the testing process """
    pass


class ProductionConfig(Config):
    """ Contains configuration parameters used after the app went live """
    pass


# Dictionary with all available configurations
config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
