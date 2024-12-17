def read_int(prompt, min, max):
    while True:
        try:
            numero = int(input(prompt))
            if numero < min or numero > max:
                raise Exception
            else:
                return numero

        except ValueError:
            print("Error: entrada incorrecta")
            
        
        except Exception:
            print("Error: el valor no está dentro del rango permitido (-10..10)")

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)