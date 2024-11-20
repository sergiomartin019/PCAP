fecha = ""
while True:
    fecha = input("Ingrese la fecha de nacimiento (AAAA/MM/DD): ")
    if fecha.isnumeric() and len(fecha) == 8:
        break;
    
digito = 0
suma = 0;

for char in fecha:
    suma += int(char)

if suma <10:
    digito = suma
else:
    for c in str(suma):
        digito = digito + int(c)

print("el digito es", digito)