import flask
from flask import request, jsonify
from youtube_api import  YouTubeDataAPI
YT_KEY = 'AIzaSyAlMc2u9oSzR-KQw3FAo7MC3fMI3yMWvSo' # you can hardcode this, too.
yt = YouTubeDataAPI(YT_KEY)


app = flask.Flask(__name__)
app.config["DEBUG"] = True


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


app.run()
