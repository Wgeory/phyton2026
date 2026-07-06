nome = input("digete um nome")
not1 = float(input("digete a primeira nota"))
not2 = float(input("digete a segunda nota"))
not3 = float(input("digete a terceira nota"))
not4 = float(input("digete a quarta nota"))
m = (not1+not2+not3+not4)/4
if m >= 6:
    print("aprovado")
    print("que sorte")
else:
    print("recuperação")
    print("que azar")
print(f"{nome}sua media é: {m}")