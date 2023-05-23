import Habitat
import Animal
TAMANIO = 7
carnivoro = ["", "", "", "", ""]
herviboro = ["", "", "", "", ""]
omnivoro = ["", "", "", "", ""]
class Sistema:
    def __init__(self):
        self._contHabitats = 0
        self._contAnimales = 0
        self._arrayAnimalesTotal = []
        self._arrayHabitats = []
        self.tipoDieta = ["Carnivoro","Herbivoro", "Omnivoro"]
        self.habitats = ["Desertico", "Selvatico", "Polar", "Acuatico"]
        self.animalesHabitat = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]

    def añadirHabitat(self): 
        print("Hay 4 hábitats posibles para crear, estos son:")
        print("1. Desértico \n2. Selvático \n3. Polar \n4. Acuático")
        print("Ingrese el número del hábitat deseado")
        try:
            opc = int(input())
            if(opc in self.habitats):
                pTempHabitat = Habitat(opc)
                self._arrayHabitats[self._contHabitats] = pTempHabitat
                self._contHabitats += 1
                print("El habitat fue añadido.")
            else:
                raise KeyError("El dato ingresado no hace parte de los hábitats")
        except:
            print()

    def añadirAnimalHabitat(self):
        if(self._contHabitats == 0):
            print("No hay hábitats por el momento")
        else:
            try:    
                pTempAnimal = self.crearAnimal(self._contAnimales)
                opc = self.mostrarHabitats()
                print("Ingrese el ID del habitat a escoger: ")
                if(opc in self._arrayHabitats):
                    habitatEscogido = self._arrayHabitats[opc]
                    #throw animal no pertenece al habitat
                    habitatEscogido.agregarAnimal(pTempAnimal)
                    self._arrayAnimalesTotal[self._contAnimales] = pTempAnimal
                    self._contAnimales += 1
            except:
                print()

    def crearAnimal(self, contAnimales):
        print("Cada hábitat tiene 6 especies de animales para agregar, escoja el hábitat que desea")
        print("0. Desértico \n1. Selvático \n2. Polar \n3. Acuático")
        opc = int(input()) 
        opcAnimal = self.mostrarAnimales(opc)
        nombre = input("Ingrese el nombre: ")
        especie = opcAnimal
        habitatPertenece = opc
        horasDormir = int(input("Ingrese las horas que duerme el animal: "))
        print("Dietas a escoger:\n0.Carnivoro\n1.Herbivoro\n2.Omnivoro")
        opcDieta = int(input("Ingrese la dieta a escoger: "))
        if(opcDieta in self.tipoDieta):
            if(opcDieta == 1):
                dieta = carnivoro
            elif(opcDieta == 2):
                dieta = herviboro
            else:
                dieta = omnivoro
            pTempAnimal = Animal(contAnimales, nombre, especie, habitatPertenece, dieta, horasDormir)
        else:
            raise TypeError("El elemento no esta en la lista de comidas")
        return pTempAnimal
        
    def mostrarAnimales(self, opc):
        for i in range(TAMANIO):
            print(self.animalesHabitat[opc][i])
        opcAnimal = int(input("Ingrese el animal a seleccionar por el ID: "))
        try:
            if(opcAnimal in self.animalesHabitat[opc]):
                animalEscogido = self.animalesHabitat[opc][opcAnimal]
            else:
                raise KeyError("El elemento no existe")
        except:
            print("")
        return animalEscogido

    def mostrarHabitats(self):
        for i in self._arrayHabitats:
            print("ID: ", i)
            print("Hábitat ", (self._arrayHabitats[i]).getTipoHabitat())


    def ingresarAccionAnimal(self):
        if(self._contAnimales == 0):
            print("No hay animales en el zoologico actualmente")
        else:
            try:
                animalEscogido = self.mostrarAnimales()
                print("Las acciones que puede realizar un animal son: ")
                print("1. Comer\n2. Jugar\n3. Dormir")
                opc = int(input("Ingrese el número de la acción a realizar: "))            
                if(opc == 1):
                    animalEscogido.comer()
                elif(opc == 2):
                    animalEscogido.jugar()
                elif(opc == 3):
                    animalEscogido.dormir()
                else:
                    raise TypeError("Se escribió un elemento que no existe")
            except:
                print("")