TAMANIO = 7
class ZoologicoView:
    
    def imprimir(self, string):
        print(string)

    def obtenerHabitat(self, habitats):
        opc = int(input("Ingrese el número del hábitat deseado: "))
        if(opc in habitats):
            habitat = habitats[opc]
        else:
            raise IndexError
        return habitat
            
    def mostrarHabitats(self, arrayHabitats):
        for i in arrayHabitats:
            print("ID: ", i)
            print("Hábitat: ", (arrayHabitats[i]).getTipoHabitat())
        opc = int(input("Ingrese el ID del hábitat a seleccionar: "))
        if(opc in arrayHabitats):
            return opc
        else:
            raise IndexError
        
    def obtenerHabitatAnimal(self, habitats):
        opc = int(input("Ingrese el número del hábitat deseado: "))
        if(opc in habitats):
            return opc
        else:
            raise IndexError
    
    def mostrarAnimales(self, animales):
        for i in range(TAMANIO):
            print(animales[i])
        opcAnimal = int(input("Ingrese el animal a seleccionar por el ID: "))
        if(opcAnimal in animales):
            animalEscogido = animales[opcAnimal]
        else:
            raise KeyError("El elemento no existe")
        return animalEscogido

    def obtenerNombre(self):
        nombre = input("Ingrese el nombre del animal: ")
        return nombre

    def obtenerHorasDormir(self):
        horasDormir = int(input("Ingrese las horas que el animal duerme: "))
        return horasDormir

    def obtenerDieta(self):
        opcDieta = int(input("Ingrese el número de la dieta a escoger: "))
        if(opcDieta in self.modelo.tipoDieta):
            if(opcDieta == 1):
                dieta = self.modelo.carnivoro
            elif(opcDieta == 2):
                dieta = self.modelo.herviboro
            elif (opcDieta == 3):
                dieta = self.modelo.omnivoro
        else:
            raise TypeError("Se presentó un error")
        return dieta