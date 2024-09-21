import os
import time

class Codigos:
    codigo: int
    nome: str
    descricao: str
    preco_compra: float
    preco_venda: float

def ProdutoComoTexto(c: Codigos) -> str:
    return (f"{c.codigo};{c.nome};{c.descricao};{c.preco_compra};{c.preco_venda}\n")


def TextoComoProduto(s: str) -> Codigos:
    codigo, nome, descricao, preco_compra, preco_venda = s.split(";")
    c = Codigos()
    c.codigo = int(codigo)
    c.nome = (nome)
    c.descricao = (descricao)
    c.preco_compra = float(preco_compra)
    c.preco_venda = float(preco_venda)
    return c


def CadastrarProduto() -> Codigos:
    os.system("cls")
    try:
        c = Codigos()
        print("Cadastrando produto...")
        c.codigo = int(input("Defina o código do produto: "))
        c.nome = str(input("Defina o nome do produto: "))
        c.descricao = str(input("Defina a descrição do produto: "))
        c.preco_compra = float(input("Defina o preço de compra do produto: "))
        c.preco_venda = float(input("Defina o valor de venda do produto: "))
        codigos.append(c)
        SalvarProduto(c)
        print("Produto cadastrado com sucesso. Tecle Enter para prosseguir:")
        time.sleep(0.1)
    except ValueError:
        while True:
            print("Dados inválidos.")
            print("1 - Tentar novamente")
            print("2 - Menu principal")
            option = input()
            if option == "1":
                CadastrarProduto()
            elif option == "2":
                break
            else:
                print("Opção inválida. Tecle Enter para retornar ao Menu principal.")
            input()
            break
    input("Aperte ENTER")

def SalvarProduto(c: Codigos):
    f = open("produtos.txt", "a+", encoding="UTF8")
    f.write(ProdutoComoTexto(c))
    f.close()


def imprimirProduto(c: Codigos):
    print(f"Código: {c.codigo}")
    print(f"Nome: {c.nome}")
    print(f"Descrição: {c.descricao}")
    print(f"Preço de compra : R${c.preco_compra:.2f}")
    print(f"Preço de venda: R${c.preco_venda:.2f}")
    lucro = c.preco_venda - c.preco_compra
    if lucro > 0:
        print(f"Lucro estimado por venda: R${lucro:.2f}")
        print("-"*40)
    else:
        print(f"Prejuízo estimado por venda: R${lucro:.2f}")
        print("-"*40)


def ListarProduto():
    os.system("cls")
    f = open("produtos.txt", "r", encoding="UTF8")
    print("-"*40)
    print("        PRODUTOS CADASTRADOS: ")
    print("-"*40)
    try:
        for linha in f:
            produto = TextoComoProduto(linha)
            imprimirProduto(produto)
        input()
    except:
        while True:
            print("Nenhum produto cadastrado. Escolha uma opção.")
            print("1 - Cadastrar Produto")
            print("Enter - Menu principal")
            option = input()
            if option == "1":
                CadastrarProduto()
            else:
                break

class Compras:
    quantidade : int
    dia : int
    mes : int
    ano : int
    subtotal : float

def CompraComoTexto(q: Compras, c: Codigos) -> str:
    return(f"{q.quantidade};{c.nome};{c.preco_compra};{q.dia};{q.mes};{q.ano};{q.subtotal}\n")

def TextoComoCompra(a: str) -> Compras:
    subtotal, dia, mes, ano, quantidade, nome, preco_compra = a.split(";")
    q = Compras()
    c = Codigos()
    q.quantidade = int(quantidade)
    q.subtotal = subtotal
    q.dia = dia
    q.mes = mes
    q.ano = ano
    c.nome = nome
    c.preco_compra = float(preco_compra)
    return c and q

def ExecutarCompra():
    os.system("cls")
    try:
        q = Compras()
        compra = int(input("Insira o código do produto cadastrado: "))
        c = next((p for p in codigos if p.codigo == compra), None)
        if c is None:
          print("Produto não encontrado. Tente novamente.")
          return
        input("Produto selecionado com sucesso. Tecle Enter para prosseguir: ")
        q.quantidade = int(input("Insira q quantidade a ser comprada: "))
        q.dia = int(input("Digite o dia da compra: "))
        q.mes = int(input("Digite o mês da compra: "))
        q.ano = int(input("Digite o ano da compra: "))
        ano_bissexto = (q.ano % 4 == 0 and q.ano % 100 != 0) or q.ano % 400 == 0
        fevereiro = q.mes == 2
        mes_30 = q.mes in [4, 6, 9, 11]
        while True:
            if q.mes < 1 or q.mes > 12:
                print("Data inválida (mês fora do intervalo 1-12!)")
                break
            elif q.dia < 1:
                print("Data inválida (dia negativo!)")
                break
            elif (mes_30 and q.dia > 30) or (not mes_30 and q.dia > 31):
                print("Data inválida (dia fora do intervalo para o mês dado!)")
                break
            elif fevereiro and ano_bissexto and q.dia > 29:
                print("Data inválida (dia maior que 29 em fevereiro de um ano bissexto!)")
                break
            elif fevereiro and not ano_bissexto and q.dia > 28:
                print("Data inválida (dia maior que 28 em fevereiro de um ano não bissexto!)")
                break
            else:
                print(f"{q.dia}/{q.mes}/{q.ano}")
                print("Data válida")
                q.subtotal = q.quantidade * c.preco_compra
                print("Item adicionado a lista de compras com sucesso.")
                input("Tecle Enter para prosseguir...")
                compras.append(q)
                SalvarCompra(q, c)
                break
    except ValueError:
        while True:
            print("Dados inválidos, a quantidade deve ser um número.")
            print("1 - Tentar novamente")
            print("Enter - Menu principal")
            opcao = input()
            if opcao == "1": ExecutarCompra()
            else: break

def SalvarCompra(q: Compras, c: Codigos):
    f = open("compras.txt", "a+", encoding="UTF8")
    f.write(CompraComoTexto(q, c))
    f.close()

def ImprimirCompra(c: Codigos, q: Compras):
    q.subtotal = q.quantidade * c.preco_compra
    print(f"Produto: {c.codigo}")
    print(f"Nome: {c.nome}")
    print(f"Quantidade comprada: {q.quantidade}")
    print(f"Subtotal: R${q.subtotal}")

def listarCompra():
    os.system("cls")
    f = open("compras.txt", "r", encoding="UTF8")
    print("-"*40)
    print(" Lista de Compras ")
    print("-"*40)
    try:
        for linha in f:
            compra = CompraComoTexto(linha)
            ImprimirCompra(compra)
        input()
    except:
        while True:
            print("Nenhuma Compra registrada. Selecione uma opção:")
            print("1- Comprar produto")
            print("Enter - Menu inicial")
            opcao = input()
            if opcao == "1": ExecutarCompra()
            else: break

codigos = []
compras = []
while True:
    os.system("cls")
    q = Compras
    c = Codigos
    print("--------------- Menu Principal ---------------")
    print("Escolha uma opção: ")
    print("1 - Cadastrar Produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Listar Compras")
    print("5 - Vender produto")
    print("6 - Encerrar")
    option = input()
    if option == "1":
        CadastrarProduto()
    elif option == "2":
        ListarProduto()
    elif option == "3":
        ExecutarCompra()
    elif option == "4":
        listarCompra()
    elif option == "6":
        break
    else:
        input("opcao inválida. Tecle Enter para prosseguir: ")