import re
import sys

from validator_collection import validators, checkers
from .browser import Browser

class Bing:
    def __init__(self):
        self.url_list = []
        self.browser = Browser()

    def search_for(self, dork, user_agent=False):
        self.browser.set_user_agent(user_agent=user_agent)
        
        if not user_agent is False:
            request = self.browser.open(f"https://www.bing.com/search?q={dork}&qs=n&form=QBRE&sp=-1&pq=gru&sc=8-3&sk=&cvid=F2AE880AAC7C414B8057EE1FC2C0A96D", timeout=10)
        else:
            request = self.browser.open(f"https://www.bing.com/search?q={dork}&qs=n&form=QBRE&sp=-1&pq=gru&sc=8-3&sk=&cvid=F2AE880AAC7C414B8057EE1FC2C0A96D", timeout=10)

        for x in self.browser.get_current_page().find_all("li", class_="b_algo"):
            self.re_url(x.find("a").get("href", None))

        self.browser.close()

        return self.url_list

    def re_url(self, url):
        regex = re.compile(r'^(?:http|ftp)s?://') # http:// or https://
        regex = re.match(regex, url) is not None

        if regex is True and not url in self.url_list:
            self.url_list.append(url)