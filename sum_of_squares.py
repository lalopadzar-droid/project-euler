lista = list(range(1,101))
sum_of_squares = sum((map(lambda x:x**2,lista)))
squares_sum = (sum(lista))**2

res = squares_sum - sum_of_squares

print(res)