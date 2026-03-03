import pickle
from dataclasses import dataclass
@dataclass
class Produto:
    ID: int
    NAME: str
    QUANTIDADE: int
    PRECO: float
lista = []
class ProdutoSubClass:
    def UpdateNome(Produto):
        new_name = input("New name: ")
        Produto.NAME= new_name
    def UpdateQuantidade(Produto):
        new_quantidade = input("New quantity: ")
        Produto.QUANTIDADE= new_quantidade
    def UpdatePreco(Produto):
        new_preco = input("New price: ")
        Produto.PRECO = new_preco

def main_menu():
    print ("Menu de navegaçao:")
    print("1. Adicionar produto novo")
    print("2. Editar produto existente")
    print("3. Ver Produtos")
    choice = int(input("Qual a tua escolha:"))
    if choice == 1:
        add_stock()
    if choice == 2:
        update_produto() 
    if choice == 3:
        ver_produtos()


def add_stock():
    name = input("qual nome do produto: ")
    quantidade = int(input("qual a quantidade:"))
    preco = float(input("qual o preco: "))
    new_produto = Produto(len(lista)+1, name, quantidade,preco)
    lista.append(new_produto)
    main_menu()

def ver_produtos():
    try:
        with open('stocks.dat', 'rb') as f:
            produtos = pickle.load(f)

        if not produtos:
            print("Não há produtos registados.")
            return

        print("\nProdutos em stock:")
        for p in produtos:
            print(f"ID: {p.ID} | Nome: {p.NAME} | Quantidade: {p.QUANTIDADE} | Preço: {p.PRECO}")

    except FileNotFoundError:
        print("Ficheiro de stock não existe.")
    main_menu()


def update_produto():
    id=int(input("Qual o prodotu que queres editar (ID)"))
    print(lista[id-1])
    x = int(input("queres mudar o nome (1) mudar a quantidade (2) mudar o preço (3)"))
    if x == 1:
        ProdutoSubClass.UpdateNome(lista[id-1])
    if x ==2:
        ProdutoSubClass.UpdateQuantidade(lista[id-1])
    if x ==3:
        ProdutoSubClass.UpdatePreco(lista[id-1])


        
with open('stocks.dat', 'rb') as f:
    lista.extend(pickle.load(f))

main_menu()
with open('stocks.dat', 'wb') as f:
    pickle.dump(lista, f)

ver_produtos()






