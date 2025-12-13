import flet as ft

def CrearNavbar(funcion_cambio_vista):
    """
    Crea una barra de navegación inferior.
    Recibe una función (funcion_cambio_vista) que se ejecutará al hacer clic.
    """
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Agregar Película"),
        ],
        on_change=funcion_cambio_vista, # Ejecuta la lógica de app.py al cambiar
        bgcolor=ft.Colors.BLUE_GREY_800,
        indicator_color=ft.Colors.BLUE_200
    )