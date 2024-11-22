palabra = input("Introduce una palabra a buscar ").upper()
grupo = input("Introduce grupo de caracteres ").upper()

contiene = True
posicion = 0
for c in palabra:
    posicion = grupo.find(c)
    if posicion < 0:
        contiene = False
        break;
    else:
        
        continue
print(contiene)
        