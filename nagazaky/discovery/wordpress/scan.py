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

import re

from nagazaky.core.color import Color
from nagazaky.core.request import Request


class Scan:
    def __init__(self, url: str, request: Request):
        """ Constructor and Attributes. """
        self.url = url
        self.request = request

    def directories_listing(self) -> None:
        directories = ["wp-content/uploads/", "wp-content/plugins/", "wp-content/themes/", "wp-includes/", "wp-admin/"]
        directories_found = []

        Color.println(" ├─{+} {G}Directories:{W}")
        for directory in directories:
            home_request = self.request.get(self.url + directory)
            if directory == "wp-admin/" and home_request.status_code == 200:
                Color.println(" │  ├ " + self.url + directory)
            if "Index of" in home_request.text:
                Color.println(" │  ├ " + self.url + directory)
            else:
                directories_found.append(directory)

        if not directories:
            Color.println(" │  │ 'No valid CMS was found.'")

    def readme_html(self) -> int or None:
        """ Get the readme file and extract the version is there is any. """
        url_readme = self.url + "readme.html"
        request_readme_html = self.request.get(url_readme)

        if request_readme_html.status_code == 200:
            Color.println(" ├─{+} {G}Readme.html:{W}")
            Color.println(" │  ├ " + url_readme)

            # Check version in readme.html.
            wordpress_version = re.search(r"Version.*", request_readme_html.text)  # en-US
            wordpress_versao = re.search(r"Versão.*", request_readme_html.text)  # pt-BR

            if wordpress_version or wordpress_versao:
                try:
                    version = wordpress_version.group().replace("Version ", "")
                except:
                    version = wordpress_versao.group().replace("Versão ", "")

                Color.println(" │  ├ WordPress Version (readme.html): " + version)

                # Returns the WordPress version
                return version
