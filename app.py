from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

random_words = []

@app.route('/')
def index():
    """Return homepage."""

    # TODO: Extract query term from url
    search_input = request.args.get('search_input')
    top_10_input = request.args.get('top_10')
    random_input = request.args.get('random')

    # set the apikey and limit
    apikey = "LIVDSRZULELA"
    lmt = 9
    # TODO: Make 'params' dict with query term and API key
    search_params = {
        "api_key": "XE9GOKSZYLQB",
        "query_term": search_input,
        "num_gifs_to_load": 9
    }

    top_10_params = {
        "api_key": "XE9GOKSZYLQB",
        "num_gifs_to_load": 9
    }

    random_params = {
        "api_key": "XE9GOKSZYLQB",
        "query_term": choice(random_words),
        "num_gifs_to_load": 9
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    search_request = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_params))
    # get the top 10 trending GIFs - using the default locale of en_US

    loaded_gifs = None
    # TODO: Get the first 10 results from the search results

    if top_10 == "true":
        top_10_request = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (top_10_params))
        loaded_gifs = json.loads(top_10_request.content)
    elif random_input == "true":
        random_request = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (random_params))
        loaded_gifs = json.loads(random_request.content)
    elif search_request.status_code == 200:
        loaded_gifs = json.loads(search_request.content)
    else:
        random_request = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (random_params))
        loaded_gifs = json.loads(random_request.content)

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template(
        "index.html",
        loaded_gifs=loaded_gifs,
        search_input=search_input)


def load_words():
    with open("random_words.txt", "r") as f:
        for word in f:
            random_words.append(word)


if __name__ == '__main__':
    load_words()
    app.run(debug=True)
