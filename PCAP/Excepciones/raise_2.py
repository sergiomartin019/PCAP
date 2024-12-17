def mal_asunto(n):
    try:
        return n / 0
    except:
        print("Lo hice otra vez")
        raise ValueError
try:
    mal_asunto(0)
except ValueError:
    print("error de valor")
except ArithmeticError:
    print("¿Qué ha pasado?")
    exit(0)
print("FIN.")