import Habitat
class Acuatico(Habitat):
    def __init__(self):
        self.splish = 1
        self.splash = 1
    
    def splishSplash(self):
        print("A los animales les gusta saltar en el agua y hacer splish al saltar y splash al caer")
        print("Se hicieron %i splish/es", self.splish)
        print("Asímismo, se hicieron %i splash/es", self.splash)
        print("Se aumentó la cantidad necesaria de splishes y de splashes")
        self.splish += 1
        self.splash += 1
