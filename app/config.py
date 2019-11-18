class Config:
    '''
    General config parent class
    '''

    pass

class ProdConfig(Config):
    '''
    Production config child class

    Args:
        Config:The parent configuration class with General configuration serttings
    '''

    pass

class DevConfig(Config):
    '''
    Development configi child class

    Args:
        config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
NEWS_BASE_API_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'