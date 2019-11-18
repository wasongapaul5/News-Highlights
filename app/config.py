import os
class Config:
    '''
    parent class general configuration
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey='
    HIGHLIGHTS_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class ProdConfig(Config):
    '''
    production configuration child class
    Args:
        config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development confiuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
