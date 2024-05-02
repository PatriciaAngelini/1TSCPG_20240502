x = True
while x == True:
    c=0
    z = int(input('Insira o numero que deseja verificar\n'))
    for i in (1, 99999):
        if z % i == 0:
            c += 1
    if c == 2:
        print('Numero Primo :)')
    else:
        print(c)
        print('Numero não Primo')
