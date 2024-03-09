import tkinter as tk
from tkinter import ttk
import requests

def convertir():
    ##Si quieres cambiar el tipo de moneda, debes cambiar el valor en la linea 6 en la variable (currency_original) y luego en la linea 7 el valor de la variable (currency_a_convertir)
    currency_original = currency_primero.get()
    currency_a_convertir = opcion_a_convertir.get()
    ingresarNumero = float(entry_cantidad.get())


    response = requests.get(f'https://v6.exchangerate-api.com/v6/3f816dcf58fd3bd50a090907/latest/{currency_original}')
    ##print(response.status_code)
    ##print(response.json())

    ## extrae un diccionario [conversion_rates] de response.json que es un diccionario de todos los datos y lo guarda en la variable conversion_rates
    conversion_rates = response.json()['conversion_rates'][currency_a_convertir]
    print(conversion_rates)
    resultado = ingresarNumero * float(conversion_rates)
    lbl_resultado.config(text="Resultado: {:.2f}".format(resultado[0] if isinstance(resultado, tuple) else resultado))
    
ventana = tk.Tk()
ventana.title("Convertidor de Moneda")

ventana.maxsize(width=450, height=400)
marco = ttk.Frame(ventana, padding=10)
marco.grid(padx=0, pady=0, sticky="nsew")

lbl_titulo = ttk.Label(marco, text="Converter currency", font=("Times New Roman", 16)).grid(padx=130, pady=0, row=0, sticky=tk.W)

lbl_operacion = ttk.Label(marco, text="Selecciona una operación:", font=("Times New Roman", 12)).grid(padx=135, pady=0, row=1, sticky=tk.W)

currency_primero = tk.StringVar()
radio_peso = ttk.Radiobutton(marco, text="COP", variable=currency_primero, value="COP").grid(column=0, row=2, sticky=tk.W)
radio_dolar = ttk.Radiobutton(marco, text="USD", variable=currency_primero, value="USD").grid(column=0, row=3, sticky=tk.W)
btn_convertir = ttk.Button(marco, text="Convertir", command=convertir).grid(padx=150, pady=0, sticky=tk.W)
radio_libras = ttk.Radiobutton(marco, text="GBP", variable=currency_primero, value="GBP").grid(column=0, row=4, sticky=tk.W)
radio_soles= ttk.Radiobutton(marco, text="PEN", variable=currency_primero, value="PEN").grid(column=0, row=5, sticky=tk.W)
radio_reales = ttk.Radiobutton(marco, text="BRL", variable=currency_primero, value="BRL").grid(column=0, row=6, sticky=tk.W)

opcion_a_convertir = tk.StringVar()
radio_peso = ttk.Radiobutton(marco, text="COP", variable=opcion_a_convertir, value="COP").grid(padx=270, pady=0, row=2, sticky=tk.W)
radio_dolar = ttk.Radiobutton(marco, text="USD", variable=opcion_a_convertir, value="USD").grid(padx=270, pady=0, row=3, sticky=tk.W)
radio_libras = ttk.Radiobutton(marco, text="GBP", variable=opcion_a_convertir, value="GBP").grid(padx=270, pady=0, row=4, sticky=tk.W)
radio_soles= ttk.Radiobutton(marco, text="PEN", variable=opcion_a_convertir, value="PEN").grid(padx=270, pady=0, row=5, sticky=tk.W)
radio_reales = ttk.Radiobutton(marco, text="BRL", variable=opcion_a_convertir, value="BRL").grid(padx=270, pady=0, row=6, sticky=tk.W)

entry_cantidad = ttk.Entry(marco)
entry_cantidad.grid(column=0, row=7, sticky=tk.W)

lbl_resultado = ttk.Label(marco, text="Resultado:")
lbl_resultado.grid(padx=270, pady=0, row=7, sticky=tk.W)

lbl_brand = ttk.Label(marco, text="By Valery Bermudez").grid(padx=0, pady=7, row=8, sticky=tk.W)

ventana.mainloop()
