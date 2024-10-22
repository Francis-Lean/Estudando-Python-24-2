num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operação = (input("Informe a operação desejada (+ , - , * , /): "))
if operação == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operação == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operação == "*":
    print("{} x {} = {}".format(num1, num2, num1 * num2))
elif operação == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Operação inválida!!!")

