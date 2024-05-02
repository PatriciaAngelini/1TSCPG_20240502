palavra = input('Digite a palavra para descobrir se é palíndromo\n')
reverso = ''

for letra in palavra:
    reverso = letra + reverso
    print(reverso)
# for i in range(len(palavra), -1, -1):
#     reverso = reverso + palavra[i]

if palavra == reverso:
    print(f'{palavra} é palíndromo')
else:
    print(f'{palavra} não é palíndromo')
