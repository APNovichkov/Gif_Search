from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    search_input = request.args.get('search_input')
    print("search_input: " + str(search_input))
    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template(
        "index.html",
        search_input=search_input)


if __name__ == '__main__':
    app.run(debug=True)
