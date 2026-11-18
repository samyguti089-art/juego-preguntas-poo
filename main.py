import tkinter as tk
from servicios.gestor_preguntas import GestorPreguntas
from interfaz.ventana_principal import VentanaPrincipal


def iniciar_aplicacion():
    """
    Función principal que arranca todo el programa.
    Crea el gestor de preguntas, la ventana de Tkinter y los conecta.
    """
    # 1. Creamos el objeto gestor que carga las preguntas en memoria
    gestor = GestorPreguntas()

    # 2. Creamos la ventana raíz de Tkinter
    ventana_raiz = tk.Tk()

    # 3. Instanciamos nuestra clase de interfaz pasándole la ventana y el gestor
    app = VentanaPrincipal(ventana_raiz, gestor)

    # 4. Iniciamos el ciclo de eventos de la ventana gráfica
    ventana_raiz.mainloop()


# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_aplicacion()
