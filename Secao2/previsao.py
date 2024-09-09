# Analisando o gráficona apostila, desenvolvi um algoritmo que calculasse o valor previsto em relação ao mês desejado.

c = 200 # valor da constante

mes = int(input("Digite o mês que deseja saber o resultado: ")) # Função para captura o mês que o cliente digitar


r = c * mes # Equação do primeiro grau, também chamada função do primeiro grau ou de função linear.

print(f"A quantidade de peças para o mês {mes} será {r}") # Impressão do resultado usando string interpolada "f-strings" (PEP 498)