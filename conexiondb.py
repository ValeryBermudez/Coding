import tkinter as tk
from tkinter import ttk
import mysql.connector

class conexiondb():
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

    # Obtener los resultado
    resultados = cursor.fetchall()

    # Imprimir los resultados
    print(resultados)
    for resultado in resultados:
        print(resultado)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de Alumnos")
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Teléfono"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Teléfono", text="Teléfono")

        data = [
            (102489632, "Isabella", 324589634),
            (102643512, "Maria", 312654789),
            (102897454, "Juan", 315478951),
            (103645896, "Pedro", 314256978),
            (103654216, "Laura", 316547893)
        ]

        for row in data:
            self.tree.insert("", "end", values=row)

        for col in ("ID", "Nombre", "Teléfono"):
            self.tree.column(col, anchor="center", width=100)

        self.tree.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = conexiondb(root)
    root.mainloop()