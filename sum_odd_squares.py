rango = [i for i in range(1,224000) if i%2!=0]
square = sum(list(map(lambda x:x**2,rango)))

print(square)