import Habitat
class Polar(Habitat):
    def __init__(self):
        self.munecosDeNieve = 1
        self.temperatura = "8º C"
    
    def revisarTemp(self):
        print("La temperatura del hábitat polar es: %s", self.temperatura)
    
    def hacerMunecosNieve(self):
        print("Hay %i munecos de nieve en tu hábitat", self.munecosDeNieve)
        cant = int(input("Ingrese la cantidad de munecos de nieve: "))
        print("Se hicieron %i munecos de nieve", cant)
        print("Aumentó la felicidad en tu hábitat jeje")
        self.munecosDeNieve += cant