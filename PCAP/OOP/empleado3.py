class Empleado:
    plantilla = []
    numEmpleados = 0
    def __init__(self, nombre:str, cargo:str, salario=25000.50):
        if salario <= 0:
            raise ValueError
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        Empleado.plantilla.append(self)
        Empleado.numEmpleados = Empleado.numEmpleados + 1

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        
    def get_salario(self):
            return self.__salario
    def __str__(self):
         return f"Nombre: {self.nombre}, cuyo cargo: {self.cargo}, y su salario es: {self.get_salario()}"

empleado1 = Empleado("miguel", "jefe", 200000)
empleado2 = Empleado("jose", "trabajador",4)

for empl in Empleado.plantilla:
    print(empl)
print(Empleado.numEmpleados)
print(Empleado.__dict__)

num1 = 7
num2 = 7.0
num3 = 7.5
if Empleado.is_integer(num1):
    print(num1, " es entero.")
else:
    print(num1, " no es entero")
if Empleado.is_integer(num2):
    print(num2, " es entero.")
else:
    print(num2, " no es entero")
if Empleado.is_integer(num3):
    print(num3, " es entero.")
else:
    print(num3, " no es entero")
