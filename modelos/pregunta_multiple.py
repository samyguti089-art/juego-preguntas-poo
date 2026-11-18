from modelos.pregunta import Pregunta


class PreguntaMultiple(Pregunta):
    """
    Clase hija que hereda de Pregunta.
    Representa una pregunta de selección múltiple con varias opciones (por ejemplo 4).
    """

    def __init__(self, enunciado, categoria, dificultad, respuesta_correcta, opciones):
        # Llamamos al constructor de la clase padre (Pregunta) usando super()
        super().__init__(enunciado, categoria, dificultad, respuesta_correcta)

        # Atributo propio de esta clase hija
        self._opciones = []
        self.establecer_opciones(opciones)

    def establecer_opciones(self, lista_opciones):
        """
        Valida y guarda la lista de opciones de la pregunta.
        """
        if len(lista_opciones) < 2:
            raise ValueError("Una pregunta múltiple debe tener al menos 2 opciones.")

        # Verificamos con un ciclo for normal si la respuesta correcta está en las opciones
        encontrada = False
        for opcion in lista_opciones:
            if str(opcion).strip().lower() == str(self._respuesta_correcta).strip().lower():
                encontrada = True

        if not encontrada:
            raise ValueError("La respuesta correcta debe estar incluida dentro de las opciones.")

        self._opciones = lista_opciones

    # --- Implementación de los métodos abstractos (Polimorfismo) ---

    def obtener_opciones(self):
        # Devuelve las opciones que se le configuraron a esta pregunta
        return self._opciones

    def calcular_puntos(self):
        """
        En selección múltiple damos más puntos porque es más difícil acertar entre 4 opciones.
        """
        if self._dificultad == "Fácil":
            return 10
        elif self._dificultad == "Media":
            return 20
        elif self._dificultad == "Difícil":
            return 30
        else:
            return 10

    def obtener_tipo(self):
        return "Selección Múltiple"

    def obtener_retroalimentacion(self, acertada):
        puntos = self.calcular_puntos()
        if acertada:
            return "¡Correcto! Ganaste " + str(puntos) + " puntos."
        else:
            return "Incorrecto. La respuesta correcta era: " + str(self._respuesta_correcta)
