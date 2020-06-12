#!/usr/bin/env python3

import requests

class Check:
    def StatusTarget(self):
        # Realiza a requisição da URL do alvo
        r = requests.get(self.url)
        # Retorna o status code da requisição
        return r.status_code
    
    def Robots(self):

        # Realiza a requisição da URL do alvo
        r = requests.get(self.url + "robots.txt", headers={'User-Agent': self.user_agent})
        # Retorna o status code da requisição
        return r.status_code
    
    class CMS:
        def Run(self):
            CMSChecked = []
            # Realiza a requisição da URL do alvo
            r = requests.get(self.url, headers={'User-Agent': self.user_agent})
            
            # Verifica se o alvo roda WordPress
            if "wp-content" in r.text:
                CMSChecked.append("WordPress")
            
            # Verifica se o alvo roda Joomla
            if "com_content" in r.text:
                CMSChecked.append("Joomla")
            
            # Verifica se o alvo roda Drupal
            if "/sites/default/files/" in r.text:
                CMSChecked.append("Drupal")
            
            # Retorna a lista com todas as CMS encontradas
            return CMSChecked
            

