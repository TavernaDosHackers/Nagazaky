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
import pathlib
import random

from abc import ABC
from requests import get

from nagazaky.core.color import Color


class Settings(ABC):
    def __init__(self):
        """ Constructor and Attributes. """

        # Load archive config.json
        self.path_dir = pathlib.Path("../../")
        dir_config_json = self.path_dir.glob("**/config.json")
        for dir_file in dir_config_json:
            with open(os.path.realpath(dir_file)) as file_config_json:
                self.__config_json = json.load(file_config_json)

        # Specifications
        self.__authors = self.__config_json["specifications"]["author"]
        self.__version = self.__config_json["specifications"]["version"]
        self.__github = self.__config_json["specifications"]["github"]
        self.__email = self.__config_json["specifications"]["email"]

        # Update and Upgrade
        self.__api_repository = self.__config_json["update"]["api_repository"]
        self.__automatic_upgrades = bool(self.__config_json["update"]["automatic_upgrades"])

    @staticmethod
    def target(url):
        """ Format the target URL accordingly. """
        if url[:7] != "http://" and url[:8] != "https://":
            url = "http://" + url
        if url[-1] != "/":
            url = url + "/"
        return url

    @staticmethod
    def target_simple(url):
        """ Format the target URL as simple. """
        if url[:7] == "http://":
            url = url.replace("http://", "")
        elif url[:8] == "https://":
            url = url.replace("https://", "")
        if url[-1] == "/":
            url = url.replace("/", "")
        return url

    @staticmethod
    def get_user_agent(user_agent: str or None) -> dict:
        """ Generate an automatic User-Agent or format a predefined agent. """

        if user_agent is None:
            # Generate an automatic User-Agent
            repo_url_agents = "https://raw.githubusercontent.com/TavernaDosHackers/Nagazaky/master/extras/user-agents/"
            agents_chrome = get(repo_url_agents + "chrome.txt").text
            agents_edge = get(repo_url_agents + "edge.txt").text
            agents_firefox = get(repo_url_agents + "firefox.txt").text
            agents_opera = get(repo_url_agents + "opera.txt").text
            agents_safari = get(repo_url_agents + "safari.txt").text

            agents = agents_chrome + agents_edge + agents_firefox + agents_opera + agents_safari
            user_agent = random.choice(agents.splitlines())
            user_agent = {"User-Agent": user_agent}

        else:
            # Format a predefined agent.
            user_agent = {"User-Agent": user_agent}

        # Returns the random User-Agent.
        return user_agent

    @staticmethod
    def get_proxy(proxy: str or None) -> dict or None:
        """ Generate an automatic proxy through an API or format a pre-set proxy. """

        # Make a request in the proxy API and format accordingly.
        if proxy == "auto":
            Color.println("\n{!} BETA - The automatic proxy function may cause Nagazaky not to work as expected.")

            while True:
                api_proxy = "https://www.proxyscan.io/api/proxy?format=json&&type=https,http&ping=25"
                request_api_proxy = get(api_proxy).json()
                status_proxy = request_api_proxy[0]["Location"]["status"]

                if status_proxy != "error" and status_proxy != "fail" and status_proxy != "None":
                    break

            protocol = request_api_proxy[0]["Type"][0].lower()
            port = request_api_proxy[0]["Port"]
            ip = request_api_proxy[0]["Ip"] + ":" + str(port)
            proxy = {protocol: protocol + "://" + ip}

        # Formats the selected proxy accordingly.
        elif proxy != "auto" and proxy is not None:
            if proxy[:4] == "http":
                protocol = "http"
                proxy = {protocol: proxy}
            elif proxy[:5] == "https":
                protocol = "https"
                proxy = {protocol: proxy}
            elif proxy[:3] == "ftp":
                protocol = "ftp"
                proxy = {protocol: protocol + "://" + proxy}

        if proxy is None:
            proxy = ""

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
    print(Settings.get_user_agent(None))
    print(Settings.get_proxy("auto"))
