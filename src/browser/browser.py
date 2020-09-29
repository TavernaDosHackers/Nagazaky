import mechanicalsoup

class Browser(mechanicalsoup.StatefulBrowser):
    def __repr__(self):
        return mechanicalsoup.StatefulBrowser(soup_config={'features':'html.parser'})