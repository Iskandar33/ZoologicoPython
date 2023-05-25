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
            self.habitatsNuevos.append(habitat)
            st.session_state["habitatsNuevos"] = self.habitatsNuevos
    
    def añadirAnimalHabitat(self, animal, habitat):
        if(animal is not None):
            self.habitatsNuevos[animal].agregarAnimal(animal)

    def getHabitat(self, id):
        return self.habitatsNuevos[id]
    
    def getHabitats(self):
        habitatsDisponibles = []
        for habitat in self.habitatsNuevos:
            if(habitat.getCupo != 0):
                habitatsDisponibles.append(habitat)
        return habitatsDisponibles
