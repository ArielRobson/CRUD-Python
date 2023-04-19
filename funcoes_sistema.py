from conexao_DB import conexao_db
from mysql.connector import errors


def inserir_dados(nome, cpf, end, setor, tel):
    conexao = conexao_db()
    try:
        cursor = conexao.cursor()
        insert = f"insert into info_clientes(nome, cpf, endereco, setor, telefone)" \
                 f"values('{nome}', '{cpf}', '{end}', '{setor}', '{tel}')"
        cursor.execute(insert)
        conexao.commit()
        conexao.close()
        print('Dados inseridos com sucesso!')

    except errors.IntegrityError as e:
        print(e)
    except errors.DatabaseError as db:
        print(db)
    except Exception as e:
        print(e)


def pesquisar_dados(nome):
    conexao = conexao_db()
    cursor = conexao.cursor()
    pesquisa = f"select * from info_clientes where nome like '%{nome}%'"
    cursor.execute(pesquisa)
    resultado = cursor.fetchall()

    for r in resultado:
        dados = f"ID: {r[0]} - NOME: {r[1]} - CPF: {r[2]} - ENDERECO: {r[3]} - SETOR: {r[4]} - TEL: {r[5]}"
        print(dados)

    conexao.close()


def pesquisar_dados_id(id):
    conexao = conexao_db()
    cursor = conexao.cursor()
    pesquisa = f"select * from info_clientes where id = {id}"
    cursor.execute(pesquisa)
    resultado = cursor.fetchall()

    for r in resultado:
        dados = f"ID: {r[0]} - NOME: {r[1]} - CPF: {r[2]} - ENDERECO: {r[3]} - SETOR: {r[4]} - TEL: {r[5]}"
        print(dados)

    conexao.close()


def atualizar_dados(id,dado, valor):
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        atualiza = f"update info_clientes set {dado} = '{valor}' where id = {id}"
        cursor.execute(atualiza)
        conexao.commit()
        conexao.close()
        print('Cliente atualizado com sucesso!')
    except Exception as e:
        print(f'Falha ao atualiza dados erro: {e}')


def deletar(id):
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        delete = f"delete from info_clientes where id = {id}"
        cursor.execute(delete)
        conexao.commit()
        conexao.close()
        print('Cliente deletado com sucesso!')
    except Exception as e:
        print('Ocorreu um erro ao tentar deletar o cliente. ' + e)
