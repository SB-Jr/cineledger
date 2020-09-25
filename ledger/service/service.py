"""
Handles the information fetching from different sources and passes back to the interface for showcasing the info fetched. Processes the information if the information needs combining or splitting.
"""

from trakt.movies import Movie
from trakt.tv import TVShow
from trakt.sync import search
from imdb import IMDb

imdb_client = IMDb()

__all__ = ['MOVIE', 'TVSHOW', 'PERSONALITY']

MOVIE = 'MOVIE'
TVSHOW = 'TVSHOW'
PERSONALITY = 'PERSONALITY'

def search_all(query: str, search_type=['movie', 'show', 'people']):
    results = search(query=query, search_type=search_type, slugify_query=True)
    return results

def search_movie_only(query: str):
    return search_all(query, ['movie'])

def search_tv_shows_only(query: str):
    return search_all(query, ['show'])


def get_imdb(id: str, type):
    id  = int(id[2:])
    if type == MOVIE or type == TVSHOW:
        return imdb_client.get_movie(id)
    elif type == PERSONALITY:
        return imdb_client.get_person(id)

# TODO: get rottentomatoes and other ratings
def get_rotten_tomatoes(id: int):
    pass