carnivoro = ["", "", "", "", ""]
herviboro = ["", "", "", "", ""]
omnivoro = ["", "", "", "", ""]
class Animal:
    def __init__(self, id, nombre, especie, habitatPertenece, dieta, horasDormir):
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._habitatPertenece = habitatPertenece
        self._dieta = dieta
        self._horasDormir = horasDormir
        self._verificadorJugar = 1
        
    def getId(self):
        return self._id
    
    def getNombre(self):
        return self._nombre
    
    def getHabitatPertenece(self):
        return self._habitatPertenece
    
    def getEspecie(self):
        return self._especie

    def getAlimentacion(self):
        return self._dieta
    
    def getHorasDormir(self):
        return self._horasDormir

    # def comer(self):
    #     print("Se mostrará las comidas que puede escoger para alimentar al animal")
    #     for i in self._dieta:
    #         print(self._dieta[i])
    #     opc = int(input("Seleccione la comida mediante el ID"))
    #     if(opc in self._dieta):
    #         print("El animal fue alimentado con ", self._dieta[opc])
    #     else:
    #         raise ValueError("El elemento no esta en la lista")
    
    def jugar(self):
        if(self._verificadorJugar == 0):
            print("%s jugó mucho al Melty Blood Actress Again Current Code metiendole duro a los combos con Shiki", self._nombre)
            self._verificadorJugar = 1
        else:
            print("%s ya había jugado MBAACC con ShikiGOD", self._nombre)

    def dormir(self):
        horas = int(input("Ingrese las horas a dormir: "))
        if(horas < self._horasDormir):
            print("%s no pudo dormir ya que debe de dormir más horas", self._nombre)
        elif(horas >= self._horasDormir and horas < 24):
            print("%s durmió placidamente", self._nombre)
        else:
            print("%s no puede dormir todo un día o más", self._nombre)