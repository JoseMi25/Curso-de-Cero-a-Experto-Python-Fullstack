import flet as ft
from services import pelicula_service

def FormView(page: ft.Page, cambiar_vista, id_pelicula=None):
    """
    Vista del formulario con Diseño Responsivo.
    """

    # ---------------- LÓGICA DE VALIDACIÓN ----------------
    def validar_formulario(e=None):
        val_titulo = tf_titulo.value.strip() if tf_titulo.value else ""
        val_director = tf_director.value.strip() if tf_director.value else ""
        val_puntuacion = tf_puntuacion.value.strip() if tf_puntuacion.value else ""

        es_valido = True
        
        if not val_titulo or not val_director or not val_puntuacion:
            es_valido = False
        else:
            if not val_puntuacion.isdigit():
                es_valido = False
                tf_puntuacion.error_text = "Solo números"
            else:
                puntos = int(val_puntuacion)
                if not (1 <= puntos <= 10):
                    es_valido = False
                    tf_puntuacion.error_text = "Entre 1 y 10"
                else:
                    tf_puntuacion.error_text = None

        btn_guardar.disabled = not es_valido
        page.update()

    # ---------------- CAMPOS ----------------
    tf_titulo = ft.TextField(label="Título", prefix_icon=ft.Icons.MOVIE, border_radius=8, border_color=ft.Colors.BLUE_200, on_change=validar_formulario)
    tf_director = ft.TextField(label="Director", prefix_icon=ft.Icons.PERSON, border_radius=8, border_color=ft.Colors.BLUE_200, on_change=validar_formulario)
    tf_puntuacion = ft.TextField(label="Puntos (1-10)", prefix_icon=ft.Icons.STAR, keyboard_type=ft.KeyboardType.NUMBER, border_radius=8, border_color=ft.Colors.BLUE_200, on_change=validar_formulario)

    # ---------------- PRECARGA ----------------
    titulo_texto = "Nueva Película"
    boton_texto = "Guardar"
    icono_titulo = ft.Icons.MOVIE_CREATION

    if id_pelicula is not None:
        pelicula_editar = pelicula_service.obtener_por_id(id_pelicula)
        if pelicula_editar:
            tf_titulo.value = pelicula_editar.titulo
            tf_director.value = pelicula_editar.director
            tf_puntuacion.value = str(pelicula_editar.puntuacion)
            titulo_texto = "Editar Película"
            boton_texto = "Actualizar"
            icono_titulo = ft.Icons.EDIT_SQUARE

    # ---------------- UTILIDADES ----------------
    mensaje_container = ft.Container(visible=False, padding=15, border_radius=10, margin=ft.margin.only(bottom=10))

    def mostrar_mensaje(texto, es_error=False):
        icon = ft.Icons.ERROR if es_error else ft.Icons.CHECK_CIRCLE
        color_bg = ft.Colors.RED_600 if es_error else ft.Colors.GREEN_700
        mensaje_container.content = ft.Row([ft.Icon(icon, color=ft.Colors.WHITE), ft.Text(texto, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER)
        mensaje_container.bgcolor = color_bg
        mensaje_container.visible = True
        page.update()
        if not es_error:
            import time, threading
            threading.Thread(target=lambda: (time.sleep(1.5), volver_inicio()), daemon=True).start()

    def volver_inicio():
        cambiar_vista(0)

    def guardar(e):
        try:
            puntos = int(tf_puntuacion.value)
            if id_pelicula is None:
                pelicula_service.crear_pelicula(tf_titulo.value.strip(), tf_director.value.strip(), puntos)
                mostrar_mensaje("¡Película creada!")
            else:
                pelicula_service.actualizar_pelicula(id_pelicula, tf_titulo.value.strip(), tf_director.value.strip(), puntos)
                mostrar_mensaje("¡Actualizado!")
        except Exception as error:
            mostrar_mensaje(str(error), es_error=True)

    # ---------------- LAYOUT RESPONSIVO ----------------
    btn_guardar = ft.ElevatedButton(text=boton_texto, icon=ft.Icons.SAVE, bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE, height=45, on_click=guardar, disabled=True, expand=True)
    btn_cancelar = ft.OutlinedButton(text="Cancelar", icon=ft.Icons.CANCEL, height=45, on_click=lambda e: volver_inicio(), style=ft.ButtonStyle(color=ft.Colors.RED_300, side=ft.BorderSide(2, ft.Colors.RED_300)), expand=True)
    
    validar_formulario()

    # [NUEVO] Cálculo dinámico del ancho
    ancho_tarjeta = 500
    if page.width < 600:
        ancho_tarjeta = page.width - 20 # Ocupa casi todo el ancho en móvil

    card = ft.Container(
        width=ancho_tarjeta,
        padding=25, border_radius=20, bgcolor=ft.Colors.BLUE_GREY_800,
        shadow=ft.BoxShadow(blur_radius=25, color=ft.Colors.BLACK54, offset=ft.Offset(0, 8)),
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Icon(icono_titulo, size=50, color=ft.Colors.BLUE_200),
                ft.Text(titulo_texto, size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                mensaje_container,
                tf_titulo, tf_director, tf_puntuacion,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                # Botones en fila que se expanden
                ft.Row([btn_guardar, btn_cancelar], spacing=10)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    return ft.Column(controls=[card], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)