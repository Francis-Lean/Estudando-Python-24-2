idade = int(input("Digite sua idade: "))
if idade >= 18 and idade < 60:
    print("Você é maior de idade.")
elif idade >= 60:
    print("Você é idoso.")
else:
    print("Você é menor de idade.")
