import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials, firestore

# Clave privada
cred = credentials.Certificate('D:\Val\privatekey_school.json')
firebase_admin.initialize_app(cred)

def obtener_datos():
    db = firestore.client()
    coleccion_alumnos = db.collection("alumnos")
    documentos = coleccion_alumnos.stream()

    datos_alumnos = []
    for documento in documentos:
        datos = documento.to_dict()
        datos_alumnos.append((documento.id, datos['correo'], datos['edad'], datos['nombre'], datos['telefono']))

    return datos_alumnos

def mostrar_contenido():
    datos_alumnos = obtener_datos()

    for row in tree.get_children():
        tree.delete(row)

    for dato in datos_alumnos:
        tree.insert("", "end", values=dato)

def eliminar_seleccion():
    seleccion = tree.selection()

    if seleccion:
        id_seleccionado = tree.item(seleccion, "values")[0]
        db = firestore.client()
        coleccion_alumnos = db.collection("alumnos")
        coleccion_alumnos.document(id_seleccionado).delete()

def agregar_alumno():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Alumno")

    correo_var = tk.StringVar()
    edad_var = tk.StringVar()
    nombre_var = tk.StringVar()
    telefono_var = tk.StringVar()

    etiqueta_correo = tk.Label(ventana_agregar, text="Correo:")
    entrada_correo = tk.Entry(ventana_agregar, textvariable=correo_var)

    etiqueta_edad = tk.Label(ventana_agregar, text="Edad:")
    entrada_edad = tk.Entry(ventana_agregar, textvariable=edad_var)

    etiqueta_nombre = tk.Label(ventana_agregar, text="Nombre:")
    entrada_nombre = tk.Entry(ventana_agregar, textvariable=nombre_var)

    etiqueta_telefono = tk.Label(ventana_agregar, text="Teléfono:")
    entrada_telefono = tk.Entry(ventana_agregar, textvariable=telefono_var)

    def agregar_a_alumnos():
        correo = correo_var.get()
        edad = edad_var.get()
        nombre = nombre_var.get()
        telefono = telefono_var.get()

        if nombre and telefono:
            db = firestore.client()
            coleccion_alumnos = db.collection("alumnos")

            nuevo_alumno = {
                "correo": correo,
                "edad": edad,
                "nombre": nombre,
                "telefono": telefono
            }

            coleccion_alumnos.add(nuevo_alumno)

            ventana_agregar.destroy()
            mostrar_contenido()

    boton_agregar = tk.Button(ventana_agregar, text="Agregar alumno", command=agregar_a_alumnos)

    etiqueta_correo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entrada_correo.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    etiqueta_edad.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entrada_edad.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    etiqueta_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entrada_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    etiqueta_telefono.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entrada_telefono.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    boton_agregar.grid(row=4, column=0, columnspan=2, pady=10)
    mostrar_contenido()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conexion Firebase")

# Crear la Treeview
tree = ttk.Treeview(ventana, columns=("ID", "correo", "edad", "nombre", "telefono"), show="headings")
tree.heading("ID", text="ID")
tree.heading("correo", text="Correo")
tree.heading("edad", text="Edad")
tree.heading("nombre", text="Nombre")
tree.heading("telefono", text="Teléfono")
tree.pack(expand=True, fill="both")

# Crear los botones
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_contenido)
boton_mostrar.pack(side=tk.LEFT, padx=5)

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_seleccion)
boton_eliminar.pack(side=tk.LEFT, padx=5)

boton_agregar = tk.Button(ventana, text="Agregar documento", command=agregar_alumno)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Iniciar el bucle de eventos
ventana.mainloop()
