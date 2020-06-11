import requests
from bs4 import BeautifulSoup

class DorkSearch:
    def __init__(self, args):
        # Declaração de variaveis no construtor
        self.dork = args.dork
        self.pages = args.pages + 0

    def Google(self):
        # Realiza a requisão do google com dork selecionada
        pass
        
    def Bing(self):
        # Realiza a requisão do bing com dork selecionada
        url_sucess   = []
        url_error404 = []

        requests.packages.urllib3.disable_warnings()
        req = requests.get(f"https://www.bing.com/search?q={self.dork}&first=10", verify=False)

        soup = BeautifulSoup(req.text, 'html.parser')
        
        for x in soup.find_all('cite'):
            x = x.text; y = x.replace("http://","").replace("https://", "").replace("www.","")

            if x[:7] == "http://":
                x = "http://www." + y
            elif x[:8] == "https://":
                x = "https://www." + y

            try:
                req = requests.get(x, verify=False)
            except Exception:
                continue

            if req.status_code == 200:
                print('Success > ', x)
            else:
                print('Error > ', x)

    def DuckGo(self):
        pass