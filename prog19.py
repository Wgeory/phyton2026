idade = int(input("digete a idade do visitante:"))
resposta = input("o visitante possui ingresso? s/n:").upper()
tem_ingresso = resposta == "s"
if idade >= 12 and tem_ingresso:
    print("acesso liberado! divirta-se no brinquedo.")
elif tem_ingresso and idade <12:
    print("voce tem o ingresso,mas não tem a idade minima de 12 anos.")
else:
    print("acesso negado. você precisa de um ingresso.")