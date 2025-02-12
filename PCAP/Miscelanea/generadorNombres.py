import random
def generadorNombres():
    listaNombres = ["xXx_miguelito777_xXx", "elver galarga54", "pepe", "pOtAxiAna", "elrincondemario"]
    random.shuffle(listaNombres)
    for nombre in listaNombres:
        yield nombre
        
generador = generadorNombres()

for _ in range(5):
    print(next(generador))
        
print(next(generador) for _ in range(5))