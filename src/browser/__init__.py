from . import bing
from src.core.settings import settings
from random import choice

class engine:
    """Nessa classe é onde as pesquisas serão iniciadas."""
    def __init__(self):
        self.bing = bing.Bing()
        self.duck = None
        self.google = None
        self.baidu = None
        self.bing_results = []
        self.duck_results = []
        self.google_results = []
        self.baidu_results = []

    def search(self, engine_search, dork, random_user_agent=False):
        if engine_search.lower() == "bing":
            if random_user_agent is True:
                urls = self.bing.search_for(dork=dork, user_agent=self.get_user_agent())
            else:
                urls = self.bing.search_for(dork=dork, user_agent=settings.user_agent_default)

            for x in urls:
                self.bing_results.append(x) 
            
            return self.bing_results

    def get_user_agent(self):
        with open("src/utils/user-agents.txt", "r") as file:
            user_agent = choice(file.readlines()).rstrip("\n")

            return user_agent