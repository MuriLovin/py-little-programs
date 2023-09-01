import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

stock = {
    21: {
      'flavor': 'Napolitana',
      'price': {
        'medium': 20.00,
        'large': 26.00
      }
    },
    22: {
      'flavor': 'Margherita',
      'price': {
        'medium': 20.00,
        'large': 26.00
      }
    },
    23: {
      'flavor': 'Calabresa',
      'price': {
        'medium': 25.00,
        'large': 32.50
      }
    },
    24: {
      'flavor': 'Toscana',
      'price': {
        'medium': 30.00,
        'large': 39.00
      }
    },
    25: {
      'flavor': 'Portuguesa',
      'price': {
        'medium': 30.00,
        'large': 39.00
      }
    }
  }

def formatPrice(price):
  return locale.currency(price)

def showMenu():
  print('-' * 34, 'Cardápio', '-' * 34)

  menu_header = ['Código', 'Descrição', 'Pizza Média - M', 'Pizza Grande - G (30% mais cara)']

  print(f'| {menu_header[0]:<8} | {menu_header[1]:<10} | {menu_header[2]:<8} | {menu_header[3]:<8} |')

  for key, pizza in stock.items():
    code = key
    description = pizza['flavor']
    price_medium = formatPrice(pizza["price"]["medium"])
    price_large = formatPrice(pizza["price"]["large"])

    print(f'| {code:<8} | {description:<10} | {price_medium:<15} | {price_large:<32} |')

  print('-' * 78, '\n')

def calculateTotal(code, lentgh):
  client_flavor = stock.get(code)
  flavor_price_medium = client_flavor['price']['medium']
  flavor_price_large = client_flavor['price']['large']

  if (lentgh == 'G'):
    return flavor_price_large

  return flavor_price_medium

print('Bem vindo a pizzaria')

total_payable = 0;

while True:
  showMenu();

  pizza_length = input('Qual o tamanho de pizza que deseja (M/G): ').upper()

  if (pizza_length not in 'GM'):
    print('opção invalida \n')
    continue

  flavor_code = int(input('Qual o sabor da pizza? digite o código do menu: '))

  if (flavor_code not in stock):
    print('opção invalida \n')
    continue

  total_payable += calculateTotal(flavor_code, pizza_length)

  flavor_chosen = stock.get(flavor_code);

  print(f'Você pediu uma Pizza {flavor_chosen["flavor"]} \n')

  new_order = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 2 - Não \n'))

  if (new_order not in [1, 2]):
    print('opção invalida \n')
    print("Finalizando o programa...")
    break #

  if (new_order == 2):
    print(f'O total a ser pago é: {formatPrice(total_payable)}')
    break
