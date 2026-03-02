total=0
suma=0

#efficient limit 354294, above this the fifth power doesnt applies

for i in range(2,1000000):
    stri=str(i)
    for j in stri:
        suma+=int(j)**5

    if suma==int(stri):
        total+=int(stri)
    suma=0
        
print(total)