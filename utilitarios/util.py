"""
31: vermelho
32: verde
33: amarelo
34: azul
35: roxo
36: ciano
37: cinza claro
"""

def cor_texto(cor, texto):
    cores = {"vermelho": 31, "verde": 32, "amarelo": 33, "azul": 34, "roxo": 35, "ciano": 36, "cinza claro": 37}
    return f'\033[{cores.get(cor)}m' + texto + '\033[0m'