import os


"""def criarArquivo():
    if os.path.exists('dados.txt'):
        pass
    else:
        with open('dados.txt', 'w', encoding='UTF-8') as arq:
            pass
        print("Arquivo criado com sucesso!!")"""


def escreverNoArquivo(texto):
    with open('dados.txt', 'a') as arq:
        arq.write(texto)


def gerarID():
    file_path = "dados.txt"
    
    if os.path.getsize(file_path) == 0:
        return 1
    else:
        with open('dados.txt', 'r') as arq:
            linhas = arq.readlines()
            ultimo_linha = linhas[-1].split("|")
            ultimo_id = ultimo_linha[0].strip().replace("ID = ", "")
            numero = int(ultimo_id) + 1
        return numero


def verificaCPF(cpf):
    if len(str(cpf)) < 11 or len(str(cpf)) > 11:
        return False
    else:
        return True


def verificaTel(telefone):
    if len(str(telefone)) < 11 or len(str(telefone)) > 11:
        return False
    else:
        return True