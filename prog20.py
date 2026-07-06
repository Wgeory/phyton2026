cargo = input("digete o cargo do funcionário caixa / vendedor / gerente:").lower()
if cargo == "caixa":
    salario = 1500
elif cargo == "vendedor":
    salario = 2400
elif cargo == "gerente":
    salario = 4000
else:
    salario = 0
    print("cargo inválido! Use: caixa,vendedor ou gerente")
    exit()
inss = salario * 0.12
if salario >2000:
    irrf = salario *0.14
else:
    irrf = salario *0.08
salario_final=salario-inss-irrf
print(f"querido seu cargo.de {cargo} tem o salario de {salario} e os impostos são:")
print(f"inss -> {inss}")
print(f"irrf -> {irrf}")
print(f"seu salário final é {salario_final}")