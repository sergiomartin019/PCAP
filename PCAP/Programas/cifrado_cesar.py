# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ""
shift2 = 0
while True:
    number = int(input("Introduce un numero: "))
    if number > 1 and number < 25:
        for char in text:
            code = ord(char) + number
            primero = ord('A')
            shift2 += (code -primero) % 26
            cipher += chr(primero + shift2)
    else:
        print("El número debe estar entre 1 y 25")
    print(cipher)
