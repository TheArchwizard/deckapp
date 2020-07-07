import flask
from .deck_scraper import *
from flask_cors import CORS


app = flask.Flask(__name__)
app.config["DEBUG"] = False
CORS(app)

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


@app.route("/dict/<string:dct>", methods=["GET"])
def dict_to_blob(dct):

    return create_json_blob(dct)

@app.route("/scrape/<path:url>", methods=["GET"])
def scrape_all(url):
    return main_app(url)
@app.route("/")
def home():
    return "<h1> Welcome </h1>"

if __name__ == '__main__':
    app.run()
