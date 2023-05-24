import Habitat
import Animal
TAMANIO = 7
class Sistema:
    def __init__(self):
        self._contHabitats = 0
        self._contAnimales = 0
        self._arrayAnimalesTotal = []
        self._arrayHabitats = []
        self.tipoDieta = ["Carnivoro","Herbivoro", "Omnivoro"]
        self.carnivoro = ["", "", "", "", ""]
        self.herviboro = ["", "", "", "", ""]
        self.omnivoro = ["", "", "", "", ""]
        self.habitats = ["Desertico", "Selvatico", "Polar", "Acuatico"]
        self.animalesHabitat = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]

    def añadirHabitat(self, opc):
            pTempHabitat = Habitat(opc)
            self._arrayHabitats[self._contHabitats] = pTempHabitat
            self._contHabitats += 1
    
    def añadirAnimalHabitat(self, habitatEscogido, pTempAnimal):
        habitatEscogido.agregarAnimal(pTempAnimal)
        self._arrayAnimalesTotal[self._contAnimales] = pTempAnimal
        self._contAnimales += 1

    # def crearAnimal(self, contAnimales, nombre, especie, habitatPertenece, opcDieta, horasDormir):    
    #     pTempAnimal = Animal(contAnimales, nombre, especie, habitatPertenece, opcDieta, horasDormir)
    #     return pTempAnimal
        
    # def mostrarAnimales(self, opc):
    #     for i in range(TAMANIO):
    #         print(self.animalesHabitat[opc][i])
    #     opcAnimal = int(input("Ingrese el animal a seleccionar por el ID: "))
    #     try:
    #         if(opcAnimal in self.animalesHabitat[opc]):
    #             animalEscogido = self.animalesHabitat[opc][opcAnimal]
    #         else:
    #             raise KeyError("El elemento no existe")
    #     except:
    #         print("")
    #     return animalEscogido

    # def mostrarHabitats(self):
    #     for i in self._arrayHabitats:
    #         print("ID: ", i)
    #         print("Hábitat ", (self._arrayHabitats[i]).getTipoHabitat())


    # def ingresarAccionAnimal(self):
    #     if(self._contAnimales == 0):
    #         print("No hay animales en el zoologico actualmente")
    #     else:
    #         try:
    #             animalEscogido = self.mostrarAnimales()
    #             print("Las acciones que puede realizar un animal son: ")
    #             print("1. Comer\n2. Jugar\n3. Dormir")
    #             opc = int(input("Ingrese el número de la acción a realizar: "))            
    #             if(opc == 1):
    #                 animalEscogido.comer()
    #             elif(opc == 2):
    #                 animalEscogido.jugar()
    #             elif(opc == 3):
    #                 animalEscogido.dormir()
    #             else:
    #                 raise TypeError("Se escribió un elemento que no existe")
    #         except:
    #             print("")