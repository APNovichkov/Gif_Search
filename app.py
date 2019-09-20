from flask import Flask, render_template, request
import requests
import json
from random import choice

app = Flask(__name__)

random_words = []
#load list of random for random button 
def load_words():
    with open("random_words.txt", "r") as f:
        for word in f:
            random_words.append(word)


load_words()

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    search_input = request.args.get('search_input')
    top_10_input = request.args.get('top_10')
    random_input = request.args.get('random')

    # TODO: Make 'params' dict with query term and API key
    search_params = {
        "key": "XE9GOKSZYLQB",
        "q": search_input,
        "limit": 9
    }

    top_10_params = {
        "key": "XE9GOKSZYLQB",
        "limit": 9
    }

    random_params = {
        "key": "XE9GOKSZYLQB",
        "q": choice(random_words),
        "limit": 9
    }
    # TODO: Make an API call to Tenor using the 'requests' library

    search_request = requests.get("https://api.tenor.com/v1/search", params=search_params)
    top_10_request = requests.get("https://api.tenor.com/v1/trending", params=top_10_params)
    random_request = requests.get("https://api.tenor.com/v1/random", params=random_params)
    
    # TODO: Get the results from the search or use of the buttons
    loaded_gifs = None
    keyword = None

    if top_10_input == "true":
        loaded_gifs = json.loads(top_10_request.content)
        keyword = "Top Trending"
        print("loading top 10")
    elif random_input == "true":
        loaded_gifs = json.loads(random_request.content)
        keyword = random_params['q']
        print("loading random")
    elif search_request.status_code != 200 or len(search_request.content) == 0:
        loaded_gifs = json.loads(top_10_request.content)
        keyword = "Top Trending"
        print("loading top 10 because code != 200 or no gifs could be found")
    else:
        loaded_gifs = json.loads(search_request.content)
        keyword = search_input
        print("loading search results")

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template(
        "index.html",
        loaded_gifs=loaded_gifs,
        search_input=search_input,
        keyword=keyword)


if __name__ == '__main__':
    app.run(debug=True)
