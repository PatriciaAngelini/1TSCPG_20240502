# resp = 's'
# while resp in ('s', 'sim'):
#     x = 0
#     numero = int(input(f'Insira o numero que deseja verificar\n'))
#     for i in range(1, numero+1):
#         if numero % i == 0:
#             x += 1
#     if x == 2:
#         print('Numero Primo :)')
#     else:
#         print('Numero não Primo')
#     resp = input("Deseja consultar outro numero: ").lower()

primo = True
numero = int(input(f'Insira o numero que deseja verificar\n'))
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print(f'{numero} é primo')
else:
    print(f'{numero} nao é primo')

