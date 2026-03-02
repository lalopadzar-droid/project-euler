lista = []
rev = []
rev2 = []
cont=100
a,b = 100,100

for i in range(100,1000):
    b=100
    for j in range(100,1000):
        res = a * b
        lista.append(str(res))
        b+=1
    a+=1

for i in lista:
    reverse = i[::-1]
    if reverse == i:
        j = int(i)
        rev2.append(j)

maxi = max(rev2)

print(maxi)
