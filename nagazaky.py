#!/usr/bin/env python3

"""
ATTENTION! We recommend installing the script before you even run this script.
Read carefully the steps to install: https://github.com/TavernaDosHackers/Nagazaky/blob/master/README.md
"""

from nagazaky.core.color import Color
from nagazaky import __main__

import sys
import asyncio
from platform import python_version

if __name__ == "__main__":
    # Verify python version
    if python_version()[0:3] < "3.7":
        Color.println("{!} Make sure you have Python 3.7+ installed, quitting.\n")
        sys.exit()

    # Start Nagazaky
    __main__.entry_point()
