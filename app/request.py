from app import app
import urllib.request,json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

   

def process_results(news_list)
    '''
    Function that processess the news result and transform them to a list of objects
    
    Args:
        news_list:A list of dictioneries that contain news details
    Return:
        News_reults:A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToimage = news_item.get('urlToimage')
        author = news_item.get('author')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')


        if urlToimage:
            news_object = News(id,name,title,description,urlToimage,author,url,publishedAt)
            news_results.append(news_object)


     return news_results