"""
This file contains webscraping functions that are specific to certain sites
"""

def mtgtop8(soup):


    """
    needs to be fixed
    :param soup:
    :return:
    """
    names = []
    numbers = []

    soup = soup.findAll("div", {"class": "hover_tr"})

    for tag in soup:

        if tag.getText()[0] != "\n":
            names.append(tag.getText()[2:].strip())
            numbers.append(int(tag.getText()[0:2].strip()))

        else:
            pass

    return dict(zip(names, numbers))



def tappedout(soup):

    soup = soup.findAll("a", {"class": "qty board"})
    dct = {}
    for el in soup:
        name = el["data-name"]
        qty = el["data-qty"]
        dct[name] = int(qty)

    return dct


def mtggoldfish(soup):
    soup1 = soup.findAll("td", {"class": "deck-col-qty"})
    soup2 = soup.findAll("td", {"class": "deck-col-card"})

    names = []
    nums = []

    for tag in soup2:
        card = tag.getText()
        card = card.strip("\n")
        names.append(card)

    for i in soup1:
        try:
            i = int(i.getText())
            nums.append(i)
        except ValueError:
            pass

    dct = dict(zip(names, nums))

    return dct

def moxfield(soup):

    soup1 = soup.findAll("a", {"class": "cursor-pointer text-body"})
    soup2 = soup.findAll("td", {"class": "text-right"})

    names = []
    nums = []

    for tag in soup1:
        card = tag.getText()
        names.append(card)

    for tag in soup2:
        number = tag.getText()
        nums.append(number)

    return dict(zip(names,nums))