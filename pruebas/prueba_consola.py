# Archivo de pruebas sencillas para verificar que nuestras clases POO funcionan bien
import sys
import os

# Agregamos la carpeta raíz del proyecto al path para poder importar los paquetes
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ruta_raiz)

from modelos.pregunta_multiple import PreguntaMultiple
from modelos.pregunta_verdadero_falso import PreguntaVerdaderoFalso
from modelos.partida import Partida
from servicios.gestor_preguntas import GestorPreguntas


def ejecutar_pruebas():
    print("=== INICIANDO PRUEBAS DE LAS CLASES DE POO ===")

    # Prueba 1: Creación y polimorfismo entre PreguntaMultiple y PreguntaVerdaderoFalso
    p_mult = PreguntaMultiple(
        "¿Cuánto es 2 + 2?",
        "Matemáticas",
        "Fácil",
        "4",
        ["2", "3", "4", "5"]
    )
    p_vf = PreguntaVerdaderoFalso(
        "Python es un lenguaje que soporta Programación Orientada a Objetos.",
        "Programación",
        "Fácil",
        "Verdadero",
        "Python permite crear clases, objetos, herencia y polimorfismo."
    )

    lista_polimorfica = [p_mult, p_vf]
    for p in lista_polimorfica:
        print("Tipo:", p.obtener_tipo(), "| Puntos:", p.calcular_puntos(), "| Opciones:", p.obtener_opciones())

    assert p_mult.calcular_puntos() == 10
    assert p_vf.calcular_puntos() == 5
    assert p_mult.verificar_respuesta("4") is True
    assert p_vf.verificar_respuesta("falso") is False
    print("[OK] Prueba 1 superada: Herencia y Polimorfismo funcionan correctamente.")

    # Prueba 2: Encapsulamiento y control de vidas/puntaje en Partida
    partida = Partida("Carlos", "Programación")
    partida.sumar_puntos(10)
    partida.restar_vida()
    assert partida.puntaje == 10
    assert partida.vidas == 2
    print("[OK] Prueba 2 superada: Encapsulamiento de Partida funciona correctamente.")

    # Prueba 3: Validación de entrada inválida (nombre vacío o respuesta fuera de opciones)
    error_detectado = False
    try:
        partida_invalida = Partida("   ", "Ciencia")
    except ValueError:
        error_detectado = True

    assert error_detectado is True
    print("[OK] Prueba 3 superada: Validación de errores en datos inválidos funciona correctamente.")

    # Prueba 4: Gestor de preguntas
    gestor = GestorPreguntas()
    total_inicial = gestor.contar_total_preguntas()
    gestor.agregar_pregunta(p_mult)
    assert gestor.contar_total_preguntas() == total_inicial + 1
    print("[OK] Prueba 4 superada: GestorPreguntas agrega y filtra preguntas correctamente.")

    print("=== TODAS LAS PRUEBAS PASARON CON ÉXITO ===")


if __name__ == "__main__":
    ejecutar_pruebas()
