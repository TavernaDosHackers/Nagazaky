#!/usr/bin/env python3

from abc import ABC


class Settings(ABC):
    def __init__(self):
        """ Constructor and Attributes. """
        # Specifications
        self.__authors = "Matheus (@blkz), Ygor Simões (@CR3DN3)"
        self.__version = "2.0-alpha"
        self.__github = "https://github.com/TavernaDosHackers/"
        self.__email = "contato@tavernadoshackers.com.br"

        # Update and Upgrade
        self.__api_repo = "https://api.github.com/repos/TavernaDosHackers/Nagazaky"
        self.__automatic_upgrades = True

    # Getters
    # Specifications
    @property
    def get_authors(self):
        return self.__authors

    @property
    def get_version(self):
        return self.__version

    @property
    def get_github(self):
        return self.__github

    @property
    def get_email(self):
        return self.__email
