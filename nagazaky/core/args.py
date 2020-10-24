#!/usr/bin/env python3

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
