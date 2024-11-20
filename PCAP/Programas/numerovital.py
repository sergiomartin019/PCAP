fecha = ""
while True:
    fecha = input("Ingrese la fecha de nacimiento (AAAA/MM/DD): ")
    if fecha.isnumeric():
        break;
    
digito = 0
suma = 0;

for char in fecha:
    digito = int(char)
    suma = suma + digito
suma2 = 0
for char in str(suma):
    digito = int(char)
    suma2 = suma2 + digito
print("sos el", suma2)
    