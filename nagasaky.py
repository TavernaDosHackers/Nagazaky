import argparse

from src.utils.whatisacms import WhatIsACMS
from src.browser import engine
from src.core.settings import settings

print(settings.banner)

parser = argparse.ArgumentParser(usage="python3 nagasaky.py", description="Nagasaky é uma ferramenta de busca por dork's e auto exploração.\nCriadores: https://github.com/blkzy | https://github.com/CR3DN3")

parser.add_argument("-d", "--dork", 
                          type=str, 
                          default=None, 
                          help="Dork para procurar os link's", 
                          required=True)

parser.add_argument("-e", "--engine-search", 
                          type=str,
                          default="Bing", 
                          help="Para escolher o motor de busca")

parser.add_argument("-r", "--random-agent", 
                          action="store_true",
                          default=False, 
                          help="User Agent aleatório...")
                          
parser.add_argument("-v", "--verbose",
                          action="store_true",
                          default=False,
                          help="Verbose mode")

parser.add_argument("--cms", 
                          action="store",
                          type=str,
                          default="all")
 
args = parser.parse_args()
browser = engine()

print(args.cms)

""""
if args.cms
WhatIsACMS(args.dork, args.verbose, settings.user_agent_default).wordpress()

if args.engine_search.lower() in ["bing", "duckduckgo", "google", "baidu"]:
    print(browser.search(args.engine_search.lower(), args.dork, args.random_agent))
else:
    print("Não conheço esse motor de busca!")
"""
