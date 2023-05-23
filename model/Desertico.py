import Habitat
class Desertico(Habitat):
    def __init__(self):
        self.oasis = "321,20,-255"
        self.cactus = 1

    def plantarCactus(self):
        print("A los animales de este hábitat les gusta ver cactus grandes por lo que se plantará más")
        print("Cactus actuales: ", self.cactus)
        print("Se plantara un cactus más")
        self.cactus += 1
    
    def buscarOasis(self):
        print("Los animales buscan un oasis para escuchar musica relajados, por lo que se lo vamos a ecnontrar")
        print("El oasis se encuentra en %s")