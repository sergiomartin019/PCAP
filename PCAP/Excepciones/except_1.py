try:
    y = 1 / 0
    
except ZeroDivisionError:
    print("¡División entre cero!")
    
except ArithmeticError:
    print("¡Problema Aritmético!")
except:
    print("algo ha cascado aquí...")

print("FIN.")