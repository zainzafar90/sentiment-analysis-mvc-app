from flask import render_template
from flask import jsonify
from flask import request

import app
import api.sentiment 

# VIEWS


def index():
    return render_template('index.html')


def by_query():
    query = request.args.get('query')
    sentimentTweets = api.sentiment.Sentiment()
    tweets = sentimentTweets.get(query)

    return render_template(
        'query.html',
        tweets=tweets[0]
    )