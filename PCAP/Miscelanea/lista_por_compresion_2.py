mi_lista = []

for n in range(11):
    mi_lista.append(0 if n %2 == 0 else 1)
print(mi_lista)

mi_lista = [0 if n %2 == 0 else 1 for n in range(11)]

print(mi_lista)