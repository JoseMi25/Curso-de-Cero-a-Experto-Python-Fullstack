import flet as ft
import socket
from views.home_view import HomeView
from views.form_view import FormView
from components.navbar import CrearNavbar

def main(page: ft.Page):
    """
    Función principal de la aplicación
    """
    # Configuración de la página
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    # Contenedor principal para las vistas
    contenedor_vista = ft.Container(
        expand=True,
        alignment=ft.alignment.top_center
    )
    
    def cambiar_vista_navbar(e):
        """Maneja el cambio de vista desde la navbar"""
        index = e.control.selected_index
        cambiar_a_vista(index)
    
    def cambiar_a_vista(index, data=None):
        """
        Función helper para cambiar de vista programáticamente
        Args:
            index: 0 para Home, 1 para Formulario
            data: ID de la película (opcional, solo para editar)
        """
        # Actualizar el índice seleccionado en la navbar
        page.navigation_bar.selected_index = index
        
        # Cambiar el contenido según el índice
        if index == 0:
            contenedor_vista.content = HomeView(page, cambiar_a_vista)
        elif index == 1:
            # Pasamos 'data' como id_pelicula
            contenedor_vista.content = FormView(page, cambiar_a_vista, id_pelicula=data)
        
        page.update()
    
    # Configurar navbar
    page.navigation_bar = CrearNavbar(cambiar_vista_navbar)
    
    # Vista inicial (Home)
    contenedor_vista.content = HomeView(page, cambiar_a_vista)
    
    # Agregar el contenedor a la página
    page.add(contenedor_vista)

# --- UTILIDAD PARA OBTENER IP LOCAL ---
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == "__main__":
    ip_local = get_local_ip()
    puerto = 8550
    
    print("=" * 50)
    print("🚀 SERVIDOR FLET INICIADO")
    print("=" * 50)
    print(f"🌍 Acceso Local:      http://localhost:{puerto}")
    print(f"📡 Acceso en Red:     http://{ip_local}:{puerto}")
    print("=" * 50)
    print("Presiona Ctrl+C para detener el servidor.")

    # Ejecución en modo Navegador Web
    ft.app(
        target=main, 
        view=ft.WEB_BROWSER, # Abre en tu navegador predeterminado
        port=puerto,         # Puerto fijo
        host="0.0.0.0"       # Permite conexiones externas
    )

    # Si prefieres modo escritorio, comenta la línea de arriba y usa esta:
    # ft.app(target=main)