"""
    Module defines the configuration params for different environments,
    viz.,
        DefaultConfig - params common across all environments
                       - i.e., SECRET_KEY, CSRSF_ENABLED=True

        DevelopmentConfig - params specific to the development environment
                        - i.e., DEBUG=True

        ProductionConfig - params specific to the production environment
                        - i.e., DEBUG=False
"""


import os


class DefaultConfig:
    """
        Define default configuration params
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    CSRF_ENABLED = True
    TEST = False


class DevelopmentConfig(DefaultConfig):
    """
        Overide some of the default configuration params with
        development-specific params
    """
    DEBUG = True


class TestingConfig(DefaultConfig):
    """
        Overide some of the default configuration params with
        testing-specific params
    """
    TEST = True
