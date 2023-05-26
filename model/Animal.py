import streamlit as st
import random
class Animal:
    def __init__(self, id, nombre, especie, habitatPertenece, dieta, horasDormir):
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._habitatPertenece = habitatPertenece
        self._dieta = dieta
        self._horasDormir = horasDormir
        self._verificadorJugar = 0
        
    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

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

    def jugar(self):
        if(self._verificadorJugar == 0):
            st.write(f'{self.getNombre()} jugó mucho al Melty Blood Actress Again Current Code metiendole duro a los combos con Shiki')
            imagen = "imagen/Ryougi1.webp"
            st.image(imagen, width = 600)
            self._verificadorJugar = 1
        else:
            imagen = "imagen/Necochaos0.png"
            st.write(f'{self.getNombre()} ya había jugadó bastante al MBAACC por lo que no puede jugar más jeje')
            st.image(imagen, width = 600)
    def dormir(self):
        st.write("Mimir")
        st.write(f'{self.getNombre()} durmió placidamente sus {self.getHorasDormir()} horas de sueño uvu')
    
    def comer(self):
        dieta = self.getAlimentacion()
        opc = random.randint(0, 4)
        comida = dieta[opc]
        st.write(f'{self.getNombre()} fue alimentado con {comida} y le gustó mucho jeje')