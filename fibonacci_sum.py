a,b = 1,1
lista = []
cont = 0
res = 0

# for i in range(4000000):
#     a,b = b,a+b
#     if a%2==0:
#         lista.append(a)
while a < 4000000:
    if a%2 == 0:
        res+=a
    a,b = b,a+b
    cont+=1

#print(lista)
print(res)