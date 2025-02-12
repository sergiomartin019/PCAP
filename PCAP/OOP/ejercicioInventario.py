class Item:
    def __init__(self,nombre,tipo,rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
class InventarioLlenoError(Exception):
    "Esta lleno"
    pass
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        
    def agregarItem(self,item):
        if type(item).__name__ == "Item":
            try:
                if len(self.inventario) < 5:
                    self.inventario.append(item)
                    print("se ha insertado el item")
                else:
                    raise InventarioLlenoError
            except InventarioLlenoError:
                print("el inventario esta lleno")
    def mostrarInventario(self):
        for item in self.inventario:
            print(item.nombre)
    def eliminarItem(self,item):
         if type(item).__name__ == "Item":
            if item in self.inventario:
                self.inventario.remove(item)
                print("se ha eliminado este objeto")
            else:
                print("no esta ese objeto en el inventario")
                
            
            

item1 = Item("espada chula chula", "espada", "icono super prime")
item2 = Item("escudo chulo chulo", "escudo", "icono super prime")
item3 = Item("armadura chic chic", "armadura", "icono super prime")
item4 = Item("jake", "mascota", "legendario")
item5 = Item("pocion de vida", "pocion", "comun")
item6 = Item("medallon de valentia", "medallon", "raro")

personaje1 = Personaje("JH de la cruz")
personaje1.agregarItem(item1)
personaje1.agregarItem(item2)
personaje1.agregarItem(item3)
personaje1.agregarItem(item4)
personaje1.agregarItem(item5)
personaje1.agregarItem(item6)

personaje1.mostrarInventario()

personaje1.eliminarItem(item1)

personaje1.mostrarInventario()

personaje1.eliminarItem(item6)


                
             