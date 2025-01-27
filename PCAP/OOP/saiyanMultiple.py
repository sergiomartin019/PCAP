class Saiyan:
    origen = 'Sadala'
    def __init__(self,nombre):
        self.nombre = nombre


class Humano:
    origen = 'Tierra'
    def __init__(self,nombre):
        self.nombre = nombre
        
class Mestizo(Saiyan, Humano):
    def __init__(self, nombre,a,b):
        self.nombre = nombre
        self.padre = a.nombre
        self.madre = b.nombre
        
    def verAncestros(self):
        for ancestro in Mestizo.__bases__:
            print(ancestro.__name__, end=' ')
        print()
        
goku = Saiyan("Son Goku")
vegeta = Saiyan("Vegeta")
bulma = Humano("Bulma")
trunks = Mestizo("Trunks",vegeta, bulma)


trunks.verAncestros()

print(trunks.origen)
trunks.origen = 'Tierra'
print(trunks.origen)
print(f"Trunks es de {trunks.origen}")
print(f"Goku es de {goku.origen}")

print(trunks.__module__)

print(f"El padre de {trunks.nombre} es {trunks.__dict__['padre']} ")
print(f"La madre de {trunks.nombre} es {trunks.__dict__['madre']} ")

if type(trunks).__name__ == 'Mestizo':
    if issubclass(Mestizo, Saiyan):
        print(f"{trunks.nombre} puede convertirse en supersaiyan")
        if issubclass(Mestizo, Humano):
             print(f"{trunks.nombre} tiene madre humana")
        else:
             print(f"{trunks.nombre} NO es humano")
    else:
         print(f"{trunks.nombre} NO puede convertirse en supersaiyan")
         
