import math

lista=[]
a=sum(range(1,28124))
total=0
j=1

def divisores(num):
    suma=0
    sumar=[]
    for i in range(1,int(math.isqrt(num)+1)):
        if num%i==0:
            sumar.append(i)
            if i*i != num and i!=1:
                sumar.append(num//i)
    suma=sum(sumar)
    return suma

def abundant(num,suma):
    if num<suma:
        return True
    else:
        return False

num=1

while num<28124:
    while True:
        x = num - j

        if x<j:
            break

        if x+j==num:
            #print(x,j)
            suma1=divisores(x)
            suma2=divisores(j)

            check = abundant(x,suma1)
            check1 = abundant(j,suma2)

        if check and check1:
            total+=num
            break

        j+=1

    num+=1
    j=1
    x=0

hola=a-total

print(hola)