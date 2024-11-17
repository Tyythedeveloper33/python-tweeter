from flask import Flask, render_template, redirect
from app.config import Config
import jinja2
from app.tweets import tweets
import random
from app.form.form import Form
app = Flask(__name__)
app.config.from_object(Config)
from datetime import datetime


@app.route("/")
def index():
    print(tweets)
    tweet = random.choice(tweets)
    return render_template('index.html', tweet=tweet)

@app.route("/feed")
def feed():

    return render_template('feed.html', tweets=tweets)

@app.route("/new", methods=["GET", "POST"])
def new():
    form = Form()

    if form.validate_on_submit():
        print(form.data)
        newTweet = {
            "id": len(tweets) + 1,
            "author": form.author.data,
            "date" : datetime.now().strftime("%m/%d/%Y") ,
            "tweet": form.tweet.data,
            "likes": 0,
        }
        tweets.append(newTweet)
        return redirect("/feed")
    return render_template('new.html', form=form)
