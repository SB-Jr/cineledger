

KEY = 'manage'

def add_tracker_parser(subparsers):
    movie_tracker_parser = subparsers.add_parser(KEY, help='Manage your wishlist and watchlist')


def handle_action(args):
    pass