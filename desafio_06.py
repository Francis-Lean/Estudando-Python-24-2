altura = float(input("Informe a sua altura: "))
sexo = str(input("Informe o seu sexo: "))

peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7

if sexo == "h" or sexo == "H":
    print("Sendo Homem e medindo {:.2f} de altura, o seu peso "
          "ideal é {:.2f} Kg.".format(altura, peso_ideal_h))
elif sexo == "m" or sexo == "M":
    print("Sendo mulher e medindo {:.2f} de altura, o seu peso "
          "ideal é {:.2f} Kg.".format(altura, peso_ideal_m))
else:
    print("VALOR INVÁLIDO")