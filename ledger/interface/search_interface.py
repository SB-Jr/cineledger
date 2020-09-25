from rich.console import Console
from rich.table import Table
from rich import box
from rich.progress import track
from ledger.service import service
from ledger.interface import display_helper

# TODO: create a console setter to set a good looking console object
console  = Console()

# TODO: improve -> use a single way which will be common for all command handler scipts
KEY = 'search'
# Flags
MOVIE_ONLY = '--movie-only'
TV_ONLY = '--tv-only'
PERSON_ONLY = '--person-only'
# Arguments
QUERY = 'query'

SEARCH_KEY_DICT = {
    MOVIE_ONLY :  ['--movie-only', 'Search for movie only', 'store_true'],
    TV_ONLY : ['--tv-only', 'Search for TV Shows only', 'store_true'],
    PERSON_ONLY : ['--person-only', 'Search for Personality only', 'store_true'],
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
    show_results(results)
    choice = get_choice(results)
    show_choice(choice)


def show_choice(choice):
    # TODO: improve -> maybe shift to a different place where only prints are handled
    imdb_info = service.get_imdb(choice.ids['ids']['imdb'], service.MOVIE)
    console.print('Name: ' + choice.title)
    console.print('Genres: ' + str(imdb_info.get('genres')))
    console.print('Director: '+ imdb_info.get('director')[0].get('name'))
    console.print('Runtime: '+ imdb_info.get('runtimes')[0] + 'min')
    console.print('Year: ' + str(imdb_info.get('year')))
    console.print('IMDb Rating: '+ str(imdb_info.get('rating')))
    console.print('Trakt Rating: ' + str(choice.ratings['rating']))

def show_results(results):
    display_helper.show_results(results)

def get_choice(results):
    # TODO: improve -> maybe shift to a different place where only choices are handled
    if len(results) == 1:
        return results[0]
    else:
        while(True):
            choice_index = input('Enter your choice(q to quit): ')
            if choice_index == 'q':
                exit()
            if not choice_index.isdigit():
                console.print('This is not a number!\nEnter a valid Number....')
                continue
            else:
                choice_index = int(choice_index)
            if choice_index <= len(results) and choice_index > 0:
                return results[choice_index-1]
            else:
                console.print('Numer is invalid!! \nPlease enter a valid number....')