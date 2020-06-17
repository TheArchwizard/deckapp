import flask
from .deck_scraper import *



app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route("/names/<path:url>", methods=["GET"])
def names_nums(url):

    deck = names_dct(url)
    jsondct = {}
    lst = []

    for k,v in deck.items():
        dct = {}
        dct["name"] = k
        dct["num"] = str(v)
        lst.append(dct)

    jsondct["values"] = lst
    print(jsondct)
    return jsondct

@app.route("/scrape/<path:url>", methods=["GET"])
def scrape_all(url):
    return main_app(url)
@app.route("/")
def home():
    return "<h1> Welcome </h1>"

if __name__ == '__main__':
    app.run()
