class Config:
    """ Contains all necessary configuration parameters """
    SERVER_HOST = '127.0.0.1'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ Contains configuration parameters used during the development """
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
