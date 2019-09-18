from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    search_input = request.args.get('search_input')
    top_10 = request.args.get('top_10')

    # set the apikey and limit
    apikey = "LIVDSRZULELA"
    lmt = 9
    # TODO: Make 'params' dict with query term and API key
    params = {
        "api_key": "XE9GOKSZYLQB",
        "query_term": search_input,
        "num_gifs_to_load": 9
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    tenor_request = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params.get("query_term"),
                                 params.get("api_key"), params.get("num_gifs_to_load")))
    # get the top 10 trending GIFs - using the default locale of en_US
    top_10_gifs = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (apikey, lmt))

    loaded_gifs = None
    # TODO: Get the first 10 results from the search results

    print("Tenor status code: " + str(tenor_request.status_code))
    print("Top_10 value: " + str(top_10))

    if top_10 == "true" or tenor_request.status_code != 200 or len(tenor_request.content) == 0:
        loaded_gifs = json.loads(top_10_gifs.content)
    else:
        loaded_gifs = json.loads(tenor_request.content)

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template(
        "index.html",
        loaded_gifs=loaded_gifs,
        search_input=search_input)


if __name__ == '__main__':
    app.run(debug=True)

    