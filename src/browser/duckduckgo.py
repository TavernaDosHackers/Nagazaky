import requests
from bs4 import BeautifulSoup

class duckduckgo:
    def __init__(self):
        ...
    
    def search(self, dork, user_agent=False):
        request = requests.get(f"https://duckduckgo.com/?q={dork}&atb=v236-1&ia=web")
        