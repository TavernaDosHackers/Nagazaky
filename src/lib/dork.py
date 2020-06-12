#!/usr/bin/env python3

import requests

from requests.exceptions import Timeout
from bs4 import BeautifulSoup

class DorkSearch:
    def Google(self):
        # Realiza a requisição do google com dork selecionada
        pass

    def DuckDuckGo(self):
        # Realiza a requisição do DuckDuckGo com dork selecionada
        pass
        
    def Bing(self):
        # Realiza a requisição do Bing com dork selecionada
        url_list     = []
        url_sucess   = []
        url_error404 = []
        

        requests.packages.urllib3.disable_warnings()

        req = requests.get(f"https://www.bing.com/search?q={self.dork}&first={self.pages}", headers={'User-Agent': self.user_agent}, verify=False)

        soup = BeautifulSoup(req.text, 'html.parser')
            
        for x in soup.find_all('cite'):
            x = x.text; y = x.split('/')[2]


            if x[:7] == "http://":
                x = "http://www." + y
            elif x[:8] == "https://":
                x = "https://www." + y
            elif not "www." in x:
                x = "http://www." + y

            url_list.append(x)

        print(url_list)

        for x in url_list:
            try:
                req = requests.get(x, headers={'User-Agent': self.user_agent}, verify=False, timeout=3)
            except Timeout:
                print(f"[!] Timout -> {x}")
            except Exception:
                print(f"[!] Erro desconhecido -> {x}") 

                #print(f"\r[+] Verificando o site -> {x}\n", end="", flush=True)
            if req.status_code == 200:
                print(f"[*] Sucesso na verificação -> {x}")
            else:
                print(f'[!] Erro na verificação -> {x}')