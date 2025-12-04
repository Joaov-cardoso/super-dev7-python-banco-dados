from mysql.connector import connect

def executar():
    # criar_titulo()
    # listar_titulos()
    editar_titulo()
    # apagar_titulo()


def criar_titulo():
    titulo = input("Digite o título do livro: ")
    quantidade_paginas = input("Digite a quantidade de páginas: ")
    paginas = int(quantidade_paginas)

    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='biblioteca'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO livros (titulo, quantidade_paginas) VALUES (%s, %s)"
    dados = (titulo, paginas)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    print("Titulo cadastrado com sucesso")


def listar_titulos():
    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='biblioteca'
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livros")

    registros = cursor.fetchall()

    cursor.close()

    for registro in registros:
        id = registro[0]
        titulo = registro[1]
        print("ID:", id, "\tTitulo: ", titulo)


def editar_titulo():
    listar_titulos()

    id = input("Digite o id que deseja editar: ")
    titulo = input("Digite o novo titulo: ")
    quantidade_paginas = input("Digite a quantidade de paginas: ")
    paginas = int(quantidade_paginas)

    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='biblioteca'
    )

    cursor = conexao.cursor()

    sql = "UPDATE livros SET titulo=%s, quantidade_paginas=%s WHERE id = %s"
    dados = (titulo, paginas, id)
    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    print("Titulo alterado com sucesso")


def apagar_titulo():
    listar_titulos()

    id = input("Ditite o id que deseja apagar: ")

    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='biblioteca'
    )

    cursor = conexao.cursor()

    sql = "DELETE FROM livros WHERE id = %s"
    dados = (id, )
    cursor.execute(sql, dados)

    conexao.commit()

    linhas_afetadas = cursor.rowcount
    if linhas_afetadas == 0:
        print("ID informadi inexistente")
    else:
        print("Categoria apagada com sucesso")

    cursor.close