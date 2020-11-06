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

from nagazaky.core.settings import Settings
from nagazaky.core.color import Color
from nagazaky.core.request import Request


class CheckCMS(Settings):
    def __init__(self, url: str, request: Request):
        """ Constructor and Attributes. """
        super().__init__()
        self.url = url
        self.request = request
        self.home_request = self.request.get(self.url)

    def run(self) -> list:
        cms = []

        # WordPress
        if "wp-" in self.home_request.text:
            Color.println(" │  ├ WordPress: {P}running{W}")
            cms.append("wordpress")

        # Joomla
        elif "com_content" in self.home_request.text:
            Color.println(" │  ├ Joomla: {P}running{W}")
            cms.append("joomla")

        # Drupal
        elif "/sites/default/files/" in self.home_request.text:
            Color.println(" │  ├ Drupal: {P}running{W}")
            cms.append("drupal")

        else:
            Color.println(" │  │ 'No valid CMS was found.'")

        # Returns a list of the CMS found.
        return cms
