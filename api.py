import flask
from deck_app import deck_scraper

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/<path:url>', methods=["GET"])
def main(url):

    return deck_scraper.main_app(url)

app.run()
