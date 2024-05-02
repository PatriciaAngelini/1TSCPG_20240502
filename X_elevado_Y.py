# 2 elevado a 4
base = int(input("Entre com o numero base a ser elevado"))
exponenciacao = int(input("Entre com a exponenciacao "))
# base = 2
# exponenciacao = 4
total = 1
count = 1
while count <= exponenciacao:
    total = total * base
    # total = total(1) * 2  = 2 # total = total(2) * 2  = 4
    # total = total(4) * 2  = 8 # total = total(8) * 2  = 16
    count = count + 1
print(f'{base} elevado {exponenciacao} é {total}')

total = 1
for i in range(exponenciacao):
    total = total * base
print(f'{base} elevado {exponenciacao} é {total}')










def calcular_potencia(x,y):
    resultado = 1
    for _ in range(y):
        resultado *= x
    return resultado

x = int(input("Digite o valor de X: "))
y = int(input('Digite o valor de Y:'))

if x > 1 and y >= 2:
    print(f'{x} elevado a {y} = {calcular_potencia(x,y)}')
else:
    print('X deve ser maior que 1 e Y deve ser inteiro maior ou igual a 2.')
