import math

divisors = 0
suma=1
cont = 1
brek=True

while divisors<500:
    divisors=0
    r=int(math.isqrt(suma))
    for i in range(1,r+1):
        if suma%i==0:
            divisors+=2
            res=suma

    cont+=1
    suma+=cont

print(res)