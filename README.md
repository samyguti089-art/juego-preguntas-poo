# 1. Nombre del proyecto
**Trivia POO — Juego de Preguntas Interactivo en Python**

Aplicación de escritorio interactiva de preguntas y respuestas con diferentes categorías, tipos de preguntas (Selección Múltiple y Verdadero/Falso), cálculo dinámico de puntaje, sistema de vidas y temporizador por pregunta, desarrollada aplicando los pilares de la Programación Orientada a Objetos (POO).

---

## 2. Descripción del problema
En el proceso de aprendizaje universitario y repaso de conceptos (como Programación, Ciencia o Cultura General), estudiar únicamente leyendo apuntes puede volverse monótono. Se identificó la necesidad de contar con una herramienta de escritorio ligera, sin dependencia de internet ni configuraciones complejas, que permita repasar contenidos mediante partidas dinámicas de preguntas y respuestas, permitiendo además que el propio estudiante agregue nuevas preguntas de repaso durante su sesión de estudio.

---

## 3. Objetivos

### Objetivo general
Diseñar y desarrollar un juego interactivo de preguntas en Python con interfaz gráfica en `Tkinter`, aplicando de forma práctica los conceptos de Programación Orientada a Objetos (clases, objetos, encapsulamiento, herencia, polimorfismo, abstracción y relaciones entre clases).

### Objetivos específicos
* Implementar una jerarquía de clases utilizando una clase abstracta base (`Pregunta`) y dos clases derivadas (`PreguntaMultiple` y `PreguntaVerdaderoFalso`).
* Proteger la integridad del estado del juego (vidas, puntaje, enunciados y nombre del jugador) mediante encapsulamiento y validaciones.
* Construir una interfaz gráfica amigable en `Tkinter` separada de la lógica del negocio.
* Permitir la ejecución de al menos tres funcionalidades completas desde la interfaz gráfica, incluyendo el registro de nuevas preguntas en memoria.

---

## 4. Funcionalidades
1. **Configuración e inicio de partida por categoría:** Permite ingresar el nombre del jugador (con validación de campo obligatorio) y filtrar las preguntas por una categoría específica (`Todas`, `Programación`, `Ciencia`, `Cultura General`) mezclándolas de forma aleatoria.
2. **Resolución interactiva de preguntas con temporizador y vidas:** Presenta cada pregunta adaptando los controles según su tipo (4 opciones para Selección Múltiple o 2 opciones para Verdadero/Falso), controla un reloj de 20 segundos por pregunta, calcula el puntaje polimórficamente según el tipo y dificultad, descuenta vidas ante errores o tiempo agotado, y muestra retroalimentación inmediata.
3. **Registro de nuevas preguntas personalizadas en memoria:** Permite crear y agregar nuevas preguntas (tanto de Selección Múltiple como de Verdadero/Falso) desde un formulario gráfico, validando que todos los datos sean coherentes antes de guardarlas en el banco de preguntas.

---

## 5. Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Interfaz Gráfica:** `tkinter` y `tkinter.ttk` (biblioteca gráfica estándar de Python)
* **Módulos estándar de soporte:**
  * `abc` (`ABC`, `abstractmethod`): Definición de clases y métodos abstractos.
  * `random` (`shuffle`): Mezcla aleatoria de preguntas en cada partida.

---

## 6. Instalación
Este proyecto utiliza únicamente bibliotecas estándar incluidas por defecto en Python, por lo que no requiere instalar paquetes externos complejos.

1. Verificar que tienes **Python 3.8 o superior** instalado:
   ```bash
   python --version
   ```
2. Clonar este repositorio de GitHub:
   ```bash
   git clone https://github.com/samyguti089-art/juego-preguntas-poo.git
   cd juego-preguntas-poo
   ```

---

## 7. Ejecución
Para iniciar la aplicación con su interfaz gráfica, ejecuta el archivo principal desde la raíz del proyecto:

