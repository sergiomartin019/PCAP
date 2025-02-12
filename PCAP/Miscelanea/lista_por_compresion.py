lista_1 = []

for n in range(6):
    lista_1.append(10 ** n)
    
lista_2 = [10 ** n for n in range(6)]

print(lista_1)
print(lista_2)