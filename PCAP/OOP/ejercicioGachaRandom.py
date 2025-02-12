import random
class personajeGacha:
    listaPersonajes = []
    def __init__(self, nombre, rareza, elemento):
        self.nombre = nombre
        self.rareza = rareza
        self.elemento = elemento
        personajeGacha.listaPersonajes.append(self)
    @staticmethod
    def Invocar():
        randomNumber = random.randrange(1,100)
        if randomNumber > 1 and randomNumber< 5:
            random.shuffle(personajeGacha.listaPersonajes)
            for personaje in personajeGacha.listaPersonajes:
                if personaje.rareza == "legendaria":
                    print(personaje.nombre, personaje.rareza)
                    break;
        if randomNumber > 6 and randomNumber <=21:
            random.shuffle(personajeGacha.listaPersonajes)
            for personaje in personajeGacha.listaPersonajes:
                if personaje.rareza == "rara":
                    print(personaje.nombre, personaje.rareza)
                    break;
        if randomNumber > 22:
            random.shuffle(personajeGacha.listaPersonajes)
            for personaje in personajeGacha.listaPersonajes:
                if personaje.rareza == "comun":
                    print(personaje.nombre, personaje.rareza)
                    break;
personaje1 = personajeGacha("personaje", "legendaria", "agua")
personaje2 = personajeGacha("personaje2", "rara", "fuego")
personaje3 = personajeGacha("personaje3", "rara", "hielo")
personaje4 = personajeGacha("personaje4", "comun", "fuego")
personaje5 = personajeGacha("personaje5", "comun", "electricidad")
personaje5 = personajeGacha("personaje6", "comun", "hielo")
personaje6 = personajeGacha("personaje6", "comun", "agua")

personajeGacha.Invocar()
personajeGacha.Invocar()
personajeGacha.Invocar()
personajeGacha.Invocar()
personajeGacha.Invocar()

        
            
            
        
            
        