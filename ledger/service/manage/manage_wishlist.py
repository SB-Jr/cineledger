import trakt
from ledger.service.auth import get_user

def get_wishlist_movies():
    user = get_user()
    movies = user.watchlist_movies
    return movies