import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('D:\Val\privatekey.json')
firebase_admin.initialize_app(cred)

def get_data():
    db = firestore.client()
    coleccion_almacen = db.collection("almacen")
    documentos = coleccion_almacen.stream()

    data_store = []
    for documento in documentos:
        datos = documento.to_dict()
        data_store.append((documento.id, datos['address'], datos['date'], datos['email'], datos['id_customer'], datos['name'], datos['phone']))

    return data_store

def show_content():
    data_store = get_data()

    for row in tree.get_children():
        tree.delete(row)

    for dato in data_store:
        tree.insert("", "end", values=dato)

def delete_selection():
    seleccion = tree.selection()

    if seleccion:
        id_seleccionado = tree.item(seleccion, "values")[0]
        db = firestore.client()
        coleccion_almacen = db.collection("almacen")
        coleccion_almacen.document(id_seleccionado).delete()

def add_customer():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Add customer")

    address_var = tk.StringVar()
    date_var = tk.StringVar()
    email_var = tk.StringVar()
    id_customer_var = tk.IntVar()
    name_var = tk.StringVar()
    phone_var = tk.IntVar()

    etiqueta_date= tk.Label(ventana_agregar, text="Date:")
    entrada_date = tk.Entry(ventana_agregar, textvariable=date_var)
    
    etiqueta_address = tk.Label(ventana_agregar, text="Address:")
    entrada_address = tk.Entry(ventana_agregar, textvariable=address_var)

    etiqueta_email = tk.Label(ventana_agregar, text="Email:")
    entrada_email = tk.Entry(ventana_agregar, textvariable=email_var)

    etiqueta_id_customer = tk.Label(ventana_agregar, text="ID_customer:")
    entrada_id_customer = tk.Entry(ventana_agregar, textvariable=id_customer_var)

    etiqueta_name = tk.Label(ventana_agregar, text="Name:")
    entrada_name = tk.Entry(ventana_agregar, textvariable=name_var)

    etiqueta_phone = tk.Label(ventana_agregar, text="Phone: ")
    entrada_phone = tk.Entry(ventana_agregar, textvariable=phone_var)

    def add_a_customer():

        address = address_var.get()
        date = date_var.get()
        email = email_var.get()
        id_customer = id_customer_var.get()
        name = name_var.get()
        phone = phone_var.get()

        if name and phone:
            db = firestore.client()
            coleccion_almacen = db.collection("almacen")

            new_customer = {
                "address": address,
                "date": date,
                "email": email,
                "ID_customer": id_customer,
                "name": name,
                "phone": phone
            }

            coleccion_almacen.add(new_customer)

            ventana_agregar.destroy()
            show_content()

    button_add = tk.Button(ventana_agregar, text="Add customer", command=add_a_customer)

    etiqueta_address.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entrada_address.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    etiqueta_date.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entrada_date.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    etiqueta_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entrada_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    etiqueta_id_customer.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entrada_id_customer.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    etiqueta_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entrada_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    etiqueta_phone.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entrada_phone.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    button_add.grid(row=4, column=0, columnspan=2, pady=10)
    show_content()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conexion Firebase")

# Crear la Treeview
tree = ttk.Treeview(ventana, columns=("address", "date", "email", "ID_customer", "name", "phone"), show="headings")
tree.heading("address", text="address")
tree.heading("date", text="date")
tree.heading("email", text="email")
tree.heading("ID_customer", text="ID_customer")
tree.heading("name", text="name")
tree.heading("phone", text="phone")
tree.pack(expand=True, fill="both")

# Crear los botones
button_show = tk.Button(ventana, text="Mostrar", command=show_content)
button_show.pack(side=tk.LEFT, padx=5)

button_delete = tk.Button(ventana, text="Eliminar", command=delete_selection)
button_delete.pack(side=tk.LEFT, padx=5)

button_add = tk.Button(ventana, text="Agregar documento", command=add_customer)
button_add.pack(side=tk.LEFT, padx=5)

# Iniciar el bucle de eventos
ventana.mainloop()