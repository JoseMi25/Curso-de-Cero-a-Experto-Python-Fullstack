import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Ajustar ruta para importar desde la carpeta "APP ZONA FIT" (mismo nivel que esta carpeta)
# Si la carpeta tiene otro nombre o está en otra ubicación, ajusta app_zona_fit_path.
this_dir = os.path.dirname(os.path.abspath(__file__))
app_zona_fit_path = os.path.abspath(os.path.join(this_dir, "..", "APP ZONA FIT"))
if app_zona_fit_path not in sys.path:
    sys.path.insert(0, app_zona_fit_path)

# Intentar importar los módulos DAO/Modelo
try:
    from cliente_dao import ClienteDAO
    from cliente import Cliente
except Exception as e:
    message = (
        "No se pudo importar ClienteDAO/Cliente desde 'APP ZONA FIT'.\n"
        "Asegúrate que la carpeta 'APP ZONA FIT' existe al mismo nivel que la carpeta 'tkinter'\n"
        f"Error: {e}"
    )
    # Si estamos en un entorno sin GUI esto lanzará excepcion; igualmente mostramos un print
    print(message)
    # Se continúa para evitar crash al importar en entornos de pruebas, pero la app mostrará error al usar DB.
    ClienteDAO = None
    Cliente = None


class ZonaFitApp:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Zona Fit (GUI)")
        self.ventana.geometry("900x600")
        self.ventana.configure(bg="#1d2d44")

        # ID seleccionado para actualizar
        self.id_seleccionado = None

        self.crear_estilos()
        self.crear_layout()
        self.crear_formulario()
        self.crear_tabla()
        self.crear_botones()
        self.cargar_datos()

        self.ventana.mainloop()

    # ESTILOS
    def crear_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Estilo tabla
        style.configure("Treeview",
            background="#0d1b2a",
            foreground="white",
            rowheight=24,  # MÁS PEQUEÑA
            fieldbackground="#0d1b2a",
            bordercolor="#415a77",
            borderwidth=1
        )
        style.map("Treeview",
            background=[("selected", "#3a86ff")],
            foreground=[("selected", "black")]
        )

        style.configure("Treeview.Heading",
            background="#415a77",
            foreground="white",
            font=("Arial", 11, "bold"),
            padding=6
        )

        # Botones estilo personalizado
        self.btn_style = {
            "bg": "#415a77",
            "fg": "white",
            "activebackground": "#778da9",
            "activeforeground": "white",
            "font": ("Arial", 12, "bold"),
            "relief": "raised",
            "bd": 3,
            "width": 12,
            "height": 1
        }

    # -------------------------------
    # LAYOUT
    # -------------------------------
    def crear_layout(self):
        # Configurar columnas
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)

        # Título
        tk.Label(
            self.ventana,
            text="Zona Fit (GYM)",
            font=("Arial", 24, "bold"),
            bg="#1d2d44",
            fg="white"
        ).grid(row=0, column=0, columnspan=2, pady=(15, 25))

        # Formularios (izquierda)
        self.frame_form = tk.Frame(self.ventana, bg="#1d2d44")
        self.frame_form.grid(row=1, column=0, sticky="n", padx=25)

        # Tabla (derecha)
        self.frame_tabla = tk.Frame(self.ventana, bg="#1d2d44")
        self.frame_tabla.grid(row=1, column=1, sticky="n", padx=25)

        # Botones inferiores
        self.frame_botones = tk.Frame(self.ventana, bg="#1d2d44")
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=25)

    # -------------------------------
    # FORMULARIO
    # -------------------------------
    def crear_formulario(self):
        label_style = {"bg": "#1d2d44", "fg": "white", "font": ("Arial", 14, "bold")}

        tk.Label(self.frame_form, text="Nombre:", **label_style).grid(row=0, column=0, pady=10, sticky="w")
        tk.Label(self.frame_form, text="Apellido:", **label_style).grid(row=1, column=0, pady=10, sticky="w")
        tk.Label(self.frame_form, text="Membresía:", **label_style).grid(row=2, column=0, pady=10, sticky="w")

        self.var_nombre = tk.StringVar()
        self.var_apellido = tk.StringVar()
        self.var_membresia = tk.StringVar()

        entry_style = {"width": 23, "font": ("Arial", 12)}

        tk.Entry(self.frame_form, textvariable=self.var_nombre, **entry_style).grid(row=0, column=1, pady=10)
        tk.Entry(self.frame_form, textvariable=self.var_apellido, **entry_style).grid(row=1, column=1, pady=10)
        tk.Entry(self.frame_form, textvariable=self.var_membresia, **entry_style).grid(row=2, column=1, pady=10)

    # -------------------------------
    # TABLA
    # -------------------------------
    def crear_tabla(self):
        columnas = ("id", "nombre", "apellido", "membresia")

        # Scrollbar solo vertical
        scroll_y = ttk.Scrollbar(self.frame_tabla, orient="vertical")

        # Crear tabla SIN scrollbar horizontal
        self.tabla = ttk.Treeview(
            self.frame_tabla,
            columns=columnas,
            show="headings",
            yscrollcommand=scroll_y.set,
            height=12     # suficiente para mostrar varias filas
        )

        scroll_y.config(command=self.tabla.yview)

        # Encabezados
        self.tabla.heading("id", text="ID", anchor=tk.CENTER)
        self.tabla.heading("nombre", text="Nombre", anchor=tk.CENTER)
        self.tabla.heading("apellido", text="Apellido", anchor=tk.CENTER)
        self.tabla.heading("membresia", text="Membresía", anchor=tk.CENTER)

        # Ajuste PERFECTO de columnas para que NO requiera scrollbar X
        self.tabla.column("id", width=60, anchor=tk.CENTER)
        self.tabla.column("nombre", width=120, anchor=tk.W)
        self.tabla.column("apellido", width=120, anchor=tk.W)
        self.tabla.column("membresia", width=120, anchor=tk.CENTER)

        # Filas alternadas (decoración)
        self.tabla.tag_configure("oddrow", background="#1b263b")
        self.tabla.tag_configure("evenrow", background="#162033")

        # Posicionar en grid
        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")

        # Permitir que la tabla expanda en su frame
        self.frame_tabla.grid_rowconfigure(0, weight=1)
        self.frame_tabla.grid_columnconfigure(0, weight=1)

        # Evento de selección
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_fila)

    # -------------------------------
    # BOTONES
    # -------------------------------
    def crear_botones(self):
        tk.Button(self.frame_botones, text="Guardar", command=self.guardar, **self.btn_style).grid(row=0, column=0, padx=20)
        tk.Button(self.frame_botones, text="Eliminar", command=self.eliminar, **self.btn_style).grid(row=0, column=1, padx=20)
        tk.Button(self.frame_botones, text="Limpiar", command=self.limpiar, **self.btn_style).grid(row=0, column=2, padx=20)


    # -------------------------------
    # CRUD
    # -------------------------------
    def cargar_datos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        clientes = ClienteDAO.seleccionar()

        for cli in clientes:
            self.tabla.insert("", tk.END, values=(cli.id, cli.nombre, cli.apellido, cli.membresia))

    def guardar(self):
        nombre = self.var_nombre.get().strip()
        apellido = self.var_apellido.get().strip()
        membresia = self.var_membresia.get().strip()

        if not nombre or not apellido or not membresia:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not membresia.isdigit():
            messagebox.showerror("Error", "La membresía debe ser numérica")
            return

        # ---------------------------------
        # SI NO HAY ID → AGREGAR CLIENTE
        # ---------------------------------
        if not self.id_seleccionado:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)

            messagebox.showinfo("Cliente Agregado!", "El cliente se registró correctamente.")

        # ---------------------------------
        # SI HAY ID → ACTUALIZAR CLIENTE
        # ---------------------------------
        else:
            cliente = Cliente(id=self.id_seleccionado, nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.actualizar(cliente)

            messagebox.showinfo("Cliente Actualizado!", "Se actualizaron los datos correctamente.")

        self.cargar_datos()
        self.limpiar()


    def seleccionar_fila(self, event):
        seleccionado = self.tabla.focus()
        if seleccionado:
            datos = self.tabla.item(seleccionado, "values")

            self.id_seleccionado = datos[0]
            self.var_nombre.set(datos[1])
            self.var_apellido.set(datos[2])
            self.var_membresia.set(datos[3])


    def actualizar(self):
        if not self.id_seleccionado:
            messagebox.showerror("Error", "Seleccione un cliente en la tabla.")
            return

        nombre = self.var_nombre.get().strip()
        apellido = self.var_apellido.get().strip()
        membresia = self.var_membresia.get().strip()

        if not nombre or not apellido or not membresia:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not membresia.isdigit():
            messagebox.showerror("Error", "La membresía debe ser numérica")
            return

        cliente = Cliente(id=self.id_seleccionado, nombre=nombre, apellido=apellido, membresia=membresia)
        ClienteDAO.actualizar(cliente)

        messagebox.showinfo("Éxito", "Cliente actualizado")

        self.cargar_datos()
        self.limpiar()

    def eliminar(self):
        seleccionado = self.tabla.focus()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un cliente de la tabla")
            return

        id_cliente = self.tabla.item(seleccionado, "values")[0]
        ClienteDAO.eliminar(Cliente(id=id_cliente))

        messagebox.showinfo("Éxito", "Cliente eliminado")
        self.cargar_datos()
        self.limpiar()

    def limpiar(self):
        self.var_nombre.set("")
        self.var_apellido.set("")
        self.var_membresia.set("")
        self.id_seleccionado = None
        self.tabla.selection_remove(self.tabla.selection())

# -------------------------------
# INICIAR APP
# -------------------------------
if __name__ == "__main__":
    ZonaFitApp()
