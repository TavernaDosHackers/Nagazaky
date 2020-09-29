from . import bing
from . import duckduckgo

from src.core.settings import settings
from random import choice

class engine:
    """Nessa classe é onde as pesquisas serão iniciadas."""
    def __init__(self):
        self.bing = bing.Bing()
        self.duck = duckduckgo.DuckDuckGo()
        self.google = None
        self.baidu = None
        self.bing_results = None
        self.duck_results = None
        self.google_results = []
        self.baidu_results = []

    def search(self, engine_search, dork, random_user_agent=False):
        if engine_search.lower() == "bing":
            if random_user_agent is True:
                self.bing_results = self.bing.search_for(dork=dork, user_agent=self.get_user_agent())
            else:
                self.bing_results = self.bing.search_for(dork=dork, user_agent=settings.user_agent_default)

            return self.bing_results

        elif engine_search.lower() == "duckduckgo":
            if random_user_agent is True:
                self.duck_results = self.duck.search_for(dork=dork, user_agent=self.get_user_agent())
            else:
                self.duck_results = self.duck.search_for(dork=dork, user_agent=settings.user_agent_default)
            
            return self.duck_results

    def get_user_agent(self):
        with open("src/utils/extras/user-agents.txt", "r") as file:
            user_agent = choice(file.readlines()).rstrip("\n")

            return user_agent