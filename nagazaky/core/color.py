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


class Color:
    """ Helper object for easily printing colored text to the terminal. """

    # Basic console colors
    colors = {
        "W": "\033[0m",  # white (normal)
        "PK": "\033[95m",  # pink
        "R": "\033[31m",  # red
        "G": "\033[32m",  # green
        "O": "\033[33m",  # orange
        "B": "\033[34m",  # blue
        "P": "\033[35m",  # purple
        "C": "\033[36m",  # cyan
        "GR": "\033[37m",  # gray
        "D": "\033[2m"  # dims current color. {W} resets.
    }

    # Helper string replacements
    replacements = {
        "{+}": "{W}{D}[{W}{G}+{W}{D}]{W}",
        "{-}": "{W}{D}[{W}{GR}-{W}{D}]{W}",
        "{!}": "{O}[{R}!{O}]{W}",
        "{?}": "{W}[{C}?{W}]"
    }

    @staticmethod
    def return_message(message: str) -> str:
        """ Returns colored string """
        output = message
        for (key, value) in Color.replacements.items():
            output = output.replace(key, value)
        for (key, value) in Color.colors.items():
            output = output.replace("{%s}" % key, value)
        return output

    @staticmethod
    def print(message: str) -> None:
        """
        Prints text using colored format on same line.
        Example:
            Color.p("R}This text is red. {W} This text is white")
        """
        import sys
        sys.stdout.write(Color.return_message(message))
        sys.stdout.flush()

    @staticmethod
    def println(message: str) -> None:
        """Prints text using colored format with trailing new line."""
        Color.print("%s\n" % message)

    @staticmethod
    def exception(message: str, ex: Exception or str) -> None:
        """ Prints message exception """
        Color.println(Color.return_message("{!} {R}%s{W}: " % message) + str(ex))


if __name__ == "__main__":
    Color.println("{R}Testing {G}One {C}Two {P}Three {W}Done")
    print(Color.return_message("{C}Testing {P}String {W}"))
    Color.println("{+} Good line")
    Color.println("{!} Danger")
