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


class Banner(Settings):
    def __init__(self):
        """ Constructor and Attributes. """
        super().__init__()

    def print_logo(self) -> None:
        """ Print the banner without specifications. """
        Color.println("""
🌸—————————————————————————————————————————————————————————————————————————————————🌸
{PK}
    888  ,d8 ,8b.     888PPP8b  ,8b.     PPPPP88p',8b.     888  ,dP 888   88 
    888_dPY8 88'8o    d88    `  88'8o        ,dP' 88'8o    888o8P'  888ooo88 
    8888' 88 88PPY8.  d8b PPY8  88PPY8.    ,dP'   88PPY8.  888 Y8L        88 
    Y8P   Y8 8b   `Y' Y8PPPPPP  8b   `Y' YPPPPPPP 8b   `Y' 888  `8p PPPPPP8P{W}""")
        print(f""" 
                 Authors: {self.get_authors} 
                              Version: {self.get_version}
                 GitHub: {self.get_github}

🌸——————————————————————————————————————————————————————————————————————————————————🌸""")

    @staticmethod
    def print_helper() -> None:
        """ Print the banner helper """
        print("""
Usage: python3 nagazaky.py [options]

Description: Nagazaky has a very simple purpose, which is to automate the entire  process 
             of collecting  information  from  a target system. Open source, fully embedded 
             in Python, in addition to  being fully didactic, it is  one  of the most 
             powerful, useful and effective tools in the  day-to-day life of an information 
             security professional."

Arguments:

   -h, --help                Show this help message and exit
   -u <URL>, --url <URL>     Target URL (http://www.site_target.com/)
   --user-agent <CUSTOM>     Customize the User-Agent. Default: Random User-Agent
   --proxy <AUTO, CUSTOM>    Use a proxy to connect to the target URL
   
   --update                  Updates Nagazaky to the latest version
   --no-logo                 Disable the initial banner\n""")


if __name__ == "__main__":
    banner = Banner()
    banner.print_logo()
    banner.print_helper()
