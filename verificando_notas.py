nota = float(input("Digite a nota do aluno (0-10): "))

if nota >= 7 and nota <= 10:
    print("Aluno aprovado!")
elif nota < 7 and nota >= 1:
    print("Aluno está de recuperação!")
elif nota  == 0:
    print("Aluno reprovado!")
else:
    print("Nota inválida!")
