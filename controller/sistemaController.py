class ZoologicoController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def añadirHabitat(self):
        self.modelo.añadirHabitat()