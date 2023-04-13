from Inserir import cria_insere as c
from leitura import ler_info as r
from atualiza import atualizar_info as a
from utilitarios import util as util
from time import sleep


print(f"{util.cor_texto('vermelho','='*10)} "
      f"{util.cor_texto('vermelho', 'CADASTRO DE CLIENTES')} "
      f"{util.cor_texto('vermelho','='*10)}")
while True:
    print(util.cor_texto('amarelo',"""    1 - Cadastrar
    2 - Ver Informações
    3 - Atualizar Informações
    4 - Deletar Cadastro
    5 - Sair"""))
    opcao = int(input("Escolha a opção: "))
    sleep(1)
    if opcao == 1:
        print(util.cor_texto('verde','Preencha com os dados do cliente:'))
        nome = str(input("Nome:"))
        cpf = int(input("CPF - (Somente números):"))
        if not c.verificaCPF(cpf):
            print("CPF inválido, verificar quantidade de digitos e inserir novamente")
            while True:
                cpf = int(input("CPF - (Somente números):"))
                if c.verificaCPF(cpf):
                    break
        rua = str(input("Endereço Rua:"))
        quadra = str(input("Quadra:" ))
        lote = str(input("Lote: "))
        setor = str(input("Setor: "))
        tel = int(input("Telefone:(+55)"))
        if not c.verificaTel(tel):
            print("Telefone inválido, verificar quantidade de digitos e inserir novamente.")
            while True:
                tel = int(input("Telefone:(+55)"))
                if c.verificaTel(tel):
                    break
        id = c.gerarID()
        try:
            c.escreverNoArquivo(f"ID = {id} | nome = {nome.lower()} | cpf = {cpf} | "
                                f"endereco = {rua + ' ' + 'qd ' + quadra + ' lt ' + lote + ' - ' + 'setor: ' + setor} "
                                f"| telefone = {tel} \n")
        except:
            print("Falha ao gravar dados no arquivo.")
########################################################################################################################
    if opcao == 2:
        nome = str(input("Informe o nome do cliente:"))
        print("\n")
        sleep(1)
        print(f"Cadastros encontrados para o nome pesquisado... ---> {nome}")
        sleep(1)
        r.busca_nome(nome)

    if opcao == 3:
        id = int(input("Informe o número do ID do cliente:"))
        a.atualiza_dados(id)


    if opcao == 5:
        break
