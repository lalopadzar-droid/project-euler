cont=1
listaA=[]
listaB=[]
amicable=[]
sumA=0
sumB=0

while cont<10000:
    for i in range(1,cont+1):
        if cont%i==0 and cont!=i:
            listaA.append(i)
    sumA=sum(listaA)

    for j in range(1,sumA+1):
        if sumA%j==0 and sumA!=j:
            listaB.append(j)
    sumB=sum(listaB)

    if sumB==cont and sumA!=sumB:
        amicable.append(sumB)
    
    listaA=[]
    listaB=[]
    sumA,sumB=0,0
    cont+=1

print(amicable)
sumC=sum(amicable)
print(sumC)