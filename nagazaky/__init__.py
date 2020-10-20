#!/usr/bin/env python3

try:
    from nagazaky.core.color import Color
    from nagazaky.core.banner import Banner
    from nagazaky.core.update import Update

    from requests import get
except (ValueError, ImportError) as ex:
    Color.exception("Error", ex)
except Exception as ex:
    Color.exception("Unknown exception error", ex)


class Nagazaky:
    def __init__(self):
        """ Constructor and Attributes. """
        self.banner = Banner()
        self.update = Update()

    def run(self):
        """ Method that starts Nagazaky. """
        self.banner.print_sub_banner()
