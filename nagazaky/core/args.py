#!/usr/bin/env python3

import argparse


class Arguments:
    def __init__(self):
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

        parser.add_argument("--no-banner",
                            action="store_true",
                            default=False,
                            help="Disable the initial banner")

        self.args = parser.parse_args()


if __name__ == "__main__":
    arguments = Arguments()
    print(arguments.args)
