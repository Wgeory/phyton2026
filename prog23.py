n1=int(input("digete um valor"))
n2=int(input("digete outro valor"))
print('("1 - somar")')
print('("2 - subtrair")')
print('("3 - multiplicar")')
print('("3 - dividir")')
e=input("digete uma das opções acima para operações")
match e:
    case "1":
        o=n1+n2
    case "2":
        o=n1-n2
    case "3":
        o=n1*n2
    case "4":
        o=n1/n2
    case _:
        o=0
        print("opção ivalida")
print(f"o resultado da operção é {o}")
print("teste de commit")
print("teste push")