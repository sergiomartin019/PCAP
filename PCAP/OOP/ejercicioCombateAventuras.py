import random
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    def atacar(self, personaje):
        if type(personaje).__name__ == "Personaje":
            esquivado = personaje.esquivar()
            try:
                if esquivado:
                    print(personaje.nombre, "ha esquivado")
                elif esquivado == False and  personaje.vida > 0:
                    personaje.vida = personaje.vida - self.ataque
                    print(personaje.nombre, "tiene", personaje.vida , "de vida")
                    if personaje.vida <= 0:
                        raise Exception
                else:
                    raise Exception
            except Exception:
                print("el personaje ha sido eliminado")
    def esquivar(self):
        randomNumber = random.randrange(1,10)
        if randomNumber < 5:
            return False
        else:
            return True     
alfredo = Personaje("alfredo", 100, 60)
gerardo = Personaje("gerardo", 70, 90)

alfredo.atacar(gerardo)
gerardo.atacar(alfredo)
alfredo.atacar(gerardo)



