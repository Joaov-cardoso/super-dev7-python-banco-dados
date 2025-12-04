from mysql.connector import connect

def executar():
    # criar_titulo()
    listar_titulos()
    # editar_titulo()
    # apagar_titulo()


def criar_titulo():
    titulo = input("Digite o título do livro: ")
    quantidade_paginas = input("Digite a quantidade de páginas: ")
    paginas = int(quantidade_paginas)
    autor = input("Digite o autor do livro: ")
    preco_str = input("Digite o preço do : ")
    preco_float = float(preco_str)
    isbn = input("Digite o ISNB do livro: ")
    descricao = input("Descrição do livro: ")

    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='biblioteca'
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO livros (" \
    "titulo, " \
    "quantidade_paginas, " \
    "autor, " \
    "preco, " \
    "isbn, " \
    "descricao" \
    ") VALUES (%s, %s,%s,%s,%s,%s)"
    dados = (titulo, paginas, autor, preco_float, isbn, descricao)

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
        quantidade_paginas = registro[2]
        autor = registro[3]
        preco = registro[4]
        isbn = registro[5]
        descricao = registro[6]
        print(
            "ID:", id, 
            "\tTitulo: ", titulo, 
            "\tQuantidade de Páginas: ", quantidade_paginas, 
            "\tAutor: ", autor, 
            "\tPreço: ", preco, 
            "\tISBN: ", isbn, 
            "\tDescrição: ", descricao
        )


def editar_titulo():
    listar_titulos()

    id = input("Digite o id que deseja editar: ")
    titulo = input("Digite o título do livro: ")
    quantidade_paginas = input("Digite a quantidade de páginas: ")
    paginas = int(quantidade_paginas)
    autor = input("Digite o autor do livro: ")
    preco_str = input("Digite o preço do : ")
    preco_float = float(preco_str)
    isbn = input("Digite o ISNB do livro: ")
    descricao = input("Descrição do livro: ")

    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='biblioteca'
    )

    cursor = conexao.cursor()

    sql = "UPDATE livros SET " \
    "titulo=%s, " \
    "quantidade_paginas=%s, " \
    "autor=%s, " \
    "preco=%s, " \
    "isbn=%s, " \
    "descricao=%s " \
    "WHERE id = %s"
    dados = (titulo, paginas, autor, preco_float, isbn, descricao, id)
    
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