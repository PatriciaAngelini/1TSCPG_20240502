# frase = input('Digite a frase para descobrir o Nº de vogais e consoantes\n').lower()
# nvogais = 0
# nconsoantes = 0
# vogais = ['a', 'i', 'u', 'e', 'o']
#
# for i in frase:
#     if i in vogais:
#         nvogais += 1
#     if i != ' ' and i not in vogais:
#         nconsoantes += 1
#
# print(f'A sua frase tem {nvogais} vogais e {nconsoantes} consoantes')


frase = input('Digite a frase para descobrir o Nº de vogais e consoantes\n')
nvogais = 0
nconsoantes = 0


for i in frase:
    if i in 'aeiouAEIOU':
        nvogais += 1
    elif i != ' ':
        nconsoantes += 1 # nconsoantes = nconsoantes + 1

print(f'A sua frase tem {nvogais} vogais e {nconsoantes} consoantes')
