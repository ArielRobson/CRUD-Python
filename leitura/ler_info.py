from CRUD.utilitarios import util
from time import sleep

def busca_nome(nome):
    with open('dados.txt', 'r') as arq:
        linhas = arq.readlines()
        for n in linhas:
            if nome.lower().strip() in n.lower().strip():
                dados = n.split("|")
                print(util.cor_texto("verde",f"{dados[0].strip()}\n"
                      f"{dados[1].strip()}\n"
                      f"{dados[2].strip()}\n"
                      f"{dados[3].strip()}\n"
                      f"================================================================================"))
                sleep(1)


