import flask
from deck_app.scraping import deck_scraper

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route("/names/<path:url>", methods=["GET"])
def print_deck(url):
    return deck_scraper.return_deck(url)


@app.route("/scrape/<path:url>", methods=["GET"])
def scrape_all(url):
    return deck_scraper.main_app(url)
@app.route('/')
def home():
    return "<h1> Welcome </h1>"

if __name__ == '__main__':
    app.run()
