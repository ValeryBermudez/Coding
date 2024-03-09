import tkinter as tk
from tkinter import ttk

class Currency:
    def __init__(self):
        self.peso = 1
        self.dolar = 1
        self.libras = 1
        self.soles = 1
        self.reales = 1
 #Peso
    def peso_to_dolar(self, peso):
        return peso * 0.00025
    def peso_to_libras(self, peso):
        return peso * 0.00020
    def peso_to_soles(self, peso):
        return peso * 0.00097
    def peso_to_reales(self, peso):
        return peso * 0.00013
#Dolar
    def dolar_to_peso(self, dolar):
        return dolar * 3952.07
    def dolar_to_libras(self, dolar):
        return dolar * 0.79
    def dolar_to_soles(self, dolar):
        return dolar * 3.81
    def dolar_to_reales(self, dolar):
        return dolar * 4.95
#Libras
    def libras_to_peso(self, libras):
        return libras * 4978.48
    def libras_to_dolar(self, libras):
        return libras * 1.26
    def libras_to_soles(self, libras):
        return libras * 4.81
    def libras_to_reales(self, libras):
        return libras * 6.25
#Soles
    def soles_to_peso(self, soles):
        return soles * 1023.75
    def soles_to_dolar(self, soles):
        return soles * 0.26
    def soles_to_libras(self, soles):
        return soles * 0.21
    def soles_to_reales(self, soles):
        return soles * 1.30
#Reales
    def reales_to_peso(self, reales):
        return reales * 166.55
    def reales_to_dolar(self, reales):
        return reales * 0.20
    def reales_to_libras(self, reales):
        return reales * 0.16
    def reales_to_soles(self, reales):
        return reales * 0.77
    
currency = Currency()

def convertir():
    try:
        cantidad = float(entry_cantidad.get())
        operacion = opcion_operacion.get()
        opcion_convertir = opcion_a_convertir.get()
        if operacion == 1:
            resultado = 0
        if operacion == opcion_convertir:
            resultado = cantidad
        elif operacion == 1:
            if opcion_convertir == 2:
                resultado = currency.peso_to_dolar(cantidad)
            elif opcion_convertir == 3:
                resultado = currency.peso_to_libras(cantidad)
            elif opcion_convertir == 4:
                resultado = currency.peso_to_soles(cantidad)
            elif opcion_convertir == 5:
                resultado = currency.peso_to_reales(cantidad)
        elif operacion == 2:
            if opcion_convertir == 1:
                resultado = currency.dolar_to_peso(cantidad)
            elif opcion_convertir == 3:
                resultado = currency.dolar_to_libras(cantidad)
            elif opcion_convertir == 4:
                resultado = currency.dolar_to_soles(cantidad)
            elif opcion_convertir == 5:
                resultado = currency.dolar_to_reales(cantidad)
        elif operacion == 3:
            if opcion_convertir == 1:
                resultado = currency.libras_to_peso(cantidad)
            elif opcion_convertir == 2:
                resultado = currency.libras_to_dolar(cantidad)
            elif opcion_convertir == 4:
                resultado = currency.libras_to_soles(cantidad)
            elif opcion_convertir == 5:
                resultado = currency.libras_to_reales(cantidad)
        elif operacion == 4:
            if opcion_convertir == 1:
                resultado = currency.soles_to_peso(cantidad)
            elif opcion_convertir == 2:
                resultado = currency.soles_to_dolar(cantidad)
            elif opcion_convertir == 3:
                resultado = currency.soles_to_libras(cantidad)
            elif opcion_convertir == 5:
                resultado = currency.soles_to_reales(cantidad)
        elif operacion == 5:
            if opcion_convertir == 1:
                resultado = currency.reales_to_peso(cantidad)
            elif opcion_convertir == 2:
                resultado = currency.reales_to_dolar(cantidad)
            elif opcion_convertir == 3:
                resultado = currency.reales_to_libras(cantidad)
            elif opcion_convertir == 4:
                resultado = currency.reales_to_soles(cantidad)

        lbl_resultado.config(text="Resultado: {:.2f}".format(resultado[0] if isinstance(resultado, tuple) else resultado))
    except ValueError:
        lbl_resultado.config(text="Error: Ingresa un número válido")
ventana = tk.Tk()
ventana.title("Convertidor de Moneda")

ventana.maxsize(width=450, height=400)
marco = ttk.Frame(ventana, padding=10)
marco.grid(padx=0, pady=0, sticky="nsew")

lbl_titulo = ttk.Label(marco, text="Converter currency", font=("Times New Roman", 16)).grid(padx=130, pady=0, row=0, sticky=tk.W)

lbl_operacion = ttk.Label(marco, text="Selecciona una operación:", font=("Times New Roman", 12)).grid(padx=135, pady=0, row=1, sticky=tk.W)

opcion_operacion = tk.IntVar()
radio_peso = ttk.Radiobutton(marco, text="Pesos", variable=opcion_operacion, value=1).grid(column=0, row=2, sticky=tk.W)
radio_dolar = ttk.Radiobutton(marco, text="Dolares", variable=opcion_operacion, value=2).grid(column=0, row=3, sticky=tk.W)
btn_convertir = ttk.Button(marco, text="Convertir", command=convertir).grid(padx=150, pady=0, sticky=tk.W)
radio_libras = ttk.Radiobutton(marco, text="Libra esterlina", variable=opcion_operacion, value=3).grid(column=0, row=4, sticky=tk.W)
radio_soles= ttk.Radiobutton(marco, text="Sol peruano", variable=opcion_operacion, value=4).grid(column=0, row=5, sticky=tk.W)
radio_reales = ttk.Radiobutton(marco, text="Real brasileño", variable=opcion_operacion, value=5).grid(column=0, row=6, sticky=tk.W)

opcion_a_convertir = tk.IntVar()
radio_peso = ttk.Radiobutton(marco, text="Pesos", variable=opcion_a_convertir, value=1).grid(padx=270, pady=0, row=2, sticky=tk.W)
radio_dolar = ttk.Radiobutton(marco, text="Dolares", variable=opcion_a_convertir, value=2).grid(padx=270, pady=0, row=3, sticky=tk.W)
radio_libras = ttk.Radiobutton(marco, text="Libra esterlina", variable=opcion_a_convertir, value=3).grid(padx=270, pady=0, row=4, sticky=tk.W)
radio_soles= ttk.Radiobutton(marco, text="Sol peruano", variable=opcion_a_convertir, value=4).grid(padx=270, pady=0, row=5, sticky=tk.W)
radio_reales = ttk.Radiobutton(marco, text="Real brasileño", variable=opcion_a_convertir, value=5).grid(padx=270, pady=0, row=6, sticky=tk.W)

entry_cantidad = ttk.Entry(marco)
entry_cantidad.grid(column=0, row=7, sticky=tk.W)

lbl_resultado = ttk.Label(marco, text="Resultado:")
lbl_resultado.grid(padx=270, pady=0, row=7, sticky=tk.W)

lbl_brand = ttk.Label(marco, text="By Valery Bermudez").grid(padx=0, pady=7, row=8, sticky=tk.W)

ventana.mainloop()