from mysql.connector import connect

def executar():
    # criar_categoria()
    # listar_categorias()
    # editar_categoria()
    apagar_categoria()


def criar_categoria():
    nome = input("Digite o nome da nova categoria: ")

    print("Criando coneção com o banco de dados")

    # Abrir uma conexao com o banco de dados
    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='mercado'
    )
    #Criando um cursor para poder executar comandos no bd
    cursor = conexao.cursor()

    #Definir qual será o comando executado
    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    dados = (nome, )

    cursor.execute(sql, dados)

    # Confirmar o comento (concretiar o comando de insert)
    conexao.commit()

    # Fechar a conexao com o bando de dados do cursor
    cursor.close()

    print("Categoria criada com sucesso")


def listar_categorias():
    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='mercado'
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome FROM categorias")

    registros = cursor.fetchall()

    cursor.close()

    for registro in registros:
        id = registro[0]
        nome = registro[1]
        print("ID:", id, "\tNome:", nome)


def editar_categoria():
    listar_categorias()

    id = input("Digite o id que seja editar: ")
    nome = input("Digite o novo nome: ")

    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='mercado'
    )

    cursor = conexao.cursor()

    sql = "UPDATE categorias SET nome= %s WHERE id = %s"
    dados = (nome, id)
    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    print("Categoria alterada com sucesso")


def apagar_categoria():
    listar_categorias()

    id = input("Digite o id que deseja apagar: ")

    conexao = connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='joaovcm123',
        database='mercado'
    )

    print("Conexão aberta com sucesso")
    cursor = conexao.cursor()

    print("Apagando categoria")

    sql = "DELETE FROM categorias WHERE id = %s"
    dados  =(id, )
    cursor.execute(sql, dados)

    conexao.commit()

    linhas_afetadas = cursor.rowcount
    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
        print("CAtegoria apagada com sucesso")

    cursor.close()
    conexao.close()