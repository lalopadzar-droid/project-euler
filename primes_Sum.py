primos = 0
cont = 2
es_primo = False
mill = True


while mill:
    ite = 2
    es_primo = True

    while ite * ite <= cont:
        if cont % ite == 0:
            es_primo = False
            break
        ite += 1

    if es_primo:
        primos+=cont
    
    if cont>=2000000:
        mill=False

    cont += 1

print(primos)