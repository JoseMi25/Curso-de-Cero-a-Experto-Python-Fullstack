import flet as ft
from services import pelicula_service
from components.dialogs import ConfirmDialog

def HomeView(page: ft.Page, cambiar_vista):
    """
    Vista principal Responsiva: Tabla para PC, Tarjetas para Móvil.
    """
    id_para_eliminar = [None] 

    def recargar_tabla():
        cambiar_vista(0)

    def ejecutar_eliminacion(e):
        if id_para_eliminar[0] is not None:
            if pelicula_service.eliminar_pelicula(id_para_eliminar[0]):
                page.snack_bar = ft.SnackBar(content=ft.Text("🗑️ Eliminado correctamente"), bgcolor=ft.Colors.RED_700)
                page.snack_bar.open = True
                page.update()
                recargar_tabla()

    def abrir_confirmacion(e):
        id_pelicula = e.control.data
        id_para_eliminar[0] = id_pelicula
        dialogo = ConfirmDialog(page, "Eliminar", f"¿Borrar película ID {id_pelicula}?", ejecutar_eliminacion)
        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()

    # Obtener datos
    lista_peliculas = pelicula_service.obtener_todos()

    # ---------------- MODO ESCRITORIO (TABLA) ----------------
    def vista_escritorio():
        filas = []
        for peli in lista_peliculas:
            filas.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(peli.id))),
                    ft.DataCell(ft.Text(peli.titulo)),
                    ft.DataCell(ft.Text(peli.director)),
                    ft.DataCell(ft.Container(content=ft.Text(str(peli.puntuacion), color=ft.Colors.WHITE), bgcolor=ft.Colors.BLUE_GREY_700, padding=6, border_radius=6, alignment=ft.alignment.center)),
                    ft.DataCell(ft.Row(controls=[
                        ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE_400, data=peli.id, on_click=lambda e: cambiar_vista(1, e.control.data)),
                        ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400, data=peli.id, on_click=abrir_confirmacion),
                    ]))
                ])
            )
        
        tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Título")),
                ft.DataColumn(ft.Text("Director")),
                ft.DataColumn(ft.Text("Puntos")),
                ft.DataColumn(ft.Text("Acciones")),
            ],
            rows=filas,
            border=ft.border.all(1, ft.Colors.BLUE_GREY_600),
            heading_row_color=ft.Colors.BLACK38,
            heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_200),
        )
        return ft.Row([tabla], alignment=ft.MainAxisAlignment.CENTER, scroll=ft.ScrollMode.ALWAYS)

    # ---------------- MODO MÓVIL (TARJETAS) ----------------
    def vista_movil():
        items = []
        for peli in lista_peliculas:
            # Diseño de tarjeta individual
            tarjeta = ft.Container(
                bgcolor=ft.Colors.BLUE_GREY_800,
                padding=15,
                border_radius=10,
                margin=ft.margin.only(bottom=10),
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.MOVIE, color=ft.Colors.BLUE_200),
                        ft.Text(peli.titulo, size=18, weight=ft.FontWeight.BOLD, expand=True),
                        ft.Container(
                            content=ft.Text(str(peli.puntuacion), weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.BLACK26, padding=5, border_radius=5
                        )
                    ]),
                    ft.Text(f"Director: {peli.director}", color=ft.Colors.GREY_400, size=14),
                    ft.Divider(color=ft.Colors.GREY_700),
                    ft.Row([
                        ft.TextButton("Editar", icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE_400, data=peli.id, on_click=lambda e: cambiar_vista(1, e.control.data)),
                        ft.TextButton("Eliminar", icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400, data=peli.id, on_click=abrir_confirmacion),
                    ], alignment=ft.MainAxisAlignment.END)
                ])
            )
            items.append(tarjeta)
        
        return ft.Column(items, scroll=ft.ScrollMode.AUTO, expand=True)

    # ---------------- DECISIÓN DE VISTA ----------------
    # Si el ancho es menor a 600, mostramos móvil. Si no, escritorio.
    es_movil = page.width < 600
    
    contenido_principal = vista_movil() if es_movil else vista_escritorio()

    titulo = ft.Text("Mis Películas", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    btn_agregar = ft.ElevatedButton("Agregar Película", icon=ft.Icons.ADD, bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE, on_click=lambda e: cambiar_vista(1))

    return ft.Column(
        controls=[
            ft.Row([ft.Icon(ft.Icons.MOVIE, size=40, color=ft.Colors.BLUE_200), titulo], alignment=ft.MainAxisAlignment.CENTER),
            btn_agregar,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            contenido_principal
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )