num=1
lista = []
prod=0
maxi=0
res=0
cont=0
#lista.append(num)

while cont<1000000:
    lista.append(num)
    while num!=1:
        if num%2==0:
            num=num/2
        else:
            num=num*3 + 1
        
        lista.append(num)
        
    leng=len(lista)

    if maxi<leng:
        maxi=leng
        res=lista[0]

    lista=[]
    cont+=1
    num=cont

print(res)