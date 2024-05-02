# n1 = int(input("Entre com o 1o numero:"))
# n2 = int(input("Entre com o 2o numero:"))
# n3 = int(input("Entre com o 3o numero:"))
#
# if n1>n2:
#     temp = n1
#     n1 = n2
#     n2 = temp
# if n1>n3:
#     temp = n1
#     n1 = n3
#     n3 = temp
# if n2>n3:
#     temp = n2
#     n2 = n3
#     n3 = temp
#
# print(f'Menor:{n1}, Intermediario:{n2}, Maior:{n3}')

n1 = int(input("Entre com o 1o numero:"))
n2 = int(input("Entre com o 2o numero:"))
n3 = int(input("Entre com o 3o numero:"))

if n1>n2:
    n1, n2 = n2, n1
if n1>n3:
    n1, n3 = n3, n1
if n2>n3:
    n2, n3 = n3, n2

print(f'Menor:{n1}, Intermediario:{n2}, Maior:{n3}')
