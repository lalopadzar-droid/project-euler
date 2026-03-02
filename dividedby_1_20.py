import math ########no se pudo

cont = 0
ite = 1

while True:
    for i in range(1,21):
        if ite%i==0:
            cont+=1

    if cont==20:
        break
    else:
        ite+=20
        cont=0


print(ite)





    # ite+=1
    # if ite%2==0:
    #     if ite%3==0:
    #         if ite%4==0:
    #             if ite%5==0:
    #                 if ite%6==0:
    #                     if ite%7==0:
    #                         if ite%8==0:
    #                             if ite%9==0:
    #                                 if ite%10==0:
    #                                     if ite%11==0:
    #                                         if ite%12==0:
    #                                             if ite%13==0:
    #                                                 if ite%14==0:
    #                                                     if ite%15==0:
    #                                                         if ite%16==0:
    #                                                             if ite%17==0:
    #                                                                 if ite%18==0:
    #                                                                     if ite%19==0:
    #                                                                         if ite%20==0:
    #                                                                             break


###respuestas correctas:
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

resultado = 1

for i in range(1, 21):
    resultado = (resultado * i) // gcd(resultado, i)

print(resultado)


# for i in range(1,21):
#     ite = math.lcm(ite, i)