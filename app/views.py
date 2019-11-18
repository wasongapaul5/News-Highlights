from flask import render_template
from app import app


@app.route('/')
def index():

    '''
    View root page function that returns the index page and it's data
    '''
    message = 'News Headlines'
    return render_template('index.html',messge = message)