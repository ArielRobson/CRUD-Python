from uteis import cor
from time import sleep
import funcoes_sistema as fs


print(cor(33, '====== CADASTRO DE CLIENTES ======'))
print('Selecione uma opção:')
print(cor(31, """1 - CADASTRAR
2 - PESQUISAR
3 - ATUALIZAR
4 - DELETAR
5 - SAIR"""))
while True:
    opcao = int(input(cor(33,'OPÇÃO: ')))

    if opcao == 1:
        print(cor(35, '===== CADASTRO DE CLIENTE ====='))
        sleep(1)
        nome = str(input('Nome do Cliente:')).upper()
        cpf = str(input('CPF cliente: ')).upper()
        end = str(input('Endereço: ')).upper()
        setor = str(input('Setor: ')).upper()
        tel = str(input('Telefone:')).upper()
        fs.inserir_dados(nome, cpf, end, setor, tel)

    elif opcao == 2:
        sleep(1)
        nome = str(input('Informe o nome ou ID do cliente: '))
        sleep(1)
        if nome.isnumeric():
            fs.pesquisar_dados_id(nome)
        else:
            fs.pesquisar_dados(nome)

    elif opcao == 3:
        sleep(1)
        print('Informe o ID para atualizar os dados:')
        opcao = int(input('ID do cliente: '))
        sleep(1)
        print('Dados a serem atualizados...')
        fs.pesquisar_dados_id(opcao)
        sleep(1)
        print("Selecione a opção para atualizar.")
        print("""1 - nome
        2 - cpf
        3 - endereco
        4 - setor
        5 - telefone""")
        sleep(1)
        coluna = int(input('opção: '))
        if coluna == 1:
            coluna = 'nome'
        elif coluna == 2:
            coluna = 'cpf'
        elif coluna == 3:
            coluna = 'endereco'
        elif coluna == 4:
            coluna = 'setor'
        else:
            coluna = 'telefone'
        valor = str(input('Informe o novo valor para atualizar: '))
        fs.atualizar_dados(opcao, coluna, valor)

    elif opcao == 4:
        print('Exclusão de cliente.')
        delete = int(input('Informe o ID do cliente para excluir: '))
        fs.deletar(delete)

    elif opcao == 5:
        break
