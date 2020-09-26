#!/usr/bin/env python3

"""
This is the CLI main handling script.
This script parses the arguments and calls all other functionality required.
                            
                             [output]                                       
                                    
[ledger] ------> [interface]  <----->  [service]
                                       
                              [config]

ledger: Starting point of CineLedger
inerface: get the information provided by "service", get's user configuration from "config" and outputs accordingly
service: handles the rest calls to get information from various sources
config: handles the user configuration
"""

from ledger.interface import handle_command
from ledger.service import auth

if __name__ == "__main__":
    auth.authenticate_user('shrijit')
    handle_command()