from imprime_pares import imprime_pares as impp
line = input("Ingresa una linea de numeros, separalos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("el total es:", total)
except:
    print("Error:" + substr+ "no es un numero.")
impp(strings)
