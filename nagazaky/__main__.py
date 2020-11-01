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

try:
    from nagazaky.core.color import Color
    from nagazaky.core.banner import Banner
    from nagazaky.core.update import Update
    from nagazaky.core.args import Arguments

    import sys
    from requests import get
except (ValueError, ImportError) as e:
    Color.exception("Error", e)
except Exception as e:
    Color.exception("Unknown exception error", e)


class Nagazaky:
    def __init__(self):
        """ Constructor and Attributes. """
        self.args = Arguments().args
        self.banner = Banner()
        self.update = Update()

    def run(self) -> None:
        """ Method that starts Nagazaky. """
        if self.args.no_banner is False:
            self.banner.print_logo()

        if self.args.url is None:
            self.banner.print_helper()
            sys.exit()

        self.update.verify()
        if self.args.update is True:
            self.update.upgrade()
            sys.exit()


def entry_point() -> None:
    try:
        nagazaky = Nagazaky()
        nagazaky.run()
    except KeyboardInterrupt as ex:
        Color.exception("KeyboardInterrupt", ex)
    except Exception as ex:
        Color.exception("Unknown exception error", ex)


if __name__ == "__main__":
    entry_point()
