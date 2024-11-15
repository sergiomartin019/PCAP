palabra = input("introduce una palabra: ")
palabra = palabra.lower().replace(' ','')
if palabra == palabra[::-1]:
    print("la palabra es palindroma")

else:
    print("la palabra no es palindromo")
    