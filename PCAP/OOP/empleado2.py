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