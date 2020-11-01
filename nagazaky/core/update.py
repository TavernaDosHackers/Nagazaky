#!/usr/bin/env python3

"""
MIT License

Copyright (c) 2020 Taverna dos Hackers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import os
from requests import get

from nagazaky.core.settings import Settings
from nagazaky.core.color import Color


class Update(Settings):
    def __init__(self):
        """ Constructor and Attributes. """
        super().__init__()

    def verify(self) -> None:
        """ Checks for updates to update versions. """
        # Make a request for the repository version.
        req_repository = get(self.get_repository).json()
        repository_version = req_repository["specifications"]["version"]

        # Checks whether the repository version is different from the current version.
        if repository_version != self.get_version:
            Color.println("{+} New version available: {G}%s{W}" % repository_version)

    def upgrade(self) -> None:
        """ Updates Nagazaky to the most current version available. """
        # Checks for the .git directory
        if not os.path.exists("../../.git"):
            Color.println("{!} Not a git repository.")
            Color.println("{+} It is recommended to clone the 'TavernaDosHackers/Nagazaky' repository from GitHub ("
                          "'git clone %sNagazaky')" % self.get_github)
            sys.exit()

        # Try to update Nagazaky
        try:
            Color.println("{+} Updating...")
            os.system(f"git pull {self.get_github}Nagazaky")
            Color.println("{+} Nagazaky was successfully updated.")
        except Exception as e:
            Color.exception("Could not update.", e)


if __name__ == "__main__":
    update = Update()
    update.upgrade()
