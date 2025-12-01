import tkinter as tk
from tkinter import ttk, messagebox

class TablaApp:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Manejo de Tabla")
        self.ventana.configure(background='#1d2d44')
        self.ventana.geometry("700x450")

        self.configurar_estilos()
        self.crear_frame_tabla()
        self.crear_tabla()
        self.cargar_datos()
        
        self.ventana.mainloop()

    # Estilos
    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
            background="#0d1b2a",
            foreground="white",
            rowheight=28,
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

        style.map("Treeview.Heading",
            background=[("active", "#778da9")]
        )

    # Frame contenedor
    def crear_frame_tabla(self):
        self.frame_tabla = tk.Frame(self.ventana, bg="#1d2d44")
        self.frame_tabla.pack(padx=15, pady=15, fill="both", expand=False)

        # Scrollbars
        self.scroll_y = ttk.Scrollbar(self.frame_tabla, orient="vertical")
        self.scroll_x = ttk.Scrollbar(self.frame_tabla, orient="horizontal")

    # Crear Treeview
    def crear_tabla(self):
        columnas = ('id', 'nombre', 'edad')

        self.tabla = ttk.Treeview(
            self.frame_tabla,
            columns=columnas,
            show='headings',
            yscrollcommand=self.scroll_y.set,
            xscrollcommand=self.scroll_x.set
        )

        self.scroll_y.config(command=self.tabla.yview)
        self.scroll_x.config(command=self.tabla.xview)

        # Encabezados
        self.tabla.heading('id', text='ID', anchor=tk.CENTER)
        self.tabla.heading('nombre', text='Nombre', anchor=tk.CENTER)
        self.tabla.heading('edad', text='Edad', anchor=tk.CENTER)

        # Columnas
        self.tabla.column('id', width=80, anchor=tk.CENTER)
        self.tabla.column('nombre', width=150, anchor=tk.CENTER)
        self.tabla.column('edad', width=120, anchor=tk.CENTER)

        # Filas alternadas
        self.tabla.tag_configure("oddrow", background="#1b263b")
        self.tabla.tag_configure("evenrow", background="#162033")

        # Ubicar tabla y scrollbars dentro del frame
        self.tabla.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        self.frame_tabla.grid_columnconfigure(0, weight=1)
        self.frame_tabla.grid_rowconfigure(0, weight=1)

        # Evento click
        self.tabla.bind("<ButtonRelease-1>", self.mostrar_info)

    # Cargar información
    def cargar_datos(self):
        datos = [
            (1, 'Alejandra', 25),
            (2, 'Matias', 32),
            (3, 'Sofia', 29),
            (4, 'Carlos', 41),
            (5, 'Lucia', 22),
            (6, 'Ramiro', 35),
            (7, 'Valentina', 27),
            (8, 'Jorge', 52),
            (9, 'Marina', 30),
            (10, 'Tomas', 19),
            (11, 'Bianca', 33),
            (12, 'Fernando', 44),
        ]

        for i, persona in enumerate(datos):
            tag = "oddrow" if i % 2 == 0 else "evenrow"
            self.tabla.insert('', tk.END, values=persona, tags=(tag,))

    # Evento al hacer clic en una fila
    def mostrar_info(self, event):
        seleccion = self.tabla.focus()
        if seleccion:
            datos = self.tabla.item(seleccion, "values")
            messagebox.showinfo(
                "Información de la fila",
                f"ID: {datos[0]}\nNombre: {datos[1]}\nEdad: {datos[2]}"
            )


# Ejecutar app
if __name__ == "__main__":
    TablaApp()
