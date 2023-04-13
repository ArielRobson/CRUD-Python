def atualiza_dados(id):
    with open('dados.txt', 'a') as arq:
        linha = arq.readlines()
        for ident in linha:
            if id in ident:
                print(1)
