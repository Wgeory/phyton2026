g=input("digete o genero (M - masculino / F - femino)").upper()
i=int(input("digete a idade"))
print(f"sexo {g} idade {i}")
if g == "M" and i >=18:
    print("candidato apto a se alistar")
else:
    print("não apto")