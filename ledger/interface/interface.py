"""
This is the interface which handles the user interaction and shows the appropriate results to the user.
Handles the action that needs to take place depending on the user's arguments passed. 
"""
# TODO: transfer the file to __init__

import argparse
from ledger.interface import search_interface
from ledger.interface import manage_interface
from rich.console import Console

console = Console() 

def handle_command():
    args = _parse_arguments()
    _perform_action(args)

def _get_paser():
    parser = argparse.ArgumentParser(prog='ledger')
    subparsers = parser.add_subparsers(title='Commands', dest = 'subcommand')
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
    if args['subcommand'] is None:
        # TODO: handle help
        exit()
    if search_interface.KEY == args['subcommand']:
        search_interface.handle_action(args)
    elif manage_interface.KEY in args['subcommand']:
        manage_interface.handle_action(args)