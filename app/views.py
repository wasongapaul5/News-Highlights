from flask import render_template
from app import app


@app.route('/')
def index():

    '''
    View root page function that returns the index page and it's data
    '''
    message = 'NEWS HIGHLIGHTS'
    return render_template('index.html',message = message)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and it's data
    '''

    return render_template('news.html',id = news_id)

def index():
    '''
    View root page function that returns the index page and it's data
    '''

    title = 'Home - Welcome to the best News Highlights Site Online'
    return render_template('index.html',title = title)


from .request import get_news
@app.route('/')
def index():

    '''
    View root page that returns the index page and its data
    '''

    topHeadlines_news = get_news('topHeadlines')
    print(top-headlines_news)
    title = 'Home,Welcome to The best News Highlights Site Online'
    return render_template('index.html', title = title,topHeadlines = top-headlines_news)
