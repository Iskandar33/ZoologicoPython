import model.Sistema
import view.sistemaView
import Animal
import Habitat
import streamlit as st

class ZoologicoController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    # def añadirHabitat(self):
    #     self.vista.imprimir("Hay 4 hábitats posibles para crear, estos son:")
    #     self.vista.imprimir("1. Desértico \n2. Selvático \n3. Polar \n4. Acuático")
    #     try:
    #         opc = self.vista.obtenerHabitat(self.modelo.habitats)
    #         self.modelo.añadirHabitat(opc)
    #     except IndexError as e:
    #         return str(e)
        
    # def añadirAnimalHabitat(self):
    #     if(self.modelo._contAnimales == 0):
    #         self.vista.imprimir("No hay animales en el zoologico actualmente")
    #     else:
    #         try: 
    #             pTempAnimal = self.modelo.crearAnimal(self.modelo._contAnimales)
    #             opc = self.vista.mostrarHabitats(self.modelo._arrayHabitats)
    #             habitatEscogido = self.modelo._arrayHabitats[opc]
    #             self.modelo.añadirAnimalHabitat(habitatEscogido, pTempAnimal)
    #         except IndexError as e:
    #             return str(e)

    # def crearAnimal(self, contAnimales):
    #     self.vista.imprimir("Cada hábitat tiene 6 especies de animales para agregar, escoja el hábitat que desea")
    #     self.vista.imprimir("0. Desértico \n1. Selvático \n2. Polar \n3. Acuático")
    #     try:
    #         opcHabitat = self.vista.obtenerHabitatAnimal()
    #         animales = self.modelo.animalesHabitat[opcHabitat]
    #         opcAnimal = self.vista.mostrarAnimales(animales)
    #         nombre = self.vista.obtenerNombre()
    #         especie = opcAnimal
    #         habitatPertenece = opcHabitat
    #         horasDormir = self.vista.obtenerHorasDormir()
    #         print("Dietas a escoger:\n0.Carnivoro\n1.Herbivoro\n2.Omnivoro")
    #         opcDieta = self.vista.obtenerDieta()
    #         pTempAnimal = self.modelo.crearAnimal(contAnimales, nombre, especie, habitatPertenece, opcDieta, horasDormir)
    #         self.vista.imprimir("El animal fue creado.")
    #     except IndexError as e:
    #         return str(e)
    #     return pTempAnimal
    
    def ingresarAccionAnimal(self):
        if(self.modelo._contAnimales == 0):
            self.vista.imprimir("No hay animales en el zoologico actualmente")
        else:
            try:
                animalEscogido = self.vista.mostrarAnimales(self.modelo._arrayAnimales)
                self.vista.imprimir("Las acciones que puede realizar un animal son: ")
                self.vista.imprimir("1. Comer\n2. Jugar\n3. Dormir")
                opc = self.vista.obtenerAccion("Ingrese el número de la acción a realizar: ")
                if(opc == 1):
                    animalEscogido.comer()
                elif(opc == 2):
                    animalEscogido.jugar()
                elif(opc == 3):
                    animalEscogido.dormir()
                else:
                    raise IndexError("Se ingresó un elemento que no hace parte de las acciones.")
            except IndexError as e:
                return str(e)
            
    def menu(self):
        st.header("Bienvenido al Zoologico")

        with st.container():
            col1, col2, col3 = st.columns(2)
            col1.subheader("Añadir Hábitat")
            boton_añadir_habitat = col1.button("Acceder a esta opción", 1)
            col2.subheader("Añadir Animal a un hábitat")
            boton_añadir_animal = col2.button("Acceder a esta opción", 2)
            col3.subheader("Ingresarle una acción a un animal")
            boton_accion_animal = col3.button("Acceder a esta opción", 3)
        
        if(boton_añadir_habitat ==  True):
            st.session_state["opcion"] = 1
        elif(boton_añadir_animal == True):
            st.session_state["opcion"] = 2
        elif(boton_accion_animal == True):
            st.session_state["opcion"] = 3
        

    def menuAñadirHabitat(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para añadir un nuevo hábitat")
            habitat = st.selectbox("Hay 4 hábitats posibles para crear, estos son: \n1. Desértico \n2. Selvático \n3. Polar \n4. Acuático"
                                   (self.modelo.habitats))
            self.modelo.añadirHabitat(habitat)
            self.vista.imprimir("Se añadió el hábitat con éxito")

    def menuAñadirAnimalHabitat(self):
        if(self.modelo._contAnimales == 0):
            self.vista.imprimir("No hay animales en el zoologico actualmente")
        else:
            pTempAnimal = self.menuCrearAnimal()
            opc = self.vista.mostrarHabitats(self.modelo._arrayHabitats)
            habitatEscogido = self.modelo._arrayHabitats[opc]
            self.modelo.añadirAnimalHabitat(habitatEscogido, pTempAnimal)

    def menuCrearAnimal(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo animal")
            habitat = st.selectbox("Hay 4 hábitats posibles para escoger, estos son: \n1. Desértico \n2. Selvático \n3. Polar \n4. Acuático"
                                   (self.modelo.habitats))
            animal = st.selectbox("Los animales posibles para este hábitat son: "
                                  (self.modelo.animalesHabitat[habitat]))
            nombre = st.text_input("Nombre del animal: ")
            horasDormir = st.number_input("Ingrese las horas que duerme el animal: ")
            dieta = st.selectbox("Dietas a escoger:\n0.Carnivoro\n1.Herbivoro\n2.Omnivoro"
                                 (self.modelo.tipoDieta))
            pTempAnimal = Animal(self.modelo._contAnimales, nombre, animal, habitat, dieta, horasDormir)
        return pTempAnimal
            
        
