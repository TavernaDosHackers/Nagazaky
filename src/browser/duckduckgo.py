from .browser import Browser
from src.utils.validator import Validator

class DuckDuckGo:
    def __init__(self):
        self.browser = Browser()
        self.validator = Validator()

    def search_for(self, dork, user_agent=False):
        url_list = []
        
        self.browser.set_user_agent(user_agent=user_agent)
        request = self.browser.open(f"https://duckduckgo.com/?q={dork}&atb=v236-1&ia=web", timeout=10)

        for code in self.browser.get_current_page().find_all("div", class_="result__body"):
            code = code.find("a", class_="result__a").get("href", None).split("=")[1].replace("%3A", ":").replace("%2F", "/")

            url_list.append(code)

        self.browser.close()

        return url_list