import math

num = 600851475143
#num = 13195
cont = 2
resp = int(math.sqrt(num))

lista = []
primos = []

while cont<=resp:
    if cont%2 != 0:
        if num%cont == 0:
            lista.append(cont)
    cont+=1

for i in lista:
    conta = 0
    for j in range(3,num):
        if i%j == 0:
            conta+=j
            break

    if conta == i:
        primos.append(i)    

maxi = max(primos)

# print(lista)
# print(primos)
print(maxi)