#!/usr/bin/env python3

try:
    from nagazaky.core.color import Color
    from nagazaky.core.banner import Banner
    from nagazaky.core.update import Update
    from nagazaky.core.args import Arguments

    from requests import get
except (ValueError, ImportError) as ex:
    Color.exception("Error", ex)
except Exception as ex:
    Color.exception("Unknown exception error", ex)


class Nagazaky:
    def __init__(self):
        """ Constructor and Attributes. """
        self.args = Arguments().args
        self.banner = Banner()
        self.update = Update()

    def run(self):
        """ Method that starts Nagazaky. """
        if self.args.no_banner is False:
            self.banner.print_logo()


if __name__ == "__main__":
    pass
