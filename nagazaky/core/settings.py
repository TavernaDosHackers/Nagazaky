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

from abc import ABC
import json


class Settings(ABC):
    def __init__(self):
        """ Constructor and Attributes. """
        # Load archive config.json
        self.__config = open("config.json", "r")
        self.__config = str(self.__config.read())
        self.__config = json.loads(self.__config)

        # Specifications
        self.__authors = self.__config["specifications"]["author"]
        self.__version = self.__config["specifications"]["version"]
        self.__github = self.__config["specifications"]["github"]
        self.__email = self.__config["specifications"]["email"]

        # Update and Upgrade
        self.__repository = self.__config["update"]["repository"]
        self.__automatic_upgrades = self.__config["update"]["automatic_upgrades"]

    # Getters
    # Specifications
    @property
    def get_authors(self) -> str:
        return self.__authors

    @property
    def get_version(self) -> str:
        return self.__version

    @property
    def get_github(self) -> str:
        return self.__github

    @property
    def get_email(self) -> str:
        return self.__email

    # Update and Upgrade
    @property
    def get_repository(self) -> str:
        return self.__repository

    @property
    def automatic_upgrades(self) -> bool:
        return self.__automatic_upgrades


if __name__ == "__main__":
    pass
