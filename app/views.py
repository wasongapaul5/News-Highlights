from flask import render_template
from app import app
from .request import get_highlights
# views
@app.route('/')
def index():
    '''
    vie`w the root page function that returns the index page and its content
    '''
    # getting top headlines
    top_headlines = get_highlights()
    print(top_headlines)
    title = 'Home - HOT NEWS AND BLOSSY GOSSIP'
    return render_template('index.html',title = title, top = top_headlines )
@app.route('/news/<news_id>')
def news(news_id):
    '''
    view movie page function that returns the news highlight page and its data
    '''
    return render_template('news.html',id=news_id)

