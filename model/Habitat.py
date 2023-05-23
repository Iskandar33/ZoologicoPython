class Habitat:
    def __init__(self, opc):
        self._tipoHabitat = opc
        self._contAnimal = 0
        self._arrayAnimales = []

    def agregarAnimal(self, animal):
        if(animal.getHabitatPertenece() == self._tipoHabitat):
            self._arrayAnimales.append(animal)
            self._contAnimal += 1
            print("El animal fue agregado con éxito al hábitat")
        else:
           raise TypeError("El animal no pertenece a este hábitat")

    def getContAnimal(self):
        return self._contAnimal

    def listarAnimales(self):
        for i in self._arrayAnimales:
            print("Animales dentro del hábitat:")
            print("ID(dentro del hábitat): ", i)
            print("Nombre: %s\nEspecie: %s\nHabitat al que pertenece: %s\nDieta:  %s\nHoras que duerme: %i", self._arrayAnimales[i].getNombre(), self._arrayAnimales[i].getEspecie(), self._arrayAnimales[i].getHabitatPertenece(), self._arrayAnimales[i].getAlimentacion(), self._arrayAnimales[i].getHorasDormir())
    