#!/usr/bin/env python3

"""
This is the CLI main handling script.
This script parses the arguments and calls all other functionality required.
TODO: Handle Config
"""

from ledger.interface import handle_command
from ledger.service import auth

if __name__ == "__main__":
    auth.authenticate_user('shrijit')
    handle_command()