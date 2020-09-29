#from validator_collection import validators, checkers
from .browser import Browser
from src.utils.validator import Validator

class Bing:
    def __init__(self):
        self.browser = Browser()
        self.validator = Validator()

    def search_for(self, dork, user_agent=False):
        url_list = []

        self.browser.set_user_agent(user_agent=user_agent)
        request = self.browser.open(f"https://www.bing.com/search?q={dork}&qs=n&form=QBRE&sp=-1&pq=gru&sc=8-3&sk=&cvid=F2AE880AAC7C414B8057EE1FC2C0A96D", timeout=10)

        for x in self.browser.get_current_page().find_all("li", class_="b_algo"):
            url_list.append(self.validator.url(x.find("a").get("href")))

        self.browser.close()

        return url_list