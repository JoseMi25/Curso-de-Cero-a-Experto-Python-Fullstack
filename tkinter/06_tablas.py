import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mostrar_info(event):
    seleccion = tabla.focus()
    if seleccion:
        datos = tabla.item(seleccion, 'values')
        messagebox.showinfo(
            "Información de la fila",
            f"ID: {datos[0]}\nNombre: {datos[1]}\nEdad: {datos[2]}"
        )

# Ventana
ventana = tk.Tk()
ventana.title("Manejo de Tabla")
ventana.configure(background='#1d2d44')
ventana.geometry("700x450")

#Estilos
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

# Frame para tabla (NO se expande toda la ventana)
frame_tabla = tk.Frame(ventana, bg="#1d2d44")
frame_tabla.pack(padx=15, pady=15, fill="both", expand=False)

#Scrollbar
scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
scroll_x = ttk.Scrollbar(frame_tabla, orient="horizontal")

# Tabla
columnas = ('id', 'nombre', 'edad')
tabla = ttk.Treeview(
    frame_tabla, 
    columns=columnas,
    show='headings',
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

scroll_y.config(command=tabla.yview)
scroll_x.config(command=tabla.xview)

# Encabezados
tabla.heading('id', text='ID', anchor=tk.CENTER)
tabla.heading('nombre', text='Nombre', anchor=tk.CENTER)
tabla.heading('edad', text='Edad', anchor=tk.CENTER)

tabla.column('id', width=80, anchor=tk.CENTER)
tabla.column('nombre', width=150, anchor=tk.CENTER)
tabla.column('edad', width=120, anchor=tk.CENTER)

# Filas alternadas
tabla.tag_configure("oddrow", background="#1b263b")
tabla.tag_configure("evenrow", background="#162033")

# Datos
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
    tabla.insert('', tk.END, values=persona, tags=(tag,))

# Ubicación de tabla + scroll solo dentro del frame
tabla.grid(row=0, column=0, sticky="nsew")
scroll_y.grid(row=0, column=1, sticky="ns")
scroll_x.grid(row=1, column=0, sticky="ew")

frame_tabla.grid_columnconfigure(0, weight=1)
frame_tabla.grid_rowconfigure(0, weight=1)

# Evento click
tabla.bind("<ButtonRelease-1>", mostrar_info)

ventana.mainloop()
