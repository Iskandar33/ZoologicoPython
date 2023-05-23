import model.Sistema 
import view.sistemaView 
import controller.sistemaController

if __name__ == "__main__":
    modelo = model.Sistema()
    vista = view.Sistema()
    controlador = controller.Sistema(modelo, vista)