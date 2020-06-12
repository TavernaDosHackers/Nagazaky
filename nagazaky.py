#!/usr/bin/env python3

import os
import time
import argparse
import requests

from src.core.settings import Strings as S
from src.core.settings import Define
from src.lib.dork import DorkSearch
from src.lib.check import Check

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url",
                    action="store",
                    type=str,
                    default=False,
                    help="Set target site (www.target.com)")

parser.add_argument("-d", "--dork",
                    action="store",
                    type=str,
                    default=False,
                    help="Set your dork")

parser.add_argument("--user-agent",
                    action="store",
                    type=str,
                    default=False,
                    help="Set your personal user-agent. Default: Random")

parser.add_argument("-p", "--pages",
                    action="store",
                    type=int,
                    default=1,
                    help="Set number of pages case use dork")

parser.add_argument("-v", "--verbose",
                    action="store_true",
                    default=False,
                    help="Active verbose mode: True")

args = parser.parse_args()
S.Banner()

try:
    
    # Define um user-agent aleatório caso o usuário não insira
    args.user_agent = Define.UserAgent(args)

    # Condição caos o usuário entre com uma dork nos argumentos
    if args.dork:
        DorkSearch.Bing(args)
    # Condição caso o usuário entre com um site nos argumentos
    elif args.url:

        # Formata a URL, adicionando "http://" caso não tenha e "/" no final
        args.url = Define.TargetClean(args)
        # Faz a requisição da URL, retornando o valor de status_code
        StatusTarget = Check.StatusTarget(args)

        # Verifica na condição se a URL está ONLINE ou OFFLINE
        if StatusTarget == 200:
            print(f"[+] Target: {args.url} [{StatusTarget}]")
        else:
            print(f"[-] Target: {args.url} [{StatusTarget}]")
        
        # Faz a requisição verificando se há um arquivo robots.txt no alvo
        StatusRobots = Check.Robots(args)

        if StatusRobots == 200:
            print(f"[+] Robots.txt found! {args.url}robots.txt")
        
        CMSList = Check.CMS.Run(args)
        for CMS in CMSList:
            print(f"[+] CMS found! {CMS}")

    # Caso o usuário não escolha nada ele fará um print help dos argumentos opcionais.
    else:
        parser.print_help()
        exit()

except KeyboardInterrupt:
    print(" - [+] CTRL + C pressed")
