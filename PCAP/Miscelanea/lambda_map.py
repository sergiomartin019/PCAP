lista_numerica = [x for x in range(5)]

lista_cuadrados = list(map(lambda x: 2 ** x, lista_numerica))

print(lista_cuadrados)

for x in map(lambda x: x * x, lista_cuadrados):
    print(x, end=" ")
print()