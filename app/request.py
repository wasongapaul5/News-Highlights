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
        url=news_item.get('url')
        urlToImage=news_item.get('urlToImage')
        if title:
            news_object = Articles(id,name,author,title,url,urlToImage,)
            news_results.append(news_object)
    return news_results



def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = base_url.format(category,api_key)
	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)
		sources_results = None
		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)
	return sources_results
def process_sources(sources_list):
	'''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''
	sources_results = []
	for source_item in sources_list:
		id = source_item.get('id')
		name = source_item.get('name')
		url = source_item.get('url')
		category = source_item.get('category')
		language = source_item.get('language')
		country = source_item.get('country')
		sources_object = Sources(id,name,description,url,category,country,language)
		sources_results.append(sources_object)
	return sources_results