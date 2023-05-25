import streamlit as st

class sistemaController:
    def __init__(self, modeloSis, modeloSisSt, vista):
        self.modeloSis = modeloSis
        self.modeloSisSt = modeloSisSt
        self.vista = vista

    def menuInicial(self, opc):
        if(opc == 1):
            st.divider()
            nuevoHabitat = self.vista.añadirHabitat()
            self.modeloSisSt.agregarHabitat(nuevoHabitat)
        
        elif(opc == 2):
            st.divider()
            nuevoAnimal = self.vista.crearAnimal()
            habitatEscogido = self.vista.escogerHabitat(nuevoAnimal)
            self.modeloSisSt.añadirAnimalHabitat(habitatEscogido, nuevoAnimal)
        
        elif(opc == 3):
            st.divider()
            animalEscogido = self.vista.elegirAnimal()