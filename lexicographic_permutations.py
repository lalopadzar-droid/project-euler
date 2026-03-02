import itertools

lista = [0,1,2,3,4,5,6,7,8,9]
perms=[]
cont=1

perms=itertools.permutations(lista)

for p in perms:
    cont+=1
    if cont>1000000:
        print(f"{cont}: {p}")
        break