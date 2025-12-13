import flet as ft

def ConfirmDialog(page, titulo, texto, on_confirm):
    """
    Crea un diálogo de confirmación.
    Args:
        page: La página actual.
        titulo: Título de la alerta.
        texto: Mensaje del cuerpo.
        on_confirm: Función a ejecutar si el usuario dice "Sí".
    """
    
    def cerrar_dialogo(e):
        dialogo.open = False
        page.update()

    def confirmar_y_cerrar(e):
        dialogo.open = False
        page.update()
        on_confirm(e) # Ejecutamos la acción real

    dialogo = ft.AlertDialog(
        modal=True, # Obliga al usuario a responder
        title=ft.Text(titulo, weight=ft.FontWeight.BOLD),
        content=ft.Text(texto),
        actions=[
            ft.TextButton("Cancelar", on_click=cerrar_dialogo),
            ft.TextButton("Sí, eliminar", on_click=confirmar_y_cerrar, style=ft.ButtonStyle(color=ft.Colors.RED_400)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    return dialogo