import streamlit as st

class SistemaSt:
    def __init__(self):
        if("habitatsNuevos") in st.session_state:
            self.habitatsNuevos = st.session_state["habitatsNuevos"]
        else:
            self.habitatsNuevos = []
            st.session_state["habitatsNuevos"] = []

    def agregarHabitat(self, habitat):
        if(habitat is not None):
            habitat.setId(len(self.habitatsNuevos))
            self.habitatsNuevos.append(habitat)
            st.session_state["habitatsNuevos"] = self.habitatsNuevos
    
    def añadirAnimalHabitat(self, habitatyAnimal):
        if(habitatyAnimal is not None):
            habitatyAnimal[0].setId(len(self.habitatsNuevos[habitatyAnimal[1]].getAnimales()))
            self.habitatsNuevos[habitatyAnimal[1]].agregarAnimal(habitatyAnimal[0])
            st.session_state["habitatsNuevos"] = self.habitatsNuevos

    def getHabitat(self, id):
        return self.habitatsNuevos[id]
    
    def getHabitats(self):
        return self.habitatsNuevos
    
    def getHabitatsTipo(self, habitatPertenece):
        habitatsDisponibles = []
        for habitat in self.habitatsNuevos:
            if((habitat.getCupo() != 0) and (habitat.getTipo() == habitatPertenece)):
                habitatsDisponibles.append(habitat)
        return habitatsDisponibles
