import requests as r 
from colorama import Fore as F 
import os as sistema 
import re, sys
import argparse as arg 
sistema.system('cls' if sistema.name == 'nt' else 'reset')

# CORES
RED = F.RED
WHITE = F.WHITE
YELLOW = F.YELLOW
GREEN = F.GREEN
BLUE = F.BLUE
CYAN = F.CYAN

def arruma(url):
	if url[-1] != "/":
		url = url + "/"
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url

index = r"""{}
                        _   _                            _            _______          _ 
                       | \ | |                          | |          |__   __|        | |
                       |  \| | __ _  __ _  __ _ ______ _| | ___   _     | | ___   ___ | |
                       | . ` |/ _` |/ _` |/ _` |_  / _` | |/ / | | |    | |/ _ \ / _ \| |
                       | |\  | (_| | (_| | (_| |/ / (_| |   <| |_| |    | | (_) | (_) | |
                       |_| \_|\__,_|\__, |\__,_/___\__,_|_|\_\\__, |    |_|\___/ \___/|_|
                                     __/ |                     __/ |                     
                                    |___/                     |___/                      

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                 # Nagazaky Exploit Finder Automatic
 				# Discord: https://discord.gg/xDT9Mem
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""".format(F.GREEN, F.WHITE, F.GREEN, F.WHITE, F.GREEN, F.WHITE, F.GREEN, F.WHITE, F.GREEN, F.WHITE)
manual = r"""
{}--url       {}Alvo (-u www.site.com)
{}--threads   {}Threads para cada requisição (-t 10)
{}--salvar    {}Salvar todos diretórios em um arquivo log.txt (-s)
""".format(GREEN, WHITE, GREEN, WHITE, GREEN, WHITE)

if len(sys.argv) == 1:
	print(index)
	print(manual)
	exit()

parser = arg.ArgumentParser()
parser.add_argument("--url","-u", action='store')
parser.add_argument("--threads","-t", action="store", type = int, default = "10")
parser.add_argument("--salvar","-s", action="store_true")
param = parser.parse_args()

if not param.url:
	print(index)
	print("{}[ERRO] {}Insira uma URL! (ex: --url www.google.com)".format(RED, WHITE))
	exit()

ok_diretorios = []
url = arruma(param.url)

print(index)
print("{}[+] {}Site alvo: {}".format(GREEN, WHITE, url))
print("{}[+] {}Threads para cada requisição: {}".format(GREEN, WHITE, param.threads))

try:
	checa = r.get(url, timeout=param.threads)
	if checa.status_code == 200:
		print("{}\n[=] {}Conexão estável.".format(GREEN, WHITE))
	else:
		print("{}[X] {}Conexão rejeitada!".format(RED, WHITE))
		exit()
except Exception as err:
	print("{}[ERRO] {}Aconteceu um erro ao fazer a conexão no site {}\nErro: {}".format(RED, WHITE, url, err))
	exit()

print("\n{}[*] {}Buscando diretórios na página inicial.".format(BLUE, WHITE))

requisicao = r.get(url).text
x_sites = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", requisicao)

if not x_sites:
	print("{}[OPS] {}Nenhum diretório foi encontrado :/.".format(RED, WHITE))
	exit()

for sit in x_sites:
	if sit[6:] in ok_diretorios:
		continue
		# H T T P S : / / 
	if url[9:] in sit:
		ok_diretorios.append(sit)
	elif url[8:] in sit:
		ok_diretorios.append(sit)
	else:
		continue

print("{}    [+] {}Total de diretório(s) encontrado na página inicial: {}".format(GREEN, WHITE, str(len(ok_diretorios))))
input("{}    Pressione {} para listar os diretórios\n".format(WHITE, "Enter"))
for y in ok_diretorios:
	print("{}    [DIR] {}{}".format(YELLOW, WHITE, y))

if param.salvar:
	print("\n{}[*] {}Salvando resultados... (log.txt)".format(BLUE, WHITE))
	arquivo = open("log.txt", "w")
	arquivo.write("[+] - Nagazaky Directory Searcher - [+]\nDiscord: https://discord.gg/xDT9Mem/\n\n[*] - Lista de diretórios encontrados - [*]\n\n")
	for linha in ok_diretorios:
		arquivo.write(linha + "\n")
	print("{}[+] {}Salvo!".format(GREEN, WHITE))
print("\n{}[=] {}Sua busca foi finalizada! =)".format(GREEN, WHITE))
exit()
