#!/usr/bin/env python3

from nagazaky.core.settings import Settings
from nagazaky.core.color import Color


class Banner(Settings):
    def __init__(self):
        """ Constructor and Attributes. """
        super().__init__()

    def print_logo(self):
        """ Print the banner without specifications. """
        Color.println("""
———————————————————————————————————————————————————————————————————————————
{PK}
    ███╗   ██╗ █████╗  ██████╗  █████╗ ███████╗ █████╗ ██╗  ██╗██╗   ██╗
    ████╗  ██║██╔══██╗██╔════╝ ██╔══██╗╚══███╔╝██╔══██╗██║ ██╔╝╚██╗ ██╔╝
    ██╔██╗ ██║███████║██║  ███╗███████║  ███╔╝ ███████║█████╔╝  ╚████╔╝ 
    ██║╚██╗██║██╔══██║██║   ██║██╔══██║ ███╔╝  ██╔══██║██╔═██╗   ╚██╔╝  
    ██║ ╚████║██║  ██║╚██████╔╝██║  ██║███████╗██║  ██║██║  ██╗   ██║   
    ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝{W}""")
        print(f""" 
                 Authors: {self.get_authors} 
                              Version: {self.get_version}
                 GitHub: {self.get_github}

———————————————————————————————————————————————————————————————————————————""")

    @staticmethod
    def print_helper():
        """ Print the banner helper """
        print("""
Usage: python3 nagazaky.py [options]

Arguments:

   -h, --help             Show this help message and exit
   -u URL, --url URL      Target URL (http://www.site_target.com/)

   --no-update
   --no-logo              Disable the initial banner\n""")


if __name__ == "__main__":
    pass
