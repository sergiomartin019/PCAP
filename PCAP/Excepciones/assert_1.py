import math
x = float(input("Ingresa un número: "))
try:
    assert x >= 0.0
except AssertionError:
    print("el valor tiene que ser mayor que 0")
    exit(1)
x = math.sqrt(x)
print(x)