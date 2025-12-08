from src.repositorios import mercado_produto_repositorio

def executar():
    criar_produto()
    # editar_produto()
    # apagar_produto()
    #listar_produtos()

def criar_produto():
    nome = input("Digite o nome do novo produto: ")
    id_categoria = int(input("Digite o id da categoria: "))

    mercado_produto_repositorio.cadastrar(nome, id_categoria)

    print("Produto criado com sucesso")
    


def editar_produto():
    pass


def apagar_produto():
    listar_produtos()
    id = int(input("Digite o id da categoria para apagar: "))
    linhas_afetadas = mercado_produto_repositorio.apagar(id)

    if linhas_afetadas:
        print("Produto apagado com sucesso")
    else:
        print("Não foi possível apagar o produto")


def listar_produtos():
    produtos = mercado_produto_repositorio.obter_todos()
    print("Código".ljust(8, " "), "Nome".ljust(20, " "), "Categoria")
    for produto in produtos:
        print(
            str(produto["id"]).ljust(8, " "),
            produto["nome"].ljust(20, " "),
            produto["categoria"]["nome"])