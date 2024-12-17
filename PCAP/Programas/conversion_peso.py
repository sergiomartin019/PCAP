peso = float(input("INTRODUCE TU PESO: "))
tipo = input("¿¿En lb o kg?? Introduzca l o k: ").lower()

if tipo == "l":
    peso = peso * 0.45;
    print(f"su peso en kg es {peso}")
elif tipo == "k":
    peso = peso / 0.45
    print(f"su peso en libras es {peso}")
else:
    print("no ha introducido algunos de los datos bien")

