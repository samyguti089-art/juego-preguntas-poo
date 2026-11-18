class Partida:
    """
    Clase que controla los datos de la partida actual del jugador:
    su nombre, categoría elegida, puntaje, vidas y cantidad de aciertos.
    Aquí aplicamos fuertemente el encapsulamiento para proteger las vidas y el puntaje.
    """

    def __init__(self, nombre_jugador, categoria_seleccionada):
        # Atributos encapsulados con guion bajo
        self._nombre_jugador = ""
        self._categoria_seleccionada = categoria_seleccionada
        self._puntaje = 0
        self._vidas = 3
        self._aciertos = 0
        self._errores = 0

        # Usamos el setter para validar el nombre desde el inicio
        self.nombre_jugador = nombre_jugador

    # --- Propiedades y validaciones (Encapsulamiento real) ---

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nuevo_nombre):
        nombre_limpio = str(nuevo_nombre).strip()
        if len(nombre_limpio) == 0:
            raise ValueError("El nombre del jugador no puede estar vacío.")
        self._nombre_jugador = nombre_limpio

    @property
    def categoria_seleccionada(self):
        return self._categoria_seleccionada

    @property
    def puntaje(self):
        return self._puntaje

    @property
    def vidas(self):
        return self._vidas

    @property
    def aciertos(self):
        return self._aciertos

    @property
    def errores(self):
        return self._errores

    # --- Métodos para modificar el estado de forma controlada ---

    def sumar_puntos(self, cantidad):
        """
        Suma puntos al jugador validando que la cantidad no sea negativa.
        """
        if cantidad > 0:
            self._puntaje = self._puntaje + cantidad
            self._aciertos = self._aciertos + 1

    def restar_vida(self):
        """
        Resta una vida cuando el jugador se equivoca o se acaba el tiempo.
        Evita que las vidas bajen de 0.
        """
        if self._vidas > 0:
            self._vidas = self._vidas - 1
        self._errores = self._errores + 1

    def sigue_con_vida(self):
        """
        Indica si el jugador todavía tiene vidas para seguir jugando.
        """
        if self._vidas > 0:
            return True
        else:
            return False

    def obtener_resumen(self):
        """
        Devuelve un texto con todas las estadísticas finales de la partida.
        """
        resumen = "Jugador: " + self._nombre_jugador + "\n"
        resumen = resumen + "Categoría: " + self._categoria_seleccionada + "\n"
        resumen = resumen + "Puntaje Total: " + str(self._puntaje) + " puntos\n"
        resumen = resumen + "Respuestas Correctas: " + str(self._aciertos) + "\n"
        resumen = resumen + "Respuestas Incorrectas: " + str(self._errores) + "\n"
        resumen = resumen + "Vidas restantes: " + str(self._vidas)
        return resumen
