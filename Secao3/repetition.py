#  testar se o número digitado pelo usuário é par ou ímpar. 
# uso do while.

numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número par!")
    else: 
        print("Número ímpar!")


# uso do for
# o Python armazena a string na memória como uma sequência de caracteres. cada um deles tem um índice associado, começando em 0.

nome = "Lucas"

for i, c in enumerate(nome, start=1):
    print(f"Posição = {i}, valor = {c}")


# uso do range, break e continue.
#Para criar uma sequência numérica de iteração em Python, podemos usar a função range().

for x in range(5):
    print(x)

for x in range(1, 10):
    print(x)

# uso do break
disciplina = "Linguagem de programação"

for c in disciplina:
    if c == 'a':
     break
    print(c)
    
    
    
# uso do continue 

disciplina = "Linguagem de programação"

for c in disciplina:
    if c == 'a':
        continue
    else:
        print(c)
        
        
# código para encontrar a posição de uma letra em um texto

texto = "A Era Medieval foi um período de reinos e castelos, onde cavaleiros defendiam suas terras e a Igreja guiava a vida das pessoas. A sociedade era dividida em camadas rígidas, com reis, nobres, camponeses e clérigos, todos desempenhando papéis distintos. Apesar de ser uma época de muitos desafios, com guerras e doenças, também foi um tempo de profundas transformações e da preservação de conhecimentos que moldariam o futuro da Europa."

for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        print(f"Vogal '{c}' encontrada na posição {i}")
    else: 
        continue 