#!/usr/bin/env python3

"""
This is the CLI main handling script.
This script parses the arguments and calls all other functionality required.
TODO: Handle Config
"""

from auth import auth_user
from ledger.interface import interface

if __name__ == "__main__":
    auth_user('shrijit')
    args = interface.parse_arguments()
    interface.perform_action(args)