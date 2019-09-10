from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    search_input = request.args.get('search_input')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "api_key": "XE9GOKSZYLQB",
        "query_term": search_input,
        "num_gifs_to_load": 9
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    tenor_request = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params.get("query_term"),
                                 params.get("api_key"), params.get("num_gifs_to_load")))

    loaded_gifs = None
    # TODO: Get the first 10 results from the search results
    if tenor_request.status_code == 200:
        loaded_gifs = json.loads(tenor_request.content)
    else:
        loaded_gifs = none

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template(
        "index.html",
        loaded_gifs=loaded_gifs,
        search_input=search_input)


if __name__ == '__main__':
    app.run(debug=True)
