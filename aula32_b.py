hora = int(input("informe a hora atual: "))
if hora >= 0 and hora <= 11:
    print("Bom dia usuário!")   
elif hora >= 12 and hora <= 17:
    print("Boa tarde usuário!")
elif hora >= 18 and hora <= 23:
    print("Boa noite usuário!")

