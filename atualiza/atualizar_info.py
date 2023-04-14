
info = []
def busca_info(id):
    with open('dados.txt', 'r') as arq:
        linha = arq.readlines()
        for ident in linha:
            if f'ID = {str(id)}' in ident:
                info = ident.replace("\n", "").split("|")
                return info


#def atualiza_info()
#print(busca_info(4))