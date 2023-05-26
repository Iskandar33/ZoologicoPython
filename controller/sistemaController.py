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
            nuevoAnimalyHab = self.vista.crearAnimal()
            self.modeloSisSt.añadirAnimalHabitat(nuevoAnimalyHab)
        
        elif(opc == 3):
            st.divider()
            self.vista.elegirAnimal()

        # elif(opc == 4):
        #     self.vista.obtenerInfo()