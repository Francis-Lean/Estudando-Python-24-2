nome = str(input("Informe o seu primeiro nome: "))

tamanho = len(nome)

if tamanho >= 1 and tamanho <= 4:
    print("O seu nome é pequeno.")
elif tamanho >= 5 and tamanho <= 6:
    print("O seu nome é normal.")
elif tamanho >= 7:
    print("O seu nome é muito grande.")
elif tamanho == 0:
    print("Você não digitou nada.")
