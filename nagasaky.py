import argparse

from src.browser import engine
from src.core.settings import settings
from ext import extension

print(settings.banner)
parser = argparse.ArgumentParser(usage="python3 proSearch.py", description="ProSearch é uma ferramenta de busca por dork's.\nCriador: https://github.com/blkzy")

parser.add_argument("-d", "--dork", type=str, default=None, help="Dork para procurar os link's", required=True)
parser.add_argument("-e", "--engine-search", type=str, default="Bing", help="Para escolher o motor de busca")
parser.add_argument("-r", "--random-agent", action="store_true", default=False, help="User Agent aleatório...")
parser.add_argument(extension.SE_config["command"][0], extension.SE_config["command"][1], type=str, default="Bing", help=extension.SE_config["description"])

args = parser.parse_args()
browser = engine()

if args.search_exploit:
    extension.SE_search_name_filter(name=args.search_exploit)

if args.engine_search.lower() in ["bing", "duckduckgo", "google", "baidu"]:
    browser.search(args.engine_search.lower(), args.dork, args.random_agent)
else:
    print("Não conheço esse motor de busca!")