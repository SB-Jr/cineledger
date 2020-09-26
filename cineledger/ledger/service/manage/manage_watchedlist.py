import trakt
from ledger.service.auth import get_user

def get_watchedlist_movies():
    user = get_user()
    movies = user.watched_movies
    return movies