a=0
b=0
c=0

for a in range(1,999):
    for b in range(1,999):
        c = 1000-a-b
        if (a**2 + b**2) == c**2:
            q,w,e=a,b,c
            #q,w,e=print(a,b,c)
            break

print(q,w,e)
