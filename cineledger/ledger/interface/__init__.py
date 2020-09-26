"""
This is the interface which handles the user interaction and shows the appropriate results to the user.
Handles the action that needs to take place depending on the user's arguments passed. 
"""

import argparse
from ledger.interface import search_interface
from ledger.interface import manage_interface


_SUBCOMMAND = 'subcommand'
_interfaces = {
    search_interface.KEY: search_interface,
    manage_interface.KEY: manage_interface
}

def handle_command():
    args = _parse_arguments()
    _perform_action(args)

def _get_paser():
    parser = argparse.ArgumentParser(prog='ledger')
    subparsers = parser.add_subparsers(title='Commands', dest = _SUBCOMMAND)
    search_interface.add_search_parser(subparsers)
    manage_interface.add_tracker_parser(subparsers)    
    return parser

def _parse_arguments():
    parser = _get_paser()
    args = parser.parse_args()
    return vars(args)

def _perform_action(args):
    # TODO: use *list* of command handlers and pass the args to command handler based subcommand value
    # TODO: do not use if else  
    if args[_SUBCOMMAND] is None:
        # TODO: handle help
        exit()
    _interfaces[args[_SUBCOMMAND]].handle_action(args)