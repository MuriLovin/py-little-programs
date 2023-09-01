import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatPrice(price):
  return locale.currency(price)

def volumeFeijoada():
    while True:
        try:
            portion_volume = float(input("Digite o volume desejado(ml): "))

            if portion_volume >= 300 and portion_volume <= 5000:
                return portion_volume * 0.08

            else:
                print("Não aceitamos porções menores que 300ml ou maiores que 5000ml. Tente novamente! \n")
                continue
        except:
            print("Valor inválido \n")

def opcaoFeijoada():
    while True:
        option_basic = 'b - Básica (Feijão + paiol + costelinha) \n'
        option_premium = 'p - Premium (Feijão + paiol + costelinha + partes de porco) \n'
        option_supreme = 's - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon) \n'

        option = input(f"Digite a opção desejada: \n {option_basic} {option_premium} {option_supreme}").lower().strip()

        if option == 'b':
            return 1

        elif option == 'p':
            return 1.25

        elif option == 's':
            return 1.50

        else:
            print('Você digitou uma opção inválida \n')

def acompanhamentoFeijoada():
    accompaniment_final_price = 0

    while True:
        exit = '0 - Não desejo mais acompanhamentos (encerrar pedido) \n'
        rice = '1 - 200g de arroz \n'
        crumbs = '2 - 150g de farofa especial \n'
        cabbage = '3 - 100g de couve cozida \n'
        orange =  '4 - 1 laranja descascada \n'

        try:
            accompaniment = int(input(f"Deseja mais um acompanhamento? \n {exit} {rice} {crumbs} {cabbage} {orange}"))

            if accompaniment == 0:
                return accompaniment_final_price

            if accompaniment == 1:
                accompaniment_final_price += 5.00

            elif accompaniment == 2:
                accompaniment_final_price += 6.00

            elif accompaniment == 3:
                accompaniment_final_price += 7.00

            elif accompaniment == 4:
                accompaniment_final_price += 3.00

            else:
                print("Acompanhamento indisponível. Selecione outra opção \n")

        except:
            print("Valor inválido \n")

def realizarNovoPedido():
    while True:
        continue_running = input("Deseja realizar outro pedido? (S/N) ").upper().strip()

        if continue_running == 'S':
            return True

        if continue_running == 'N':
            return False

        print("Opção desconhecida")

print("Bem vindo ao restaurante que só vende feijoada")

while True:
    volume_chosen = volumeFeijoada();
    option_chosen = opcaoFeijoada();
    accompaniment_chosen = acompanhamentoFeijoada();

    total_payable = (volume_chosen * option_chosen) + accompaniment_chosen

    print(f"O valor a ser pago é: {formatPrice(total_payable)} \n")

    print(f"Formula de cálculo da conta: (volume = {formatPrice(volume_chosen)} * opção = {option_chosen}) + acompanhamento = {formatPrice(accompaniment_chosen)} \n")

    if realizarNovoPedido():
        continue

    print('Finalizando programa')
    break
