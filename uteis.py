import datetime


def log(mensagem):
    with open('log.txt', 'a') as arq:
        arq.write(f'{datetime.datetime.now()} ==== {mensagem} ====.\n')


def cor(num_cor, texto):
    return f'\033[{num_cor}m{texto}\033[m'
