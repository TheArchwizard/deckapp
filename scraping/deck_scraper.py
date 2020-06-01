from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
from .sites import *



"""
print("Name: " + card.name())
print("Number in deck: " + str(d[i]))
print("Typeline: " + card.type_line())
print("Converted mana cost: " + str(card.cmc()))
print("\n")
print("--- %s seconds ---" % (time.time() - start))
plt.figure(figsize=(8, 5))
plt.pie(d.values(), labels=list(d.keys()), autopct="%.1f%%")
plt.show()

"""

class Card:

    def __init__(self,name,type_line,cmc):
        self.name = name
        self.type_line = type_line
        self.cmc = cmc

    def print_card(self):
        print("{}, {}, {}".format(self.name,self.type_line,self.cmc))

    def return_card(self):
        return "{}, {}, {}".format(self.name,self.type_line,self.cmc)

def chunk(d):
    lists = []
    newlist = []
    dictlst = list(d.keys())
    for i in range(0,len(dictlst)):

        if i != 0 and i % 75 == 0:
            lists.append(newlist)
            newlist = []
            lists.append(newlist)

        newlist.append(dictlst[i])


    return lists


def post_request(jsonblob):

    api_url = "https://api.scryfall.com/cards/collection"
    response = requests.post(api_url, json=jsonblob)

    if response.status_code == 200:
        print(json.loads(response.content.decode("utf-8")))
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

def create_json_blob(d_or_l):

    card_names = list(d_or_l)
    jsonblob = {}

    list_of_dicts = []
    for i in range(0, len(card_names)):
        d1 = {}
        d1["name"] = card_names[i]
        list_of_dicts.append(d1)
    jsonblob["identifiers"] = list_of_dicts
    print(jsonblob)
    return jsonblob


def return_big_deck(jsonblob):

    for i in range(1, len(jsonblob)):
        jsonblob[0]["data"].extend(jsonblob[i]["data"])

    return jsonblob[0]

def json_to_deck(jsonblob):

    deck = []

    for i in jsonblob["data"]:

        c = Card(i["name"], i["type_line"], i["cmc"])
        deck.append(c)
        c.print_card()


def picksite(url, soup):

    url_dct = {1: "mtgtop8.com/event", 2: "tappedout.net/mtg-decks", 3: "mtggoldfish.com"}

    if url_dct[1] in url:
        return mtgtop8(soup)

    elif url_dct[2] in url:
        return tappedout(soup)

    elif url_dct[3] in url:
        return mtggoldfish(soup)
    else:
        print("Unrecognized deck url.")


def main_app(url):

    try:
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        dct = picksite(url, soup)

        if len(dct) > 75:
            lsts = chunk(dct)
            lstofblobs = []
            for lst in lsts:

                json_blob = create_json_blob(lst)
                json_blob = post_request(json_blob)
                lstofblobs.append(json_blob)
            return return_big_deck(json_blob)

        else:
            json_blob = create_json_blob(dct)
            json_blob = post_request(json_blob)

            return json_blob

    except ValueError:
        print("Invalid url.")

def test():


    try:
        url = input("Enter a url: ")
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        dct = picksite(url, soup)


        if len(dct) > 75:
            lsts = chunk(dct)
            lstofblobs = []
            for lst in lsts:

                json_blob = create_json_blob(lst)
                json_blob = post_request(json_blob)
                lstofblobs.append(json_blob)
            return return_big_deck(json_blob)

        else:
            json_blob = create_json_blob(dct)
            json_blob = post_request(json_blob)

            return json_blob

    except ValueError:
        print("Invalid url.")


