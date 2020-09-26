import os

_WISHLIST='wishlist'
_WATCHEDLIST='watchedlist'
_HOME = os.path.join(os.getenv('HOME'),'.config/cineledger')
DEFAULT_LOCATION = {
    _WISHLIST: os.path.join(_HOME, _WISHLIST+'.json'),
    _WATCHEDLIST: os.path.join(_HOME, _WATCHEDLIST+'.json')
}

def get_wishlist_location():
    return DEFAULT_LOCATION[_WISHLIST]

def get_watched_list():
    return DEFAULT_LOCATION[_WATCHEDLIST]