from trakt import init
import trakt.core
import json
import os
from rich.console import Console


console = Console()

"""
This script takes care of the authentication for the user.
This needs to be called before carying on any other functionality.
"""


def _handle_existing_user(user_name, json_path):
    with open(json_path, 'r') as f:
            session_info = json.loads(f.read())
    trakt.core.OAUTH_TOKEN = session_info['OAUTH_TOKEN']
    trakt.core.CLIENT_ID = session_info['CLIENT_ID']
    trakt.core.CLIENT_SECRET = session_info['CLIENT_SECRET']
    console.print('Logged-in as User: {}'.format(user_name))


def _handle_new_user(user_name=None):
    trakt.core.AUTH_METHOD = trakt.core.OAUTH_AUTH
    if user_name is None:
        user_name = input('Enter your Trakt User name: ')
    trakt.init(user_name, store=True)

def auth_user(user_name=None):
    home_path = os.getenv('HOME')
    json_path = os.path.join(home_path, '.pytrakt.json')
    if os.path.exists(json_path):
        _handle_existing_user(user_name, json_path)
    else:
        _handle_new_user(user_name)