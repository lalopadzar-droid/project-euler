a,b=1,1
leng=0
cont=1

while leng!=1000:
    a,b = b,a+b
    leng=len(str(a))
    cont+=1
    int(a)

print(cont,":",a)

