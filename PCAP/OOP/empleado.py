class Empleado:
    def __init__(self,nombre,apellidos,cargo,salario = 1000):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario
    def getSalario(self):
        return self.__salario
    def __str__(self):
        return f"{self.nombre} {self.apellidos}, que es {self.cargo}, gana {self.getSalario()}"
listempleados =[
    Empleado("chiyo", "papa", "jefazo", 10000),
    Empleado("osaka", "villen", "desempleada"),
    Empleado("jose miguel", "sanchez", "programador", 2000),
    Empleado("p", "diddy", "encarcelado", 4000)
]

empleados_vip =[empleado for empleado in listempleados if empleado.getSalario() >= 2000]
for e in empleados_vip:
    print(e)

     

        