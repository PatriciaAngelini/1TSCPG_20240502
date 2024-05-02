#Numeros pares até 600:
# Crie um algoritmo que imprima os
# numeros pares de 1 até 600
titulo = "Numeros pares ate 600"
print(f'{titulo:^30}')
for i in range(1, 601, 1): #comeco, final - 1, pulo
    if i % 2 == 0:
        print(i, end=' ')

for i in range(2, 601, 2): #comeco, final - 1, pulo
    print(i, end=' ')
