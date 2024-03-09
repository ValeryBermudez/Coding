import tkinter as tk
from tkinter import ttk
import mysql.connector

def mostrar_contenido():
    # Establecer la conexión
    conexion = mysql.connector.connect(
        host="localhost",
        port=33065,
        user="localhostt",
        password="Localhost0",
        database="escuela"
    )

    # Crear un objeto cursor para interactuar con la base de datos
    cursor = conexion.cursor()

    # Ejecutar una consulta
    consulta = "SELECT * FROM alumnos"
    cursor.execute(consulta)

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Limpiar la tabla antes de agregar nuevos datos
    for row in tree.get_children():
        tree.delete(row)

    # Imprimir los resultados en la interfaz
    for resultado in resultados:
        tree.insert("", "end", values=resultado)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

def eliminar_seleccion():
    seleccion = tree.selection()

    if seleccion:
        id_seleccionado = tree.item(seleccion, "values")[0]

        # Establecer la conexión
        conexion = mysql.connector.connect(
            host="localhost",
            port=33065,
            user="localhostt",
            password="Localhost0",
            database="escuela"
        )

        # Crear un objeto cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Ejecutar la consulta de eliminación
        consulta = f"DELETE FROM alumnos WHERE id={id_seleccionado}"
        cursor.execute(consulta)

        # Confirmar la transacción
        conexion.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        # Actualizar la tabla en la interfaz después de la eliminación
        mostrar_contenido()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conexion DB")

# Crear la Treeview
tree = ttk.Treeview(ventana)
tree["columns"] = ("ID", "Nombre", "Teléfono")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.pack(expand=True, fill="both")

# Crear el botón para mostrar contenido
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_contenido)
boton_mostrar.pack()

# Crear el botón para eliminar
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_seleccion)
boton_eliminar.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
