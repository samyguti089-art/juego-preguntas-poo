import tkinter as tk
from tkinter import ttk, messagebox
from modelos.partida import Partida
from modelos.pregunta_multiple import PreguntaMultiple
from modelos.pregunta_verdadero_falso import PreguntaVerdaderoFalso


class VentanaPrincipal:
    """
    Clase encargada de la interfaz gráfica del juego usando Tkinter.
    Se comunica con GestorPreguntas (Asociación) y crea la Partida (Composición).
    """

    def __init__(self, raiz, gestor_preguntas):
        self.raiz = raiz
        self.gestor = gestor_preguntas

        # Configuración básica de la ventana principal
        self.raiz.title("Trivia POO - Juego de Preguntas Interactivo")
        self.raiz.geometry("700x560")
        self.raiz.resizable(False, False)
        self.raiz.configure(bg="#f0f4f8")

        # Variables de control para el estado del juego actual
        self.partida_actual = None
        self.preguntas_partida = []
        self.indice_pregunta = 0
        self.tiempo_restante = 20
        self.id_temporizador = None
        self.pregunta_respondida = False

        # Variable de Tkinter para guardar qué opción marcó el usuario en los Radiobutton
        self.opcion_seleccionada = tk.StringVar(value="")

        # Creamos los 3 contenedores (Frames) para cambiar de pantalla fácilmente
        self.frame_menu = tk.Frame(self.raiz, bg="#f0f4f8")
        self.frame_juego = tk.Frame(self.raiz, bg="#f0f4f8")
        self.frame_registro = tk.Frame(self.raiz, bg="#f0f4f8")

        # Construimos los elementos de cada pantalla
        self.construir_pantalla_menu()
        self.construir_pantalla_juego()
        self.construir_pantalla_registro()

        # Al abrir el programa mostramos primero el menú principal
        self.mostrar_menu()

    # =========================================================================
    # PANTALLA 1: MENÚ PRINCIPAL
    # =========================================================================

    def construir_pantalla_menu(self):
        # Título principal
        lbl_titulo = tk.Label(
            self.frame_menu,
            text="TRIVIA INTERACTIVA POO",
            font=("Arial", 22, "bold"),
            bg="#f0f4f8",
            fg="#1e3a8a"
        )
        lbl_titulo.pack(pady=(35, 5))

        lbl_subtitulo = tk.Label(
            self.frame_menu,
            text="Pon a prueba tus conocimientos en diferentes categorías",
            font=("Arial", 11),
            bg="#f0f4f8",
            fg="#475569"
        )
        lbl_subtitulo.pack(pady=(0, 20))

        # Tarjeta central para pedir los datos del jugador
        panel_datos = tk.Frame(self.frame_menu, bg="#ffffff", bd=1, relief="solid", padx=30, pady=25)
        panel_datos.pack(pady=10)

        # Campo: Nombre del jugador
        lbl_nombre = tk.Label(
            panel_datos,
            text="Nombre del Jugador:",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            fg="#1e293b"
        )
        lbl_nombre.pack(anchor="w", pady=(0, 5))

        self.entrada_nombre = tk.Entry(panel_datos, font=("Arial", 12), width=32, bd=1, relief="solid")
        self.entrada_nombre.pack(pady=(0, 15))

        # Campo: Selección de categoría
        lbl_categoria = tk.Label(
            panel_datos,
            text="Selecciona una Categoría:",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            fg="#1e293b"
        )
        lbl_categoria.pack(anchor="w", pady=(0, 5))

        self.combo_categoria = ttk.Combobox(
            panel_datos,
            font=("Arial", 11),
            width=30,
            state="readonly"
        )
        self.combo_categoria.pack(pady=(0, 20))

        # Botón para iniciar la partida (Funcionalidad 1)
        btn_iniciar = tk.Button(
            panel_datos,
            text="Iniciar Partida",
            font=("Arial", 12, "bold"),
            bg="#2563eb",
            fg="#ffffff",
             width=25,
            pady=6,
            cursor="hand2",
            command=self.iniciar_nueva_partida
        )
        btn_iniciar.pack(pady=(5, 10))

        # Botón para ir a registrar una nueva pregunta (Funcionalidad 3)
        btn_ir_registro = tk.Button(
            panel_datos,
            text="Agregar Nueva Pregunta al Banco",
            font=("Arial", 10, "bold"),
            bg="#059669",
            fg="#ffffff",
            width=28,
            pady=5,
            cursor="hand2",
            command=self.mostrar_pantalla_registro
        )
        btn_ir_registro.pack(pady=5)

        # Etiqueta inferior que muestra cuántas preguntas hay cargadas en memoria
        self.lbl_total_banco = tk.Label(
            self.frame_menu,
            text="",
            font=("Arial", 10, "italic"),
            bg="#f0f4f8",
            fg="#64748b"
        )
        self.lbl_total_banco.pack(pady=20)

    def mostrar_menu(self):
        # Detenemos el reloj por si estaba corriendo
        self.detener_temporizador()

        # Ocultamos las otras pantallas y mostramos el menú
        self.frame_juego.pack_forget()
        self.frame_registro.pack_forget()
        self.frame_menu.pack(fill="both", expand=True)

        # Actualizamos la lista de categorías y el contador de preguntas
        lista_categorias = self.gestor.obtener_categorias()
        self.combo_categoria["values"] = lista_categorias
        if len(lista_categorias) > 0:
            self.combo_categoria.current(0)

        total = self.gestor.contar_total_preguntas()
        self.lbl_total_banco.config(text="Preguntas disponibles actualmente en memoria: " + str(total))

    # =========================================================================
    # PANTALLA 2: JUEGO DE PREGUNTAS (FUNCIONALIDADES 1 Y 2)
    # =========================================================================

    def construir_pantalla_juego(self):
        # Barra superior de estado (Jugador, Puntaje, Vidas, Tiempo)
        barra_superior = tk.Frame(self.frame_juego, bg="#1e3a8a", padx=15, pady=10)
        barra_superior.pack(fill="x")

        self.lbl_info_jugador = tk.Label(
            barra_superior,
            text="Jugador: -",
            font=("Arial", 11, "bold"),
            bg="#1e3a8a",
            fg="#ffffff"
        )
        self.lbl_info_jugador.pack(side="left", padx=10)

        self.lbl_info_puntaje = tk.Label(
            barra_superior,
            text="Puntaje: 0",
            font=("Arial", 11, "bold"),
            bg="#1e3a8a",
            fg="#fde047"
        )
        self.lbl_info_puntaje.pack(side="left", padx=15)

        self.lbl_info_vidas = tk.Label(
            barra_superior,
            text="Vidas: 3",
            font=("Arial", 11, "bold"),
            bg="#1e3a8a",
            fg="#fca5a5"
        )
        self.lbl_info_vidas.pack(side="left", padx=15)

        self.lbl_temporizador = tk.Label(
            barra_superior,
            text="Tiempo: 20 s",
            font=("Arial", 11, "bold"),
            bg="#1e3a8a",
            fg="#86efac"
        )
        self.lbl_temporizador.pack(side="right", padx=10)

        # Etiqueta con datos técnicos de la pregunta (Demuestra Polimorfismo)
        self.lbl_meta_pregunta = tk.Label(
            self.frame_juego,
            text="Categoría | Tipo | Valor",
            font=("Arial", 10, "bold"),
            bg="#f0f4f8",
            fg="#334155"
        )
        self.lbl_meta_pregunta.pack(pady=(15, 5))

        # Tarjeta para mostrar el enunciado y las opciones
        panel_pregunta = tk.Frame(self.frame_juego, bg="#ffffff", bd=1, relief="solid", padx=25, pady=20)
        panel_pregunta.pack(padx=30, pady=5, fill="both", expand=True)

        self.lbl_enunciado = tk.Label(
            panel_pregunta,
            text="Aquí aparecerá el enunciado de la pregunta",
            font=("Arial", 13, "bold"),
            bg="#ffffff",
            fg="#0f172a",
            wraplength=580,
            justify="left"
        )
        self.lbl_enunciado.pack(anchor="w", pady=(0, 15))

        # Contenedor donde se colocarán los Radiobutton de las opciones
        self.contenedor_opciones = tk.Frame(panel_pregunta, bg="#ffffff")
        self.contenedor_opciones.pack(fill="x", pady=5)

        # Creamos 4 Radiobuttons reutilizables para mostrar 2 o 4 opciones según el tipo de pregunta
        self.botones_radio = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.contenedor_opciones,
                text="",
                variable=self.opcion_seleccionada,
                value="",
                font=("Arial", 11),
                bg="#ffffff",
                 fg="#1e293b",
                activebackground="#e2e8f0",
                anchor="w",
                padx=10,
                pady=4
            )
            self.botones_radio.append(rb)

        # Etiqueta para mostrar si acertó o falló y la explicación
        self.lbl_retroalimentacion = tk.Label(
            panel_pregunta,
            text="",
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            fg="#1e3a8a",
            wraplength=580,
            justify="left"
        )
        self.lbl_retroalimentacion.pack(anchor="w", pady=(15, 5))

        # Barra inferior con botones de acción
        barra_botones = tk.Frame(self.frame_juego, bg="#f0f4f8", pady=12)
        barra_botones.pack(fill="x", padx=30)

        self.btn_confirmar = tk.Button(
            barra_botones,
            text="Confirmar Respuesta",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="#ffffff",
            width=18,
            pady=5,
            command=self.confirmar_respuesta
        )
        self.btn_confirmar.pack(side="left", padx=5)

        self.btn_siguiente = tk.Button(
            barra_botones,
            text="Siguiente Pregunta",
            font=("Arial", 11, "bold"),
            bg="#0d9488",
            fg="#ffffff",
            width=18,
            pady=5,
            state="disabled",
            command=self.avanzar_siguiente_pregunta
        )
        self.btn_siguiente.pack(side="left", padx=5)

        btn_salir = tk.Button(
            barra_botones,
            text="Volver al Menú",
            font=("Arial", 10),
            bg="#64748b",
            fg="#ffffff",
            width=14,
            pady=5,
            command=self.mostrar_menu
        )
        btn_salir.pack(side="right", padx=5)

    def iniciar_nueva_partida(self):
        """
        Valida los datos del menú, crea el objeto Partida y arranca el juego.
        """
        nombre = self.entrada_nombre.get()
        categoria = self.combo_categoria.get()

        # Intentamos crear la Partida. Si el nombre está vacío, la clase Partida lanza ValueError
        try:
            self.partida_actual = Partida(nombre, categoria)
        except ValueError as error:
            messagebox.showwarning("Dato inválido", str(error))
            return

        # Pedimos al gestor las preguntas de esa categoría
        self.preguntas_partida = self.gestor.obtener_preguntas_por_categoria(categoria)
        if len(self.preguntas_partida) == 0:
            messagebox.showinfo("Sin preguntas", "No hay preguntas registradas en esta categoría.")
            return

        self.indice_pregunta = 0

        # Cambiamos a la pantalla de juego
        self.frame_menu.pack_forget()
        self.frame_juego.pack(fill="both", expand=True)

        # Cargamos la primera pregunta
        self.mostrar_pregunta_actual()

    def mostrar_pregunta_actual(self):
        """
        Muestra en pantalla la pregunta correspondiente al índice actual.
        """
        self.detener_temporizador()
        self.pregunta_respondida = False
        self.opcion_seleccionada.set("")
        self.lbl_retroalimentacion.config(text="")

        # Activamos el botón de confirmar y desactivamos el de siguiente
        self.btn_confirmar.config(state="normal")
        self.btn_siguiente.config(state="disabled")

        # Actualizamos los datos de la barra superior
        self.actualizar_barra_estado()

        # Obtenemos el objeto pregunta actual (puede ser PreguntaMultiple o PreguntaVerdaderoFalso)
        pregunta = self.preguntas_partida[self.indice_pregunta]

        # Aquí se aplica POLIMORFISMO: llamamos a obtener_tipo(), calcular_puntos() y obtener_opciones()
        # sin importar cuál de las dos clases hijas sea
        numero_actual = self.indice_pregunta + 1
        total_preguntas = len(self.preguntas_partida)
        texto_meta = (
            "Pregunta " + str(numero_actual) + " de " + str(total_preguntas) +
            "  |  Categoría: " + pregunta.categoria +
            "  |  Dificultad: " + pregunta.dificultad +
            "  |  Tipo: " + pregunta.obtener_tipo() +
            "  |  Valor: " + str(pregunta.calcular_puntos()) + " pts"
        )
        self.lbl_meta_pregunta.config(text=texto_meta)
        self.lbl_enunciado.config(text=pregunta.enunciado)

        # Obtenemos las opciones de forma polimórfica (4 opciones o 2 opciones)
        opciones = pregunta.obtener_opciones()

        # Primero ocultamos todos los Radiobutton y luego mostramos solo los necesarios
        for rb in self.botones_radio:
            rb.pack_forget()

        for i in range(len(opciones)):
            texto_opcion = opciones[i]
            self.botones_radio[i].config(text=texto_opcion, value=texto_opcion, state="normal")
            self.botones_radio[i].pack(anchor="w", pady=3)

        # Iniciamos el temporizador de 20 segundos para esta pregunta
        self.tiempo_restante = 20
        self.lbl_temporizador.config(text="Tiempo: " + str(self.tiempo_restante) + " s")
        self.ejecutar_temporizador()

    def ejecutar_temporizador(self):
        """
        Descuenta 1 segundo cada 1000 milisegundos usando after() de Tkinter.
        """
        if self.pregunta_respondida:
            return

        if self.tiempo_restante > 0:
            self.lbl_temporizador.config(text="Tiempo: " + str(self.tiempo_restante) + " s")
            self.tiempo_restante = self.tiempo_restante - 1
            self.id_temporizador = self.raiz.after(1000, self.ejecutar_temporizador)
        else:
            # Si el tiempo llega a 0, el jugador pierde una vida automáticamente
            self.lbl_temporizador.config(text="¡Tiempo agotado!")
            self.procesar_tiempo_agotado()

    def detener_temporizador(self):
        if self.id_temporizador is not None:
            self.raiz.after_cancel(self.id_temporizador)
            self.id_temporizador = None

    def confirmar_respuesta(self):
        """
        Verifica si la opción seleccionada por el usuario es correcta.
        """
        if self.pregunta_respondida:
            return

        respuesta_elegida = self.opcion_seleccionada.get()
        if respuesta_elegida == "":
            messagebox.showwarning("Atención", "Por favor selecciona una opción antes de confirmar.")
            return

        self.pregunta_respondida = True
        self.detener_temporizador()

        pregunta = self.preguntas_partida[self.indice_pregunta]
        es_correcta = pregunta.verificar_respuesta(respuesta_elegida)

        if es_correcta:
            puntos_ganados = pregunta.calcular_puntos()
            self.partida_actual.sumar_puntos(puntos_ganados)
            self.lbl_retroalimentacion.config(
                text=pregunta.obtener_retroalimentacion(True),
                fg="#15803d"
            )
        else:
            self.partida_actual.restar_vida()
            self.lbl_retroalimentacion.config(
                text=pregunta.obtener_retroalimentacion(False),
                fg="#b91c1c"
            )

        self.actualizar_barra_estado()
        self.bloquear_opciones_Y_preparar_avance()

    def procesar_tiempo_agotado(self):
        """
        Se ejecuta cuando el jugador no responde antes de que el reloj llegue a 0.
        """
        self.pregunta_respondida = True
        pregunta = self.preguntas_partida[self.indice_pregunta]
        self.partida_actual.restar_vida()

        mensaje = "Se acabó el tiempo. Perdiste 1 vida.\n" + pregunta.obtener_retroalimentacion(False)
        self.lbl_retroalimentacion.config(text=mensaje, fg="#b91c1c")

        self.actualizar_barra_estado()
        self.bloquear_opciones_Y_preparar_avance()

    def bloquear_opciones_Y_preparar_avance(self):
        # Deshabilitamos los Radiobuttons para que no cambie su respuesta
        for rb in self.botones_radio:
            rb.config(state="disabled")

        self.btn_confirmar.config(state="disabled")
        self.btn_siguiente.config(state="normal")

    def avanzar_siguiente_pregunta(self):
        """
        Pasa a la siguiente pregunta o termina el juego si ya no hay vidas o preguntas.
        """
        # Verificamos si el jugador todavía tiene vidas
        if not self.partida_actual.sigue_con_vida():
            messagebox.showinfo(
                "Fin de la Partida - Sin vidas",
                "Te has quedado sin vidas.\n\n" + self.partida_actual.obtener_resumen()
            )
            self.mostrar_menu()
            return

        # Avanzamos el índice de la lista de preguntas
        self.indice_pregunta = self.indice_pregunta + 1

        if self.indice_pregunta < len(self.preguntas_partida):
            self.mostrar_pregunta_actual()
        else:
            messagebox.showinfo(
                "¡Partida Completada!",
                "Has respondido todas las preguntas de la partida.\n\n" + self.partida_actual.obtener_resumen()
            )
            self.mostrar_menu()

    def actualizar_barra_estado(self):
        self.lbl_info_jugador.config(text="Jugador: " + self.partida_actual.nombre_jugador)
        self.lbl_info_puntaje.config(text="Puntaje: " + str(self.partida_actual.puntaje))
        self.lbl_info_vidas.config(text="Vidas: " + str(self.partida_actual.vidas))

    # =========================================================================
    # PANTALLA 3: AGREGAR NUEVA PREGUNTA AL BANCO (FUNCIONALIDAD 3)
    # =========================================================================

    def construir_pantalla_registro(self):
        lbl_titulo = tk.Label(
            self.frame_registro,
            text="AGREGAR NUEVA PREGUNTA",
            font=("Arial", 18, "bold"),
            bg="#f0f4f8",
            fg="#1e3a8a"
        )
        lbl_titulo.pack(pady=(20, 10))

        panel_form = tk.Frame(self.frame_registro, bg="#ffffff", bd=1, relief="solid", padx=25, pady=15)
        panel_form.pack(padx=30, pady=5, fill="both", expand=True)

        # Fila 1: Tipo de pregunta y Categoría
        fila_super = tk.Frame(panel_form, bg="#ffffff")
        fila_super.pack(fill="x", pady=5)

        tk.Label(fila_super, text="Tipo de Pregunta:", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", padx=5)
        self.combo_tipo_nueva = ttk.Combobox(
            fila_super,
            values=["Selección Múltiple", "Verdadero / Falso"],
            state="readonly",
            width=20
        )
        self.combo_tipo_nueva.current(0)
        self.combo_tipo_nueva.grid(row=1, column=0, padx=5, pady=3)
        self.combo_tipo_nueva.bind("<<ComboboxSelected>>", self.cambiar_tipo_formulario)

        tk.Label(fila_super, text="Categoría:", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=0, column=1, sticky="w", padx=5)
        self.entrada_categoria_nueva = tk.Entry(fila_super, font=("Arial", 10), width=20, bd=1, relief="solid")
        self.entrada_categoria_nueva.insert(0, "Programación")
        self.entrada_categoria_nueva.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(fila_super, text="Dificultad:", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=0, column=2, sticky="w", padx=5)
        self.combo_dificultad_nueva = ttk.Combobox(
            fila_super,
            values=["Fácil", "Media", "Difícil"],
            state="readonly",
            width=14
        )
        self.combo_dificultad_nueva.current(0)
        self.combo_dificultad_nueva.grid(row=1, column=2, padx=5, pady=3)

        # Enunciado
        tk.Label(panel_form, text="Enunciado de la pregunta:", font=("Arial", 10, "bold"), bg="#ffffff").pack(anchor="w", pady=(10, 2))
        self.entrada_enunciado_nuevo = tk.Entry(panel_form, font=("Arial", 11), width=62, bd=1, relief="solid")
        self.entrada_enunciado_nuevo.pack(anchor="w", pady=(0, 8))

        # Respuesta correcta
        tk.Label(panel_form, text="Respuesta Correcta (debe coincidir con una opción o ser Verdadero/Falso):", font=("Arial", 10, "bold"), bg="#ffffff").pack(anchor="w", pady=(5, 2))
        self.entrada_respuesta_nueva = tk.Entry(panel_form, font=("Arial", 11), width=62, bd=1, relief="solid")
        self.entrada_respuesta_nueva.pack(anchor="w", pady=(0, 8))

        # Sub-panel dinámico para las 4 opciones (Selección Múltiple) o la explicación (V/F)
        self.lbl_extra_form = tk.Label(
            panel_form,
            text="Opciones separadas por coma (ejemplo: Opción A, Opción B, Opción C, Opción D):",
            font=("Arial", 10, "bold"),
            bg="#ffffff"
        )
        self.lbl_extra_form.pack(anchor="w", pady=(5, 2))

        self.entrada_extra_nueva = tk.Entry(panel_form, font=("Arial", 11), width=62, bd=1, relief="solid")
        self.entrada_extra_nueva.pack(anchor="w", pady=(0, 15))

        # Botones de guardar o cancelar
        fila_botones = tk.Frame(panel_form, bg="#ffffff")
        fila_botones.pack(pady=10)

        btn_guardar = tk.Button(
            fila_botones,
            text="Guardar Pregunta",
            font=("Arial", 11, "bold"),
            bg="#059669",
            fg="#ffffff",
            width=18,
            pady=5,
            command=self.guardar_nueva_pregunta
        )
        btn_guardar.pack(side="left", padx=10)

        btn_volver = tk.Button(
            fila_botones,
            text="Cancelar y Volver",
            font=("Arial", 11),
            bg="#64748b",
            fg="#ffffff",
            width=18,
            pady=5,
            command=self.mostrar_menu
        )
        btn_volver.pack(side="left", padx=10)

    def mostrar_pantalla_registro(self):
        self.frame_menu.pack_forget()
        self.frame_juego.pack_forget()
        self.frame_registro.pack(fill="both", expand=True)

    def cambiar_tipo_formulario(self, evento=None):
        """
        Cambia el texto de ayuda dependiendo de si el usuario elige Selección Múltiple o V/F.
        """
        tipo = self.combo_tipo_nueva.get()
        if tipo == "Selección Múltiple":
            self.lbl_extra_form.config(
                text="Opciones separadas por coma (ejemplo: Opción 1, Opción 2, Opción 3, Opción 4):"
            )
        else:
            self.lbl_extra_form.config(
                text="Explicación breve de por qué la respuesta es Verdadero o Falso:"
            )

    def guardar_nueva_pregunta(self):
        """
        Recoge los datos del formulario, instancia la subclase correspondiente
        y la guarda en el GestorPreguntas.
        """
        tipo = self.combo_tipo_nueva.get()
        categoria = self.entrada_categoria_nueva.get().strip()
        dificultad = self.combo_dificultad_nueva.get()
        enunciado = self.entrada_enunciado_nuevo.get().strip()
        respuesta = self.entrada_respuesta_nueva.get().strip()
        texto_extra = self.entrada_extra_nueva.get().strip()

        try:
            if tipo == "Selección Múltiple":
                # Separamos las opciones por coma usando un ciclo básico
                partes = texto_extra.split(",")
                lista_opciones = []
                for parte in partes:
                    opcion_limpia = parte.strip()
                    if len(opcion_limpia) > 0:
                        lista_opciones.append(opcion_limpia)

                nueva_pregunta = PreguntaMultiple(
                    enunciado,
                    categoria,
                    dificultad,
                    respuesta,
                    lista_opciones
                )
            else:
                if len(texto_extra) == 0:
                    texto_extra = "Sin explicación adicional."

                nueva_pregunta = PreguntaVerdaderoFalso(
                    enunciado,
                    categoria,
                    dificultad,
                    respuesta,
                    texto_extra
                )

            # Si no hubo errores de validación, agregamos la pregunta al gestor
            self.gestor.agregar_pregunta(nueva_pregunta)
            messagebox.showinfo("Éxito", "¡La pregunta se registró correctamente en el banco!")

            # Limpiamos los campos después de guardar
            self.entrada_enunciado_nuevo.delete(0, tk.END)
            self.entrada_respuesta_nueva.delete(0, tk.END)
            self.entrada_extra_nueva.delete(0, tk.END)

            # Regresamos al menú principal
            self.mostrar_menu()

        except ValueError as error:
            messagebox.showerror("Error de validación", str(error))
