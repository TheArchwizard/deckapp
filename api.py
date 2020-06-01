import flask
from deck_app import deck_scraper

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/scrape/<path:url>', methods=["GET"])
def scrape(url):

    return deck_scraper.main_app(url)
@app.route('/')
def home():
    return "<h1> Welcome </h1>"

app.run()
