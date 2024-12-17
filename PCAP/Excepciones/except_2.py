try:
    y = 1 / 0
except (ZeroDivisionError, ArithmeticError):
    print("¡División entre cero!")

except:
    print("algo ha cascado aquí...")

print("FIN.")