from flask import render_template
from app import app


@app.route('/')
def index():

    '''
    View root page function that returns the index page and it's data
    '''
    message = 'News Headlines'
    return render_template('index.html',message = message)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and it's data
    '''

    return render_template('news.html',id = news_id)