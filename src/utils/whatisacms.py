import requests

class WhatIsACMS:
    def __init__(self, url, verbose, user_agent):
        self.url = url
        self.user_agent = user_agent
        self.verbose = verbose

    def wordpress(self):
        """
        Faz uma requisição no site alvo com o 
        diretório de login do WordPress.
        """
        if self.verbose == True:
            print(f"[*] Verificando diretórios WordPress")
        rWordPressDirectoryLogin = requests.get(self.url + "/wp-login.php", headers={'User-Agent': self.user_agent})
        rWordPressDirectoryContent = requests.get(self.url + "/wp-content/", headers={'User-Agent': self.user_agent})

        """
        Verifica se as requisições do site alvo
        com os diretórios retornaram 200 (OK).
        """
        if rWordPressDirectoryLogin.status_code == 200 or rWordPressDirectoryContent.status_code == 200:
            print("[+] Diretório(s) WordPress econtrado:")
        if rWordPressDirectoryLogin.status_code == 200:
            print("    - /wp-login.php")
        if rWordPressDirectoryContent.status_code == 200:
            print("    - /wp-content/")


    def joomla(self):
        """
        Faz uma requisição no site alvo com o 
        diretório de login do Joomla.
        """
        if self.verbose == True:
            print(f"[*] Verificando diretórios Joomla...")
        rJoomlaDirectoryLogin = requests.get(self.url + "/com_content/", headers={'User-Agent': self.user_agent})
        rJoomlaDirectoryContent = requests.get(self.url + "/administrator/", headers={'User-Agent': self.user_agent})

        """
        Verifica se as requisições do site alvo
        com os diretórios retornaram 200 (OK).
        """
        if rJoomlaDirectoryLogin.status_code == 200 or rJoomlaDirectoryContent.status_code == 200:
            print("[+] Diretório(s) Joomla econtrado:")
        if rJoomlaDirectoryLogin.status_code == 200:
            print("    - /com_content/")
        if rJoomlaDirectoryContent.status_code == 200:
            print("    - /administrator/")


    def drupal(self):
        """
        Faz uma requisição no site alvo com o 
        diretório de login do Drupal.
        """
        if self.verbose == True:
            print(f"[*] Verificando diretórios Drupal...")
        rDrupalDirectoryFiles = requests.get(self.url + "/sites/default/files/", headers={'User-Agent': self.user_agent})
        rDrupalDirectoryREADME = requests.get(self.url + "/modules/README.txt", headers={'User-Agent': self.user_agent})

        """
        Verifica se as requisições do site alvo
        com os diretórios retornaram 200 (OK).
        """
        if rDrupalDirectoryFiles.status_code == 200 or rDrupalDirectoryREADME.status_code == 200:
            print("[+] Diretório(s) Drupal econtrado:")
        if rDrupalDirectoryFiles.status_code == 200:
            print("    - /sites/default/files/")
        if rDrupalDirectoryREADME.status_code == 200:
            print("    - /modules/README.txt")