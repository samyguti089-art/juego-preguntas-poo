# Importamos ABC y abstractmethod para poder crear nuestra clase abstracta
from abc import ABC, abstractmethod


class Pregunta(ABC):
    """
    Clase abstracta que representa una pregunta general del juego.
    Sirve como molde (plantilla) para los diferentes tipos de preguntas.
    """

    def __init__(self, enunciado, categoria, dificultad, respuesta_correcta):
        # Usamos guion bajo para aplicar encapsulamiento (atributos protegidos)
        self._enunciado = ""
        self._categoria = categoria
        self._dificultad = dificultad
        self._respuesta_correcta = respuesta_correcta

        # Usamos el setter para validar el enunciado desde que se crea el objeto
        self.enunciado = enunciado

    # --- Propiedades (Getters y Setters) para el encapsulamiento ---

    @property
    def enunciado(self):
        return self._enunciado

    @enunciado.setter
    def enunciado(self, nuevo_enunciado):
        # Validamos que el enunciado no sea un texto vacio
        texto_limpio = str(nuevo_enunciado).strip()
        if len(texto_limpio) == 0:
            raise ValueError("El enunciado de la pregunta no puede estar vacío.")
        self._enunciado = texto_limpio

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria):
        texto_limpio = str(nueva_categoria).strip()
        if len(texto_limpio) == 0:
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = texto_limpio

    @property
    def dificultad(self):
        return self._dificultad

    @property
    def respuesta_correcta(self):
        return self._respuesta_correcta

    # --- Método común que heredan todas las clases hijas ---

    def verificar_respuesta(self, respuesta_usuario):
        """
        Compara la respuesta que eligió el jugador con la respuesta correcta.
        Pasamos todo a minúsculas y quitamos espacios para evitar errores.
        """
        if respuesta_usuario is None:
            return False

        texto_usuario = str(respuesta_usuario).strip().lower()
        texto_correcto = str(self._respuesta_correcta).strip().lower()

        if texto_usuario == texto_correcto:
            return True
        else:
            return False

    # --- Métodos abstractos (obligatorios para las clases hijas) ---

    @abstractmethod
    def obtener_opciones(self):
        """Devuelve la lista de opciones disponibles para mostrar en pantalla."""
        pass

    @abstractmethod
    def calcular_puntos(self):
        """Calcula cuántos puntos da la pregunta según su tipo y dificultad."""
        pass

    @abstractmethod
    def obtener_tipo(self):
        """Devuelve un texto indicando qué tipo de pregunta es."""
        pass

    @abstractmethod
    def obtener_retroalimentacion(self, acertada):
        """Devuelve un mensaje para el jugador después de responder."""
        pass
