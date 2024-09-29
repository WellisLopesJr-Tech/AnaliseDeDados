a = 2 
b = 1

equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\ A entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}") 
    
# A função eval() recebe como entrada umm string (sequencia de caracteres) digitada pelo usuário;
# Essa entrada é analisada e aavaliada como uma expressão python pela função eval();
# range() cria uma sequência númerica;