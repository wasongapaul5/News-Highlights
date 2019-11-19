from app import app
import urllib.request,json
from .models import news


api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
highlights_url = app.config["HIGHLIGHTS_URL"]
Source = news.Source
Articles = news.Articles


def get_highlights():
    '''
    function that gets the json response to our url rquest
    '''

    with urllib.request.urlopen(highlights_url+api_key) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results


def process_results(news_list):
    '''
    function that processes the news result and transform them into a list of objects
    Args:
        news_list:A list of dictionaries that contain news details
    Returns:
        news_list:A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id=news_item.get('id')
        name=news_item.get('name')
        author=news_item.get('author')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        urlToImage=news_item.get('urlToImage')
        publishedAt=news_item.get('publishedAt')
        if title:
            news_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt)
            news_results.append(news_object)
    return news_results



