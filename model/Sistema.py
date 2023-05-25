class Sistema:
    def __init__(self):
        self._contHabitats = 0
        self._contAnimales = 0
        self._arrayAnimalesTotal = []
        self._arrayHabitats = []
        self.animalesHabitat = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]

    def agregarHabitat(self, habitat):
        self._arrayHabitats.append(habitat)
        self._contHabitats += 1
    
    def añadirAnimalHabitat(self, habitatEscogido, pTempAnimal):
        habitatEscogido.agregarAnimal(pTempAnimal)
        self._arrayAnimalesTotal.append(pTempAnimal)
        self._contAnimales += 1

    def getHabitats(self):
        return self._arrayHabitats
    
    def getContHabitats(self):
        return self._contHabitats
    
    def getContAnimales(self):
        return self._contAnimales
    



