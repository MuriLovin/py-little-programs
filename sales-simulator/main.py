def calculateDiscount(price, discount = False):
  if (discount):
    return price * discount

  return price

run = True

print('Bem vindo ao Simulador de Vendas')

while run:
  discount_minimum = 0
  discount_medium = 0.03
  discount_high = 0.06
  discount_master = 0.1

  product_price_input = input('Digite o valor do produto: R$ ')
  product_quantity = int(input('Digite a quantidade do produto: '))

  product_price = float(product_price_input.replace(',', '.'))

  total_without_discount = product_price * product_quantity

  print(f'O valor sem desconto foi: R$ {total_without_discount:.2f}')

  if (product_quantity <= 4):
    total_with_discount = total_without_discount - calculateDiscount(total_without_discount)

  elif (product_quantity >= 5 and product_quantity <= 19):
    total_with_discount = total_without_discount - calculateDiscount(total_without_discount, discount_medium)

  elif (product_quantity >= 20 and product_quantity <= 99):
    total_with_discount = total_without_discount - calculateDiscount(total_without_discount, discount_high)

  else:
    total_with_discount = total_without_discount - calculateDiscount(total_without_discount, discount_master)

  print(f'O valor sem desconto foi: R$ {total_with_discount:.2f} \n')

  continue_running = input("Deseja realizar outra operação? (S/N) ").upper()

  if (continue_running == 'S'):
    continue

  elif (continue_running == 'N'):
    print('Finalizando o programa, obrigado e volte sempre')
    run = False

  else:
    print("Comando desconhecido. Finalizando o programa!")
    run = False