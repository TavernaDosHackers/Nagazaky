import requests

class Check:
    def StatusTarget(self, url):
        # Realiza a requisição da URL do alvo
        r = requests.get(url)
        # Retorna o status code da requisição
        return r.status_code

    def Robots(self, url):
        # Realiza a requisição da URL do alvo
        r = requests.get(url+"robots.txt", headers={'User-Agent': self.user_agent})
        # Retorna o status code da requisição
        return r.status_code