#!/usr/bin/env python3

from random import choice


class Strings:
    # Define as variáveis de cores
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    BLACK = '\033[30m'
    WHITE = '\033[37m'
    RESET = '\033[0;0m'
    BOLD = '\033[1m'

    def Banner():
        # Print no Banner do Nagazaky
        print(f"""_________________________________________________________________________{Strings.GREEN}{Strings.BOLD}
          _   _                            _
         | \ | |                          | |           Mass Exploit
         |  \| | __ _  __ _  __ _ ______ _| | ___   _      Finder Priv8
         | . ` |/ _` |/ _` |/ _` |_  / _` | |/ / | | |
         | |\  | (_| | (_| | (_| |/ / (_| |   <| |_| |
         |_| \_|\__,_|\__, |\__,_/___\__,_|_|\_\\__, |
                       __/ |                     __/ |
                      |___/                     |___/{Strings.RESET}
_________________________________________________________________________
        """)


class Define:
    def TargetClean(self):

        # Verifica se a URL tem "http://" ou "https://"
        if self.url[:7] != "http://" or self.url[:8] != "https://":
            self.url = "http://" + self.url

        # Verifica se a URL tem "/" no final
        if self.url[-1] != "/":
            self.url = self.url + "/"

        # Retorna a URL formatada
        return self.url

    def UserAgent(self):

        # Verifica se o user-agent foi setado pelo usuário
        if self.user_agent == False:

            # Abre o arquivo com vários user-agents
            OpenAgents = open("extras/user-agents/user-agents.txt", "r")
            # Leia todas as linhas do arquivo
            Agents = OpenAgents.readlines()
            # Fecha o arquivo
            OpenAgents.close()
            # Seleciona um user-agent aleatório na lista
            Agents = choice(Agents).rstrip("\n")

        # Retorna um user-agent aleatório
        return Agents
