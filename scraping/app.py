from flask import render_template, request, Flask, redirect
from .deck_scraper import *
from flask_cors import CORS


app = Flask(__name__)
app.config["DEBUG"] = False
CORS(app)

@app.route("/names/<path:url>", methods=["GET"])
def names_nums(url):

    deck = names_dct(url)
    jsondct = {}
    lst = []

    for name,quantity in deck.items():
        dct = {}
        dct["name"] = name
        dct["num"] = str(quantity)
        lst.append(dct)

    jsondct["values"] = lst
    return jsondct

@app.route("/upload-file", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":

        if request.files:

            file = request.files["text"]

            return redirect("index.html")




@app.route("/dict/<string:dct>", methods=["GET"])
def dict_to_blob(dct):

    return create_json_blob(dct)

@app.route("/scrape/<path:url>", methods=["GET"])
def scrape_all(url):
    return main_app(url)
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
