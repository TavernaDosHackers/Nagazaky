import os
import argparse

#from src.core.settings import Define
from src.lib.dork import DorkSearch

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--dork",
                    action="store",
                    type=str,
                    default=False,
                    help="Set your dork")

parser.add_argument("-p", "--pages",
                    action="store",
                    type=str,
                    default=False,
                    help="Set number of pages")


parser.add_argument("--user-agent",
                    action="store",
                    type=str,
                    default=False,
                    help="Customize the User-Agent. Default: Random User-Agent")

parser.add_argument("--proxy",
                    action="store",
                    type=str,
                    default=False,
                    help="Use a proxy to connect to the target URL")

args = parser.parse_args()

try:
    DorkSearch.Bing(args)

except KeyboardInterrupt:
    print("[+] CTRL + C pressed")
