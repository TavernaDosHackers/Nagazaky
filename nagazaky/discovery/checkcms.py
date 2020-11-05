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

from nagazaky.core.color import Color
from nagazaky.core.settings import Settings
from nagazaky.core.request import Request


class CheckCMS(Settings):
    def __init__(self, url: str, request: Request):
        """ Constructor and Attributes. """
        super().__init__()
        self.url = url
        self.request = request

        self.su_request = self.request.get(self.url)

    def wordpress(self) -> bool:
        if "wp-content" in self.su_request.text:
            Color.println(" │  ├ WordPress: {G}running{W} (/wp-content/)")
            return True

    def joomla(self) -> bool:
        if "com_content" in self.su_request.text:
            Color.println(" │  ├ Joomla: {G}running{W} (/com_content/)")
            return True

    def drupal(self) -> bool:
        if "/sites/default/files/" in self.su_request.text:
            Color.println(" │  ├ Drupal: {G}running{W} (/sites/default/files/)")
            return True
