class cartaNoEncontradaError(Exception):
    "Esta lleno"
    pass
class Carta:
    def __init__(self, nombre, ataque, defensa, tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo
    
class Jugador:
    def __init__(self):
        self.mazo = []
    def agregarCarta(self,carta):
        if type(carta).__name__ == "Carta":
            self.mazo.append(carta)
            print("se ha agregado la carta", carta.nombre)
    def invocarCarta(self, carta):
         if type(carta).__name__ == "Carta":
            try:
                if carta not in self.mazo:
                    raise cartaNoEncontradaError
                else:
                    print("jugador ha sacado la carta", carta.nombre)
            except cartaNoEncontradaError:
                print("no esta la carta en el mazo")

jugador = Jugador()
dragon = Carta("dragon blanco de ojos azules", 100, 100, "dragon")
ojoderah = Carta("ojo de rah", 0, 0, "hechizo")
jugador.agregarCarta(dragon)
jugador.invocarCarta(dragon)
jugador.invocarCarta(ojoderah)