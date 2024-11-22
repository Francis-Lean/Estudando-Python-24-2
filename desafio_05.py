n = int(input("Digite um número inteiro que seja positivo: "))

if n >= 0:
    if n % 2 == 0:
        print("O número {} é um número par.".format(n))
    else:
        print("O número {} é um número impar.".format(n))
else:
    print("O número {} é um número negativo.".format(n))
    