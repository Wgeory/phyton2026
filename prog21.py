opção = int(input("digete uma opção"))

match opção:
    case 1:
        print("você escolheu a opção 1: ver saldo.")
    case 2:
        print("você escolheu a opção 2: fazer saque.")
    case 3:
        print("você escolheu a opção 3: falar com atendente.")
    case _:
        print("opção invalida! escolha um número de 1 a 3.")