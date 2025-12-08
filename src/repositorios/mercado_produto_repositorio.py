from src.banco_dados import conectar

def cadastrar(nome: str, id_categoria: int):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO produtos (nome, id_categoria) VALUES (%s, %s)"
    dados = (nome, id_categoria)
    cursor.execute(sql, dados)
    conexao.commit()
    cursor.close()
    conexao.close()


def editar(id: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "UPDATE categorias SET nome = %s WHERE id = %s"
    dados = (nome, id)
    cursor.execute(sql, dados)
    conexao.commit()
    cursor.close()
    conexao.close()


def apagar(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM produtos WHERE id = %s"
    dados = (id,)
    cursor.execute(sql, dados)
    conexao.commit()

    linhas_afetadas = cursor.rowcount

    cursor.close()
    conexao.close()
    return linhas_afetadas


def obter_todos():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """select
    produtos.id,
    produtos.nome,
    categorias.id,
    categorias.nome
    from produtos
    inner join categorias on (produtos.id_categoria = categoria.id)"""
    cursor.execute(sql)
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()
    produtos = []

    for registro in registros:
        produto = {
            "id": registro[0],
            "nome": registro[1]
        },"categoria"={
            "id": registro[2],
            "nome": registro[3]
        }
        produtos.append(produto)
    return produtos