operacao_1 = 2 + 3 * 5
operacao_2 = (2+3) * 5
operacao_3 = 4 / 2 ** 2 

# Pega o restante da divisão de 13 por 3 e soma com 4
operacao_4 = 13 % 3 + 4 

print(f"Resultado em operacao_1 = {operacao_1}")
print(f"Resultado em operacao_2 = {operacao_2}")
print(f"Resultado em operacao_3 = {operacao_3}")
print(f"Resultado em operacao_4 = {operacao_4}")


#  Uma equação do segundo grau possui a fórmula: y = a*x**2 + b*x + c, onde a, b, c são constantes. O valor de y (resultado) depende do valor de x, ou seja, x é a variável independente e y a dependente. Considerando os valores a = 2, b = 0.5 e c = 1, vamos solicitar para o usuário um valor de x e retornar o valor de y correspondente ao x que ele digitou.

a = 2
b = 0.5
c = 1
x = float(input('Digite o valor de x: '))

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}")
