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

import json
import os
from requests import get
from abc import ABC

from nagazaky.core.color import Color


class Settings(ABC):
    def __init__(self):
        """ Constructor and Attributes. """
        # Load archive config.json
        self.__config_json = open(os.path.realpath("nagazaky/core/config.json"), "r")
        self.__config_json = str(self.__config_json.read())
        self.__config_json = json.loads(self.__config_json)

        # Specifications
        self.__authors = self.__config_json["specifications"]["author"]
        self.__version = self.__config_json["specifications"]["version"]
        self.__github = self.__config_json["specifications"]["github"]
        self.__email = self.__config_json["specifications"]["email"]

        # Update and Upgrade
        self.__api_repository = self.__config_json["update"]["api_repository"]
        self.__automatic_upgrades = bool(self.__config_json["update"]["automatic_upgrades"])

    @staticmethod
    def get_user_agent(user_agent):
        pass

    @staticmethod
    def get_proxy(proxy: str or None) -> dict:
        """ Generate an automatic proxy through an API or format a pre-set proxy. """

        # Make a request in the proxy API and format accordingly.
        if proxy is None:
            while True:
                request_api_proxy = get("https://www.proxyscan.io/api/proxy?format=json&level=elite,"
                                        "anonymous&type=https,http&ping=100").json()
                status_proxy = request_api_proxy[0]["Location"]["status"]

                if status_proxy != "error" and status_proxy != "fail" and status_proxy != "None":
                    break

            protocol = request_api_proxy[0]["Type"][0].lower()
            port = request_api_proxy[0]["Port"]
            ip = request_api_proxy[0]["Ip"] + ":" + str(port)
            proxy = {protocol: ip}

        # Formats the selected proxy accordingly.
        else:
            if proxy[:4] == "http":
                protocol = "http"
                proxy = {protocol: proxy}
            elif proxy[:5] == "https":
                protocol = "https"
                proxy = {protocol: proxy}
            elif proxy[:3] == "ftp":
                protocol = "ftp"
                proxy = {protocol: proxy}
            else:
                proxy = ""

        # Prints the selected proxy on the screen.
        for key, value in proxy.items():
            key_value = key + "://" + value
            Color.println("{+} Proxy: %s" % key_value)

        # Returns the selected proxy in the dictionary.
        return proxy

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
        return self.__api_repository

    @property
    def get_automatic_upgrades(self) -> bool:
        return self.__automatic_upgrades


if __name__ == "__main__":
    pass
