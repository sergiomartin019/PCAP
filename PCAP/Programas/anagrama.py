while True:
    text1 = input("Introduce la primera palabra: ").upper()
    if not text1.isalpha():
        print("Error: " + text1 + " no es una cadena alfabetica")
        break;
    else:
        text2 = input("introduce la segunda palabra: ").upper()
        if not text2.isalpha():
            print("Error: " + text2 + " no es una cadena alfabetica")
        break;

if sorted(text1) == sorted(text2):
    print("Las palabras son anagramas")
        

    
        