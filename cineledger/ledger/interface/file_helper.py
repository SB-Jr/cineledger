import json
from ledger.config import config

def store_wishlist(wishlist):
    file_location = config.get_wishlist_location()
    with open(file_location, 'w') as file:
        data = [(media.title, media.ids['ids']['imdb'], media.ids['ids']['trakt']) for media in wishlist]
        data_json = json.dumps(data)
        file.writelines(data_json)

def store_watchedlist(watchedlist):
    file_location = config.get_watched_list()
    with open(file_location, 'w') as file:
        data = [media.ids['ids']['trakt'] for media in watchedlist]
        data_json = json.dumps(data)
        file.writelines(data_json)