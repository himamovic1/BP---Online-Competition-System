class Config:
    """ Contains all necessary configuration parameters """
    pass


class DevelopmentConfig(Config):
    """ Contains configuration parameters used during the development """
    pass


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
