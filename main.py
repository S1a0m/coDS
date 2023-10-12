#!/bin/python3
import sys

import coDS_variables
import coDS_functions

try:
    print(coDS_variables.welcome)                   # welcome
    coDS_functions.main_co()                        # treatment
    print("\nBye")
except KeyboardInterrupt:
    print("\n\nExit")
    sys.exit()
