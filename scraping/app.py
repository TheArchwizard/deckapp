import flask
from .deck_scraper import main_app

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/scrape/<path:url>', methods=["GET"])
def scrape(url):
    return main_app(url)
@app.route('/')
def home():
    return "<h1> Welcome </h1>"

if __name__ == '__main__':
    app.run()
