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

from nagazaky.core.settings import Settings
import argparse


class Arguments(Settings):
    def __init__(self):
        super().__init__()
        parser = argparse.ArgumentParser(usage="python3 nagazaky.py",
                                         add_help=False)

        parser.add_argument("-h", "--help",
                            action="store_true",
                            help="Show this help message and exit")

        parser.add_argument("-u", "--url",
                            action="store",
                            type=str,
                            default=None,
                            help="Target URL (http://www.site_target.com/)")

        parser.add_argument("--user-agent",
                            action="store",
                            type=str,
                            default=self.get_user_agent(),
                            help="Customize the User-Agent. Default: Random User-Agent")

        parser.add_argument("--update",
                            action="store_true",
                            default=self.automatic_upgrades,
                            help="Update Nagazaky to the latest version available")

        parser.add_argument("--no-banner",
                            action="store_true",
                            default=False,
                            help="Disable the initial banner")

        self.args = parser.parse_args()


if __name__ == "__main__":
    arguments = Arguments()
    print(arguments.args)
