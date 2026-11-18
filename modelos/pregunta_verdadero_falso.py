from modelos.pregunta import Pregunta


class PreguntaVerdaderoFalso(Pregunta):
    """
    Clase hija que hereda de Pregunta.
    Representa una pregunta donde solo se puede responder 'Verdadero' o 'Falso'.
    """

    def __init__(self, enunciado, categoria, dificultad, respuesta_correcta, explicacion):
        # Llamamos al constructor de la clase padre usando super()
        super().__init__(enunciado, categoria, dificultad, respuesta_correcta)

        # Validamos que la respuesta correcta sea únicamente Verdadero o Falso
        respuesta_limpia = str(respuesta_correcta).strip().capitalize()
        if respuesta_limpia != "Verdadero" and respuesta_limpia != "Falso":
            raise ValueError("En este tipo de pregunta la respuesta solo puede ser 'Verdadero' o 'Falso'.")

        self._respuesta_correcta = respuesta_limpia
        # Atributo propio: una breve explicación para enseñar al jugador por qué es V o F
        self._explicacion = explicacion

    @property
    def explicacion(self):
        return self._explicacion

    # --- Implementación de los métodos abstractos (Polimorfismo) ---

    def obtener_opciones(self):
        # Siempre devuelve únicamente estas dos opciones fijas
        return ["Verdadero", "Falso"]

    def calcular_puntos(self):
        """
        En Verdadero/Falso damos menos puntos porque hay 50% de probabilidad de acertar.
        """
        if self._dificultad == "Fácil":
            return 5
        elif self._dificultad == "Media":
            return 10
        elif self._dificultad == "Difícil":
            return 15
        else:
            return 5

    def obtener_tipo(self):
        return "Verdadero / Falso"

    def obtener_retroalimentacion(self, acertada):
        puntos = self.calcular_puntos()
        if acertada:
            mensaje = "¡Muy bien! Ganaste " + str(puntos) + " puntos.\n"
        else:
            mensaje = "Fallaste. Era " + str(self._respuesta_correcta) + ".\n"

        # Agregamos la explicación que caracteriza a esta clase hija
        mensaje = mensaje + "Nota: " + str(self._explicacion)
        return mensaje
