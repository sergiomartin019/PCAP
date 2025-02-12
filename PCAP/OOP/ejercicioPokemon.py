class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
    def atacar(self, pokemon):
        if type(pokemon).__name__ == "Pokemon":
            try:
                if pokemon.vida > 0:
                    pokemon.vida = pokemon.vida - self.ataque
                    print(pokemon.nombre, "tiene", pokemon.vida , "de vida")
                    if pokemon.vida <= 0:
                        raise Exception
                elif pokemon.vida <= 0:
                    raise Exception
            except Exception:
                print("el pokemon ha sido eliminado")
    
        

squirtle = Pokemon("squirtle", "agua", 100, 50)
charmander = Pokemon("charmander", "agua", 80, 60)

squirtle.atacar(charmander)
charmander.atacar(squirtle)
squirtle.atacar(charmander)
            
        
        
        