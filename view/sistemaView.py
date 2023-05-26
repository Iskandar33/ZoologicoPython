import streamlit as st
import pandas as pd
import requests

import model.Habitat
import model.Animal as Animal
import model.Sistema 
import model.SistemaSt
import controller.sistemaController as controller
class sistemaView:
    def __init__(self):
        self.sistema = model.Sistema.Sistema()
        self.sistemaSt = model.SistemaSt.SistemaSt()
        self.controller = controller.sistemaController(self.sistema, self.sistemaSt, self)

    def imprimirError(self, string):
        st.error(string, icon = "🤖")
    
    def imprimirNoError(self, string):
        st.success(string, icon = "✅")
            
    def menu(self):
        st.header("Bienvenido al Zoologico")

        with st.container():
            col1, col2, col3 = st.columns(3)
            col1.subheader("Añadir Hábitat")
            boton_añadir_habitat = col1.button("Acceder a esta opción", 1)
            col2.subheader("Añadir Animal a un hábitat")
            boton_añadir_animal = col2.button("Acceder a esta opción", 2)
            col3.subheader("Ingresarle una acción a un animal")
            boton_accion_animal = col3.button("Acceder a esta opción", 3)
            # col4.subheader("Información del Oso de Anteojos")
            # boton_informacion = col4.button("Acceder a esta opción", 4)

        if(boton_añadir_habitat):
            st.session_state["opcion"] = 1
        elif(boton_añadir_animal):
            st.session_state["opcion"] = 2
        elif(boton_accion_animal):
            st.session_state["opcion"] = 3
        # elif(boton_informacion):
        #     st.session_state["opcion"] = 4

        if("opcion" in st.session_state):
            self.controller.menuInicial(st.session_state["opcion"])
    
    def añadirHabitat(self):
        with st.container():
            st.subheader("Formulario para crear un nuevo hábitat")
            habitat = st.selectbox("Hay 4 hábitats posibles para escoger, estos son: \n1. Desértico \n2. Selvático \n3. Polar \n4. Acuático"
                                   , ("", "Desertico", "Selvatico", "Polar", "Acuatico"))
            boton_Crear_Habitat = st.button("Agregar Hábitat.")

            if(boton_Crear_Habitat):
                if(habitat == ""):
                    self.imprimirError("El hábitat no puede estar vacio.")
                else:
                    habitat = model.Habitat.Habitat(habitat)
                    self.imprimirNoError("El hábitat fue creado.")
                    return habitat
    
    
    def mostrarHabitats(self):
        st.divider()
        if(self.sistema.getContHabitats != 0):
            with st.container():
                st.subheader("Los hábitats actuales son: ")
                for habitat in self.sistema.getHabitats():
                    col1, col2 = st.columns(2)
                    col1.write("Tipo de hábitat: ", habitat.getTipo())
                    col2.write("Cupo del hábitat: ", habitat.getCupo())
                
    def elegirAnimal(self):
        animales = []
        for habitat in self.sistemaSt.getHabitats():
            for animal in habitat.getAnimales():
                animales.append(animal)
        # for animal in animales:
        #     st.write(pd.DataFrame({
        #         "Nombre": [animal.getNombre()],
        #         "Especie": [animal.getEspecie()]
        #     }))
        animalesAtt = [f'{animal.getId()}: {animal.getNombre()}' for animal in animales]
        escogerAnimal = st.selectbox("Escoge el animal:",
                                        (animalesAtt), key = "seleccion_animal")
        # self.imprimirNoError("El animal fue escogido con éxito.")
        # self.ingresarAccion(escogerAnimal)
        opc = st.selectbox("Las acciones a ingresar son, jugar, dormir y comer",
                    ("", "Jugar", "Dormir", "Comer"), key = "seleccion_accion")
    
        boton_seleccionar = st.button("Seleccionar opción")
        if(boton_seleccionar):
            idAnimalEscog = int(escogerAnimal.split(":")[0])
            for animal in animales:
                if(animal.getId() == idAnimalEscog):
                    animalSelecc = animal
                    break
            if(opc == ""):
                self.imprimirError("El campo de elección de opción no puede estar vacio")
            if(escogerAnimal == ""):
                self.imprimirError("El campo de elección de animal 'Escoger Animal' no puede estar vacio")
            elif(opc == "Jugar"):
                # st.write("Se entrará a jugar con el animal.")
                animalSelecc.jugar()
            elif(opc == "Dormir"):
                animalSelecc.dormir()    
            else:
                animalSelecc.comer()
                
    def menuComer(self, animal):
        comidasAnimal = animal.getAlimentacion()
        comida = st.selectbox("Las comidas que el animal puede comer son: "
                                , list(comidasAnimal), key = "seleccion_comida")
        
        boton_alimentar = st.button("Alimentar", key = "boton_alimentar")
        if(boton_alimentar):
            self.imprimirNoError("El animal fue alimentado con éxito, le gustó la comida!")
        
    def crearAnimal(self):
        with st.container():
            st.subheader("Formulario para crear un Animal")
            habitatPertenece = st.selectbox("Hay 4 hábitats posibles para escoger, estos son: \n1. Desértico \n2. Selvático \n3. Polar \n4. Acuático"
                                   , ("", "Desertico", "Selvatico", "Polar", "Acuatico"))
            if(habitatPertenece == "Desertico"):
                animal = st.selectbox("Los animales que pertenecen a este hábitat son: "
                                      , ("", "Camello", "Avestruz", "Correcaminos", "Coyote", "Dingo Australiano"))
            elif(habitatPertenece == "Selvatico"):
                animal = st.selectbox("Los animales que pertenecen a este hábitat son: "
                                      , ("", "Puma", "Tapir", "Oso de Anteojos", "Leopardo", "Orangután"))
            elif(habitatPertenece == "Polar"):
                animal = st.selectbox("Los animales que pertenecen a este hábitat son: "
                                      , ("", "Oso Polar", "Morsa", "Pinguino", "Beluga", "Narval"))
            elif(habitatPertenece == "Acuatico"):
                animal = st.selectbox("Los animales que pertenecen a este hábitat son: "
                                      , ("", "Delfín", "Orca", "Calamar Vampiro", "Serpiente Marina", "Estrella de Mar"))

            nombre = st.text_input("Nombre del animal: ")
            horasDormir = st.number_input("Horas que duerme el animal: ", step = 1)
            dieta = st.selectbox("Dietas a escoger:\n0.Carnivoro\n1.Herbivoro\n2.Omnivoro"
                                 , ("", "Carnivoro", "Herviboro", "Omnivoro"))
            
            habitatsDisponibles = self.sistemaSt.getHabitatsTipo(habitatPertenece)
            habitatsAtt = [f'{habitat.getId()}: {habitat.getTipo()}, cupos: {habitat.getCupo()}' for habitat in habitatsDisponibles]
            habitatEscogido = st.selectbox("Los hábitats posibles son: "
                                        , (habitatsAtt))
            
            boton_crear_Animal = st.button("Crear Animal")

            if(boton_crear_Animal):
                if(habitatPertenece == ""):
                    self.imprimirError("El hábitat al que pertenece no puede estar vacio")
                elif(animal == ""):
                    self.imprimirError("El campo 'Animal' no puede estar vacio")
                elif(nombre == ""):
                    self.imprimirError("El campo 'Nombre' no puede estar vacio")
                elif((horasDormir == 0) or (horasDormir >= 24)):
                    self.imprimirError("Un animal no puede estar todo el día despierto, dormir todo el día o el número no puede ser mayor a un día entero")
                elif(dieta == ""):
                    self.imprimirError("El campo 'Dieta' no puede estar vacio")
                elif(habitatEscogido == ""):
                    self.imprimirError("El campo de seleccionar el hábitat no puede estar vacio")
                else:
                    if(dieta == "Carnivoro"):
                        dietaCompleta = ["Carne", "Chorizo", "Pechuga de pollo", "Muslo", "Pollo"]
                    elif(dieta == "Herviboro"):
                        dietaCompleta = ["Hierba", "Lechuga", "Hojas", "Corteza", "Savia"]
                    else:
                        dietaCompleta = ["Carne", "Hierba", "Pollo", "Hojas", "Savia"]    
                    
                    pTempAnimal = Animal.Animal(self.sistema.getContAnimales(), nombre, animal, habitatPertenece, dietaCompleta, horasDormir)
                    self.imprimirNoError("El animal fue creado.")
                    id = int(habitatEscogido.split(":")[0])
                    return [pTempAnimal, id]
                
    # def obtenerInfo(self):
    #     url = ""
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         data = response.json()
    #         print(data)
    #     else:
    #         print(f"Error en la solicitud: {response.status_code}")

