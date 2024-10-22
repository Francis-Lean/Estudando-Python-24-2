num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num3:
    print("O maior número é o {}".format(num1))
elif num2 > num3 and num1:
    print("O maior número é o {}".format(num2))
else:
    print("O maior número é o {}".format(num3))
