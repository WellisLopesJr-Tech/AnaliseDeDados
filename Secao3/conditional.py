a = 5
b = 10

if a < b: 
    print("a é menor do que b")
    r = a + b
    print(f"a soma de a + b é {r}")

a = 5
b = 10

if a < b: 
    print("a é menor do que b")
    r = a + b
    print(r)
else:
    print("a é maior do que b")
    r = a - b
    print(r)

# uso do elif

codigo_compra = 5111

if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazoo no boleto.")
elif codigo_compra == 5444: 
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado!")



