# Estrura lógicas em python: AND, OR, NOT

# Um aluno só pode ser aprovado caso ele tenha menos de 5 faltas e média final superior a 7.

qtdefaltas = int(input("Digite a quantidade de faltas: "))
mediaFinal = float(input("Digite a média final: "))

if qtdefaltas <= 5 and mediaFinal >= 7:
    print("Aluno aprovado!")
else: 
    print("Aluno reprovado!")

# Python avalia expressões lógicas e retorna true ou false automaticamente 
 
A = 15
B = 9
C = 9

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C )



