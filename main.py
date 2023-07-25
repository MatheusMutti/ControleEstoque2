# Programa foi criado em C# originalmente, para fins de prática ele será convertido para Python
#

def print_menu():

    print("[1] Novo\n" + "[2] Listar Produtos\n" + "[3] Consultar Produto\n" + "[4] Entrada Estoque\n" +
          "[5] Saída Estoque\n" + "[6] Checar Quantidades\n" + "[7] Excluir Produto\n" + "[0] Sair\n")


def opcao1():

    nome = input("Informe o nome do produto: ")
    preco = input("Informe o preço: ")
    ano = input("Informe o ano: ")
    qtde = 0
    qtdemin = input("Informe o quantidade mínima: ")
    qtdenax = input("Informe o quantidade máxima: ")

    produto = [nome, preco, ano, qtde, qtdemin, qtdenax]

    ListaProdutos.append(produto)

    print(f"\n{nome} foi adicioado.\n")


def opcao2():

    for i, produto in enumerate(ListaProdutos):
        print(f"Nome: {ListaProdutos[i][0]}")
        print(f"Preço: {ListaProdutos[i][1]}")
        print(f"Ano: {ListaProdutos[i][2]}")
        print(f"Quantidade: {ListaProdutos[i][3]}")
        print(f"Quantidade mínima: {ListaProdutos[i][4]}")
        print(f"Quantidade máxima: {ListaProdutos[i][5]}\n")


def opcao3():

    nomeConsulta = input("Consulta de produtos\nInforme o nome do produto:\n")

    for i, produto in enumerate(ListaProdutos):
        if nomeConsulta == ListaProdutos[i][0]:
            print(f"Nome: {ListaProdutos[i][0]}")
            print(f"Preço: {ListaProdutos[i][1]}")
            print(f"Ano: {ListaProdutos[i][2]}")
            print(f"Quantidade: {ListaProdutos[i][3]}")
            print(f"Quantidade mínima: {ListaProdutos[i][4]}")
            print(f"Quantidade máxima: {ListaProdutos[i][5]}\n")
            break
        else:
            print("Produrando...")
        print(f"{nomeConsulta} não encontrado\n")


def opcao4():

    nomeConsulta = input("Entrada de produtos\nInforme o nome do produto:\n")

    for i, produto in enumerate(ListaProdutos):
        if nomeConsulta == ListaProdutos[i][0]:
            print(f"{ListaProdutos[i][0]} encontrado!\n")
            qtdeEntrada = int(input("Informe a quantidade a dar entrada em estoque:\n"))
            ListaProdutos[i][3] += qtdeEntrada
            break
        else:
            print("Produrando...")

    print("Pesquisa finalizada.\n")


def opcao5():

    nomeConsulta = input("Saída de produtos\nInforme o nome do produto:\n")

    for i, produto in enumerate(ListaProdutos):
        if nomeConsulta == ListaProdutos[i][0]:
            print(f"{ListaProdutos[i][0]} encontrado!\n")
            qtdeSaida = int(input("Informe a quantidade a dar saída em estoque:\n"))
            ListaProdutos[i][3] -= qtdeSaida
            break
        else:
            print("Produrando...")

    print("Pesquisa finalizada.\n")

def opcao6():

    for i, produto in enumerate(ListaProdutos):

        QtdeAtual = int(ListaProdutos[i][3])

        QtdeMinProduto = int(ListaProdutos[i][4])

        QtdeMaxProduto = int(ListaProdutos[i][5])

        Saldo = QtdeAtual - QtdeMinProduto

        if QtdeAtual < QtdeMinProduto:
            print(f"Produto {ListaProdutos[i][0]} está abaixo do mínimo. "
                  f"A quantidade necessária é de {Saldo * -1}.\n")
        else:
            print("Quantidades dentro do definido")


def opcao7():

    nomeConsulta = input("Exclusão de produto\nInforme o nome do produto:\n")

    for i, produto in enumerate(ListaProdutos):
        if nomeConsulta == ListaProdutos[i][0]:
            print(f"{ListaProdutos[i][0]} encontrado!\n")
            ListaProdutos.remove(ListaProdutos[i])
            print(f"{ListaProdutos[i][0]} excluído com sucesso!\n")


def opcao0():
    exit()


if __name__ == '__main__':
    ListaProdutos = []
    while True:

        print_menu()
        opcao_user = int(input(""))

        if opcao_user == 1:
            opcao1()

        elif opcao_user == 2:
            opcao2()

        elif opcao_user == 3:
            opcao3()

        elif opcao_user == 4:
            opcao4()

        elif opcao_user == 5:
            opcao5()

        elif opcao_user == 6:
            opcao6()

        elif opcao_user == 7:
            opcao7()

        elif opcao_user == 0:
            opcao0()
