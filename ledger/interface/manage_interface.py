from rich.console import Console
from ledger.service.manage import manage_wishlist
from ledger.interface import display_helper

KEY = 'manage'
console = Console()

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

# subcommands
WATCHED_LIST = 'watched'
WISH_LIST = 'wish'
COLLECTION_TYPE = 'collection type'
MEDIA_TYPE = 'media type'
SUBCOMMANDS = [
    [ 
        COLLECTION_TYPE, {
            'help':'Which collection out of watched/wish you would like to manage', 
            'choices': ['wish', 'watched']
            }
    ],
    [
        MEDIA_TYPE, {
            'help': 'Which media type out of movie/series/all you would like to manage', 
            'choices': ['movie', 'series', 'all'],
            'nargs': '?',
            'default': 'movie'
        }
    ]
]
RATE_FLAG = 'rate'
GENRE_FLAG = 'genre'
PERSONALITY_FLAG = 'personality'
FLAGS = [
    [
       ['-r',  '--rate'], {
            'dest': RATE_FLAG,
            'help': 'Filter based on the rating of the media',
            'action': 'store'
            }
    ],
    [
        ['-g', '--genre'], {
            'dest': GENRE_FLAG,
            'help': 'Filter based on the genre of the media',
            'nargs': '*',
            'action': 'extend'
            }
    ],
    [
        ['-c', '--crew'], {
            'dest': PERSONALITY_FLAG,
            'help': 'Filter based on a specific personality present in the crew of the media',
            'nargs': '*',
            'action': 'extend'
            }
    ]
]

def add_tracker_parser(subparsers):
    movie_tracker_parser = subparsers.add_parser(KEY, help='Manage your wish-list and watched-list')
    # TODO: add argument to save the wishhlist into a file for offline management
    # TODO: add argument to get show 10 movies from wishlist at a time from the offline file, take input to show next 10 movies
    # TODO: add flag to filter genres from wish list
    # TODO: same for watched list
    for subcmd in SUBCOMMANDS:
        movie_tracker_parser.add_argument(subcmd[0], **subcmd[1])
    for flag in FLAGS:
        movie_tracker_parser.add_argument(*flag[0], **flag[1])

def _show_wishlist(wishlist):
    limit = 10
    counter = 0
    while True:
        wishlist_trunc = wishlist[counter*limit : (counter+1)*limit]
        display_helper.show_results(wishlist_trunc)
        cont = input('Press Enter to print next 10 media else enter q: ')
        if cont == 'q':
            exit()
        counter +=1


def handle_action(args):
    console.print(args)
    collection_type = args[COLLECTION_TYPE]
    media_type = args[MEDIA_TYPE]
    if args[COLLECTION_TYPE] == WISH_LIST:
        _show_wishlist(manage_wishlist.get_wishlist_movies())