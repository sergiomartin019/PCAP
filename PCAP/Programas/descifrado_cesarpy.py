# Cifrado César - descifrando un mensaje.
cipher = input('Ingresa tu criptograma: ')
text = ''
espacio = " "
for char in cipher:
    if not char.isalpha():
        if char is espacio:
            text += espacio
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)