import requests
from src.apimanager import apiendpoint
from src.apimanager import apifields
from src import settings


def __dispatch():
    request_url = apiendpoint.APIEndpoint().request_url
    return requests.get(request_url).json()


def __filter(card_pool, format_sets):
    cards = []
    for card in card_pool:
        if card[apifields.APICollectibleFields.SET] in format_sets.keys()\
                and card[apifields.APICollectibleFields.NAME] not in settings.BASIC_HEROES:
            cards.append(card)
    return cards


def standard_cards():
    return __filter(__dispatch(), settings.STANDARD_SETS)


def wild_cards():
    return __filter(__dispatch(), settings.WILD_SETS)


def wild_exclusive_cards():
    return __filter(__dispatch(), settings.WILD_EXCLUSIVE_SETS)


def arena_cards():
    cards = __filter(__dispatch(), settings.ARENA_SETS)
    for card in cards:
        if card[apifields.APICollectibleFields.NAME] in settings.ARENA_EXCLUSIONS:
            cards.remove(card)
    return cards


def adventure_cards():
    return __filter(__dispatch(), settings.ADVENTURES)


def expansion_cards():
    return __filter(__dispatch(), settings.EXPANSIONS)


def set_cards():
    pass
