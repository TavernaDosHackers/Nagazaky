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
import subprocess

from nagazaky.core.settings import Settings
from nagazaky.core.request import Request
from nagazaky.core.color import Color


class Update(Settings):
    def __init__(self, request: Request):
        """ Constructor and Attributes. """
        super().__init__()
        self.request = request

    def verify(self, arg_update: bool) -> bool:
        """ Checks for updates to update versions. """
        # Make a request for the repository version.
        req_repository = self.request.get(self.get_repository).json()
        repository_version = req_repository["specifications"]["version"]

        # Checks whether the repository version is different from the current version.
        if repository_version != self.get_version:
            Color.println("\n{+} New version available: {G}%s{W}" % repository_version)
            return True
        else:
            if arg_update:
                Color.println("\n{+} Congratulations, you are already using the latest version available.")
                sys.exit()

    def upgrade(self) -> None:
        """ Updates Nagazaky to the most current version available. """
        # Checks for the .git directory
        if not os.path.exists(os.path.realpath(".git")):
            Color.println("{!} Not a git repository.")
            Color.println("{+} It is recommended to clone the 'TavernaDosHackers/Nagazaky' repository from GitHub ("
                          "'git clone %sNagazaky')" % self.get_github)
            sys.exit()

        # Try to update Nagazaky
        output = ""
        try:
            Color.println("{+} Updating...")
            process = subprocess.Popen(f"git checkout . && git pull {self.get_github}Nagazaky", shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = process.communicate()
            Color.println("{+} Nagazaky was successfully updated.")
            Color.println("{+} Check the new release notes at: {"
                          "G}https://github.com/TavernaDosHackers/Nagazaky/commits/master{W}")
        except Exception as e:
            Color.exception("Could not update.", e)
