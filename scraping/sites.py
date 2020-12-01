"""
This file contains webscraping functions that are specific to certain websites
"""

def mtgtop8(soup):

    """
    Scrapes card names and quantities from tappedout.net and returns them as a dictionary.
    This function works in the test environment and scrapes data properly, but breaks when
    the data is sent to the Scryfall API. Fix later.
    :param soup:
    :return dict:
    """
    card_names = []
    card_quantities = []

    soup = soup.findAll("div", {"class": "hover_tr"})

    for tag in soup:

        if tag.getText()[0] != "\n":
            card_names.append(tag.getText()[2:].strip())
            card_quantities.append(int(tag.getText()[0:2].strip()))

        else:
            pass

    return dict(zip(card_names, card_quantities))



def tappedout(soup):

    """
    Scrapes card names and quantities from tappedout.net and returns them as a dictionary.
    :param soup:
    :return dict:
    """

    soup = soup.findAll("a", {"class": "qty board"})
    dct = {}
    for tag in soup:
        card_name = tag["data-name"]
        card_quantity = tag["data-qty"]
        dct[card_name] = int(card_quantity)

    return dct


def mtggoldfish(soup):

    """
    Scrapes card names and quantities from mtggoldfish.com and returns them as a dictionary.
    :param soup:
    :return dict:
    """

    name_soup = soup.findAll("a", {"rel": "popover"})
    quantity_soup = soup.findAll("td", {"class": "text-right"})

    card_names = []
    card_quantities = []

    for tag in name_soup:
        card_name = tag.getText()
        card_names.append(card_name)

    for tag in quantity_soup:

        try:
            quantity = int(tag.getText())
            card_quantities.append(quantity)

        except ValueError:
            pass

    return dict(zip(card_names, card_quantities))



