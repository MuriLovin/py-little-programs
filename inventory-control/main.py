import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatPrice(price):
  return locale.currency(price)

def mountMenu(title, options):
    menu = title
    for option in options:
        menu += ' {} \n'.format(option)
    return menu

def showMenu():
    while True:
        try:
            menu_title = "Escolha a opção desejada: \n"
            menu_content = [
                '1. Cadastrar produto',
                '2. Consultar Produto(s)',
                '3. Remover Produto',
                '4. Sair'
            ]

            option_chosen = int(input(mountMenu(menu_title, menu_content)))

            if option_chosen not in [1, 2, 3, 4]:
                print("Opção desconhecida, por favor tente novamente \n")
                continue

            return option_chosen
        except:
            print("Opção invalida, por favor tente novamente \n")
            continue

products = dict()

def cadastrarProduto(code):
    product_name = input("Digite o nome do produto: ")
    product_manufacturer = input("Digite o nome do fabricante: ")

    product_price = 0
    while True:
        try:
            product_price = float(input("Digite o valor(R$) do produto: "))
            break
        except:
            print("Valor invalido. por favor tente novamente \n")

    products[code] = {
        "name": product_name,
        "manufacturer": product_manufacturer,
        "price": product_price
    }

    print("Produto Cadastrado com sucesso! \n")

def consultarProduto():
    while True:
        try:
            menu_title = "Escolha a opção desejada: \n"
            menu_content = [
                '1 - Consultar todos os produtos',
                '2 - Consultar Produto por Código',
                '3 - Consultar Produto(s) por Fabricante',
                '4 - Retornar'
            ]

            option_chosen = int(input(mountMenu(menu_title, menu_content)))

            if option_chosen not in [1, 2, 3, 4]:
                print("Opção desconhecida, por favor tente novamente \n")
                continue

            return option_chosen
        except:
            print("Opção invalida, por favor tente novamente \n")
            continue

def removerProduto():
    product_code_chosen = 0
    while True:
        try:
            product_code_chosen = int(input("Digite o Código do Produto a ser removido: "))
            products.pop(product_code_chosen)
            print("Produto removido com sucesso")
            break
        except KeyError:
            print("Produto não encontrado \n")
            return
        except ValueError:
            print("Valor invalido. por favor tente novamente \n")

def showConsultType(type):
    if (type == 1):
        for code, product in products.items():
            print(f'Código: {code}')
            print(f'Nome: {product["name"]}')
            print(f'Fabricante: {product["manufacturer"]}')
            print(f'Valor: {formatPrice(product["price"])} \n')

        return
    if (type == 2):
        product_code_chosen = 0
        while True:
            try:
                product_code_chosen = int(input("Digite o Código do Produto: "))
                break
            except:
                print("Valor invalido. por favor tente novamente \n")

        product_founded = products.get(product_code_chosen)

        if (product_founded == None):
            print("Produto não encontrado \n")
            return

        print(f'Código: {product_code_chosen}')
        print(f'Nome: {product_founded["name"]}')
        print(f'Fabricante: {product_founded["manufacturer"]}')
        print(f'Valor: {formatPrice(product_founded["price"])} \n')

        return
    if (type == 3):
        product_manufacture_chosen = input("Digite o fabricante do(s) Produto(s): ").lower()
        for code, product in products.items():
            manufacture = product['manufacturer'].lower()

            if (manufacture != product_manufacture_chosen):
                continue

            print(f'Código: {code}')
            print(f'Nome: {product["name"]}')
            print(f'Fabricante: {product["manufacturer"]}')
            print(f'Valor: {formatPrice(product["price"])} \n')

        return
    if (type == 4):
        return

print("Bem vindo ao programa de controle de estoque")

product_identifier = 0

while True:
    option_chosen = showMenu()

    if (option_chosen == 1):
        cadastrarProduto(product_identifier)
        product_identifier += 1
        continue

    if (option_chosen == 2):
        consult_type_chosen = consultarProduto()
        showConsultType(consult_type_chosen)
        continue

    if (option_chosen == 3):
        removerProduto()
        continue

    if (option_chosen == 4):
        print("Finalizando programa...")
        break