```bash
python main.py
```

Para ejecutar las pruebas de consola que verifican las clases de POO:

```bash
python pruebas/prueba_consola.py
```

---

## 8. Manual de usuario

### Paso 1: Menú Principal
Al abrir el programa verás la pantalla principal:
1. Escribe tu nombre en el campo **"Nombre del Jugador"**.
2. Elige la categoría que deseas practicar en la lista desplegable **"Selecciona una Categoría"**.
3. Haz clic en **"Iniciar Partida"**. *(Si dejas el nombre vacío, el sistema mostrará una alerta pidiéndote completarlo).*

*(Puedes colocar aquí tu captura: `![Menú Principal](docs/imagenes/menu_principal.png)`)*

### Paso 2: Responder Preguntas
Durante la partida:
1. En la barra superior verás tu nombre, puntaje acumulado, vidas restantes (inicias con 3 vidas) y el tiempo restante (20 segundos por pregunta).
2. Selecciona una de las opciones marcando su botón circular (`Radiobutton`).
3. Presiona **"Confirmar Respuesta"** para validar si acertaste y ver la retroalimentación o explicación.
4. Presiona **"Siguiente Pregunta"** para avanzar hasta completar el cuestionario o agotar tus vidas.

*(Puedes colocar aquí tu captura: `![Pantalla de Juego](docs/imagenes/pantalla_juego.png)`)*

### Paso 3: Agregar una Nueva Pregunta
Desde el menú principal haz clic en **"Agregar Nueva Pregunta al Banco"**:
1. Selecciona el **Tipo de Pregunta** (`Selección Múltiple` o `Verdadero / Falso`), escribe la **Categoría** y elige la **Dificultad** (`Fácil`, `Media` o `Difícil`).
2. Escribe el enunciado y la respuesta correcta.
3. Si es de Selección Múltiple, escribe las opciones separadas por coma (asegurándote de incluir la respuesta correcta entre ellas). Si es de Verdadero/Falso, escribe una breve explicación.
4. Haz clic en **"Guardar Pregunta"**. El contador del menú principal aumentará inmediatamente.

*(Puedes colocar aquí tu captura: `![Agregar Pregunta](docs/imagenes/agregar_pregunta.png)`)*

---

## 9. Estructura del proyecto
```text
juego_preguntas_poo/
│
├── main.py                              # Punto de entrada que inicia la aplicación
│
├── modelos/                             # Capa de entidades y modelos de POO
│   ├── __init__.py
│   ├── pregunta.py                      # Clase abstracta base Pregunta (ABC)
│   ├── pregunta_multiple.py             # Subclase para preguntas de selección múltiple
│   ├── pregunta_verdadero_falso.py      # Subclase para preguntas de Verdadero o Falso
│   └── partida.py                       # Clase que encapsula el estado del jugador y vidas
│
├── servicios/                           # Capa de lógica de negocio
│   ├── __init__.py
│   └── gestor_preguntas.py              # Administra, filtra y mezcla el banco de preguntas
│
├── interfaz/                            # Capa de interfaz gráfica de usuario (GUI)
│   ├── __init__.py
│   └── ventana_principal.py             # Ventana principal y pantallas en Tkinter
│
├── pruebas/                             # Pruebas de verificación de clases
│   └── prueba_consola.py                # Script de pruebas unitarias básicas
│
├── docs/                                # Documentación técnica del proyecto
│   ├── INFORME_TECNICO.md               # Informe detallado de arquitectura y POO
│   └── imagenes/                        # Carpeta para capturas de pantalla
│
├── requirements.txt                     # Detalle de bibliotecas utilizadas
└── README.md                            # Documentación general y manual de usuario
```

---

## 10. Autor
* **Estudiante:** Samuel David Gutierrez Mantilla
* **Programa:** Ingeniería de Sistemas — 4.º Semestre
* **Asignatura:** Programación Orientada a Objetos
