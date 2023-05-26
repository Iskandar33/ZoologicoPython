class Habitat:
    def __init__(self, opc):
        self._id = 0
        self._tipoHabitat = opc
        self._contAnimal = 0
        self._arrayAnimales = []
        self.cupo = 4

    def agregarAnimal(self, animal):
        self._arrayAnimales.append(animal)
        self._contAnimal += 1
        self.cupo -= 1
    
    def getAnimales(self):
        return self._arrayAnimales

    def setId(self, id):
        self._id = id
        
    def getId(self):
        return self._id

    def getContAnimal(self):
        return self._contAnimal
    
    def getTipo(self):
        return self._tipoHabitat

    def getCupo(self):
        return self.cupo
    
    def listarAnimales(self):
        for i in self._arrayAnimales:
            print("Animales dentro del hábitat:")
            print("ID(dentro del hábitat): ", i)
            print("Nombre: %s\nEspecie: %s\nHabitat al que pertenece: %s\nDieta:  %s\nHoras que duerme: %i", self._arrayAnimales[i].getNombre(), self._arrayAnimales[i].getEspecie(), self._arrayAnimales[i].getHabitatPertenece(), self._arrayAnimales[i].getAlimentacion(), self._arrayAnimales[i].getHorasDormir())
    