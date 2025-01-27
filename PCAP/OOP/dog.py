class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: ¡Guau!"
 
 
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, Corderito!"
 
 
class GuardDog(SheepDog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, Señor Intruso!"
    
class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + " No me gustan las montañas"
        
 
 
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
lowland = LowlandDog("lowtaper")

print(rocky)
print(luna)
print(lowland)
 