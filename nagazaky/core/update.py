#!/usr/bin/env python3

from nagazaky.core.settings import Settings


class Update(Settings):
    def __init__(self):
        """ Constructor and Attributes. """
        super().__init__()

    def verify(self):
        """ Checks for updates to update versions. """
        pass

    def upgrade(self):
        """ Updates Nagazaky to the most current version available. """
        pass


if __name__ == "__main__":
    update = Update()
    update.verify()
    update.upgrade()
