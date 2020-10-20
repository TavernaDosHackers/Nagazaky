#!/usr/bin/env python3

from nagazaky.core.settings import Settings


class Banner(Settings):
    def __init__(self):
        """ Constructor and Attributes. """
        super().__init__()

    def print(self):
        """ Print the banner without specifications. """
        pass

    def print_sub_banner(self):
        """ Print the banner with specifications. """
        pass


if __name__ == "__main__":
    pass
