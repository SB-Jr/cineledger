"""
Command Structure
ledger manage [wish|watch] [-m|-s] [--genre [genre-list], --rate rating, --cast personality-name]

ledger manage wish -m
ledger manage watch -m
ledger manage wish -s
ledger manage watch -s

ledger manage wish -m --genre horror
ledger manage wish -m --genre suspense horror
ledger manage wish -m --rate 8
ldeger manage wish -m --cast christopher-nolan
"""

from ledger.service.manage import manage_wishlist
from ledger.service.manage import manage_watchedlist
from ledger.interface import display_helper
from ledger.interface import file_helper

KEY = 'manage'

def add_tracker_parser(subparsers):
    movie_tracker_parser = subparsers.add_parser(KEY, help='Manage your wish-list and watched-list')
    # TODO: add argument to save the wishhlist into a file for offline management
    # TODO: add flag to filter genres from wish list
    # TODO: same for watched list
    for subcmd in _SUBCOMMANDS:
        movie_tracker_parser.add_argument(subcmd[0], **subcmd[1])
    for flag in _FLAGS:
        movie_tracker_parser.add_argument(*flag[0], **flag[1])

def handle_action(args):
    print(args)
    _command_handler[args[_COLLECTION_TYPE]](args)
        

def _wishlist_interface(args):
    wishlist = manage_wishlist.get_wishlist_movies()
    if args[_STORE_FLAG]:
        file_helper.store_wishlist(wishlist)
    else:
        display_helper.show_results(wishlist, mutliple=True)

def _watchedlist_interface(args):
    watched = manage_watchedlist.get_watchedlist_movies()
    if args[_STORE_FLAG]:
        file_helper.store_watchedlist(watched)
    else:
        display_helper.show_results(watched, mutliple=True)


# subcommands
_WATCHED_LIST = 'watched'
_WISH_LIST = 'wish'
# data types
_COLLECTION_TYPE = 'collection type'
_MEDIA_TYPE = 'media type'
_SUBCOMMANDS = [
    [ 
        _COLLECTION_TYPE, {
            'help':'Which collection out of watched/wish you would like to manage', 
            'choices': ['wish', 'watched']
            }
    ],
    [
        _MEDIA_TYPE, {
            'help': 'Which media type out of movie/series/all you would like to manage', 
            'choices': ['movie', 'series', 'all'],
            'nargs': '?',
            'default': 'movie'
        }
    ]
]
#flags
_RATE_FLAG = '--rate'
_GENRE_FLAG = '--genre'
_PERSONALITY_FLAG = '--personality'
_STORE_FLAG = '--store'
_FLAGS = [
    [
       [_RATE_FLAG], {
            'dest': _RATE_FLAG,
            'help': 'Filter based on the rating of the media',
            'action': 'store'
            }
    ],
    [
        [_GENRE_FLAG], {
            'dest': _GENRE_FLAG,
            'help': 'Filter based on the genre of the media',
            'nargs': '*',
            'action': 'extend'
            }
    ],
    [
        [_PERSONALITY_FLAG], {
            'dest': _PERSONALITY_FLAG,
            'help': 'Filter based on a specific personality present in the crew of the media',
            'nargs': '*',
            'action': 'extend'
            }
    ],
    [
        [_STORE_FLAG], {
            'dest': _STORE_FLAG,
            'help': 'Store the data into a file',
            'action': 'store_true'
            }
    ]
]

_command_handler = {
    _WISH_LIST: _wishlist_interface,
    _WATCHED_LIST: _watchedlist_interface
}