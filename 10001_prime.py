primos = []
cont = 2
es_primo = False


while len(primos) < 10001:
    ite = 2
    aaa=2
    es_primo = True

    while aaa * ite <= cont:
        if cont % ite == 0:
            es_primo = False
            break
        ite += 1
        aaa +=1

    if es_primo:
        primos.append(cont)

    cont += 1

print(primos[-1])