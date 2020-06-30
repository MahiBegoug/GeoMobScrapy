import flask
from flask import request, jsonify
from youtube_api import  YouTubeDataAPI
from twitter_scraper import get_tweets
import wikipedia
# import twitter_scraper

YT_KEY = 'AIzaSyAlMc2u9oSzR-KQw3FAo7MC3fMI3yMWvSo' # you can hardcode this, too.
yt = YouTubeDataAPI(YT_KEY)


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"


@app.route("/api/twitter",methods=['GET'])
def twitter_name():
    if 'name' in request.args:
        country_name = str(request.args['name'])
        return jsonify(get_tweets(country_name))


@app.route("/api/wiki",methods=['GET'])
def wiki_name():
    # check if an name Country provided
    # if ID is provided, assing it to a variable
    # if no ID is provided, display an error in the browser
    if 'name' in request.args:
        country_name = str(request.args['name'])
        wikipedia.set_lang("en")
        wikipage = wikipedia.page(country_name)
        data = {
            'title': wikipage.title,
            'url':wikipage.url,
            'summary':wikipage.summary,
            'content':wikipage.content,
            'images':wikipage.images,
            'mainImage':wikipage.images[0]
        }
        return jsonify(data)

@app.route('/api/country', methods=['GET'])
def country_name():
    # check if an name Country provided
    # if ID is provided, assing it to a variable
    # if no ID is provided, display an error in the browser
    if 'name' and 'max' in request.args:
            country_name = str(request.args['name'])
            max_results = int(request.args['max'])
            return jsonify(yt.search(q=country_name, max_results=max_results))
    else:
        return jsonify("Error: No name field provided. Please specify an Name Country.")

if __name__ == '__main__':

    app.run()
