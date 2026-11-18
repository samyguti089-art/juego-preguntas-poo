import random
from modelos.pregunta_multiple import PreguntaMultiple
from modelos.pregunta_verdadero_falso import PreguntaVerdaderoFalso


class GestorPreguntas:
    """
    Clase de servicio que administra el banco de preguntas en memoria.
    Tiene una relación de AGREGACIÓN con las preguntas, porque guarda una lista
    de objetos de tipo PreguntaMultiple y PreguntaVerdaderoFalso.
    """

    def __init__(self):
        # Lista privada donde se guardan todos los objetos de tipo Pregunta
        self._banco_preguntas = []
        # Al crear el gestor, cargamos las preguntas por defecto del juego
        self.cargar_preguntas_iniciales()

    def cargar_preguntas_iniciales(self):
        """
        Crea varios objetos de PreguntaMultiple y PreguntaVerdaderoFalso
        y los guarda en la lista del banco de preguntas.
        """
        # --- Categoría: Programación ---
        p1 = PreguntaMultiple(
            "¿Qué método especial se usa como constructor en una clase de Python?",
            "Programación",
            "Fácil",
            "__init__",
            ["__start__", "__init__", "__main__", "constructor"]
        )

        p2 = PreguntaVerdaderoFalso(
            "En POO, la herencia permite que una clase hija reutilice atributos y métodos de una clase padre.",
            "Programación",
            "Fácil",
            "Verdadero",
            "La herencia evita repetir código común entre clases similares."
        )

        p3 = PreguntaMultiple(
            "¿Cómo se llama la capacidad de distintos objetos de responder diferente al mismo método?",
            "Programación",
            "Media",
            "Polimorfismo",
            ["Encapsulamiento", "Polimorfismo", "Instanciación", "Compilación"]
        )

        p4 = PreguntaVerdaderoFalso(
            "Una clase abstracta en Python se puede instanciar directamente sin crear clases hijas.",
            "Programación",
            "Difícil",
            "Falso",
            "Las clases abstractas con métodos abstractos solo sirven como plantilla y no se pueden instanciar directo."
        )

        # --- Categoría: Ciencia ---
        p5 = PreguntaMultiple(
            "¿Cuál es el planeta más grande del sistema solar?",
            "Ciencia",
            "Fácil",
            "Júpiter",
            ["Marte", "Tierra", "Júpiter", "Saturno"]
        )

        p6 = PreguntaVerdaderoFalso(
            "El agua hierve a 100 grados Celsius al nivel del mar.",
            "Ciencia",
            "Fácil",
            "Verdadero",
            "A presión atmosférica normal (nivel del mar), el punto de ebullición del agua es 100 °C."
        )

        p7 = PreguntaMultiple(
            "¿Qué órgano del cuerpo humano consume aproximadamente el 20% de la energía total?",
            "Ciencia",
            "Media",
            "El cerebro",
            ["El estómago", "El cerebro", "Los pulmones", "El hígado"]
        )

        # --- Categoría: Cultura General ---
        p8 = PreguntaMultiple(
            "¿En qué continente se encuentra ubicado Egipto principalmente?",
            "Cultura General",
            "Fácil",
            "África",
            ["Asia", "Europa", "África", "Oceanía"]
        )

        p9 = PreguntaVerdaderoFalso(
            "Gabriel García Márquez escribió la novela 'Cien años de soledad'.",
            "Cultura General",
            "Fácil",
            "Verdadero",
            "El escritor colombiano publicó esta obra maestra en 1967 y ganó el Nobel en 1982."
        )

        p10 = PreguntaMultiple(
            "¿Cuál es el océano más extenso del planeta Tierra?",
            "Cultura General",
            "Media",
            "Océano Pacífico",
            ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Ártico"]
        )

        # Guardamos todas las preguntas creadas usando nuestro método agregar_pregunta
        lista_inicial = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        for pregunta in lista_inicial:
            self.agregar_pregunta(pregunta)

    def agregar_pregunta(self, nueva_pregunta):
        """
        Agrega un objeto Pregunta al banco de preguntas en memoria.
        """
        if nueva_pregunta is not None:
            self._banco_preguntas.append(nueva_pregunta)

    def obtener_categorias(self):
        """
        Recorre las preguntas para devolver las categorías disponibles sin repetir.
        """
        categorias = ["Todas"]
        for pregunta in self._banco_preguntas:
            if pregunta.categoria not in categorias:
                categorias.append(pregunta.categoria)
        return categorias

    def obtener_preguntas_por_categoria(self, categoria_buscada):
        """
        Filtra las preguntas según la categoría elegida por el jugador
        y las mezcla aleatoriamente con random.shuffle().
        """
        preguntas_filtradas = []

        # Recorremos el banco con un ciclo for tradicional
        for pregunta in self._banco_preguntas:
            if categoria_buscada == "Todas" or pregunta.categoria == categoria_buscada:
                preguntas_filtradas.append(pregunta)

        # Mezclamos el orden para que cada partida sea diferente
        random.shuffle(preguntas_filtradas)
        return preguntas_filtradas

    def contar_total_preguntas(self):
        """
        Retorna cuántas preguntas hay registradas actualmente en el sistema.
        """
        return len(self._banco_preguntas)
