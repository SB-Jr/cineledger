from ledger.service import service
from ledger.interface import display_helper

# TODO: create a console setter to set a good looking console object

# TODO: improve -> use a single way which will be common for all command handler scipts
KEY = 'search'


# Flags
_MOVIE_ONLY = '--movie-only'
_TV_ONLY = '--tv-only'
_PERSON_ONLY = '--person-only'
# Arguments
QUERY = 'query'

SEARCH_KEY_DICT = {
    _MOVIE_ONLY :  [_MOVIE_ONLY, 'Search for movie only', 'store_true'],
    _TV_ONLY : [_TV_ONLY, 'Search for TV Shows only', 'store_true'],
    _PERSON_ONLY : [_PERSON_ONLY, 'Search for Personality only', 'store_true'],
    QUERY : ['query', 'The name of the Movie, Tv Show or Personality to search', 'store']
    # TODO: add a searched movie to wish list
    # TODO: add a searched movie to watch list
}

def add_search_parser(subparsers):
    search_parser = subparsers.add_parser(KEY, help='Search Movies, TvShows or Personalities')
    for key in SEARCH_KEY_DICT:
        value = SEARCH_KEY_DICT[key]
        search_parser.add_argument(value[0], help=value[1], action=value[2])

def handle_action(args):
    results = service.search_all(args[QUERY])
    display_helper.show_results(results)
    choice = display_helper.get_choice(results)
    _show_choice(choice)

def _show_choice(choice):
    imdb_info = service.get_imdb(choice.ids['ids']['imdb'], service.MOVIE)
    display_helper.show_choice(choice, imdb_info)