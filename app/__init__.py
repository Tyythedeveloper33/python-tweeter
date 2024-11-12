from flask import Flask, render_template
from app.config import Config
import jinja2
from app.tweets import tweets
import random

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    print(tweets)
    tweet = random.choice(tweets)
    return render_template('index.html', tweet=tweet)

@app.route("/feed")
def feed():
    return render_template('feed.html', tweets=tweets)

