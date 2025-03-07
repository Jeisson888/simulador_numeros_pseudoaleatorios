import sys
import os
# Configuración inicial
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from modelo.generar import *
from modelo.probar import *


# Funciones

def ejecutar_prueba():
    metodo_generacion = metodo_generacion_var.get()
    metodo_prueba = metodo_prueba_var.get()
    try:
        iteraciones = int(n_entry.get())
        semilla = int(semilla_entry.get())
    except ValueError:
        resultado_label.config(text="Error: Los valores deben ser numéricos.")
        return

    numeros = []

    try:
        if metodo_generacion == "Congruencial Lineal Multiplicativo":
            multiplicador = int(a_entry.get())
            modulo = int(m_entry.get())
            numeros = congruencial_lineal_multiplicativo(iteraciones, multiplicador, semilla, modulo)
        elif metodo_generacion == "Congruencial Lineal":
            multiplicador = int(a_entry.get())
            corrimiento = int(c_entry.get())
            modulo = int(m_entry.get())
            numeros = congruencial_lineal(iteraciones, multiplicador, semilla, corrimiento, modulo)
        elif metodo_generacion == "Cuadrados Medios":
            numeros = cuadrados_medios(iteraciones, semilla)
        elif metodo_generacion =="Congruencial permutado":
            numeros = pcg(iteraciones, multiplicador, corrimiento, semilla, modulo)
        else:
            resultado_label.config(text="Seleccione un método de generación válido.")
            return

        if not numeros:
            resultado_label.config(text="No se generaron números.")
            return

        if metodo_prueba == "KS":
            resultado = kolmogorov_smirnov(numeros, numeros)
        elif metodo_prueba == "Chi-cuadrado":
            resultado = chi_cuadrada(numeros, 0, 1)
        elif metodo_prueba == "Medias":
            resultado = prueba_medias(numeros)
        elif metodo_prueba == "Varianza":
            resultado = "Prueba de Varianza no implementada"
        else:
            resultado = "Seleccione una prueba válida."

        resultado_label.config(text=resultado)
    except Exception as e:
        resultado_label.config(text=f"Error: {str(e)}")


def mostrar_parametros():
    metodo_generacion = metodo_generacion_var.get()
    ocultar_parametros()

    if metodo_generacion in ["Congruencial Lineal Multiplicativo", "Congruencial Lineal", "Congruencial permutado"]:
        a_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        a_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        m_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        m_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        if metodo_generacion in ["Congruencial Lineal", "Congruencial permutado"]:
            c_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
            c_entry.grid(row=4, column=1, sticky="ew", padx=5, pady=5)


def ocultar_parametros():
    for widget in [a_label, a_entry, c_label, c_entry, m_label, m_entry]:
        widget.grid_forget()


# Interfaz Gráfica
ventana = tk.Tk()
ventana.title("Pruebas de Números Aleatorios")
ventana.geometry("400x450")

frame_generacion = ttk.LabelFrame(ventana, text="Generación de Números")
frame_generacion.pack(padx=10, pady=10, fill="x")

metodo_generacion_var = tk.StringVar()
metodo_generacion_combobox = ttk.Combobox(frame_generacion, textvariable=metodo_generacion_var, values=["Congruencial Lineal Multiplicativo", "Congruencial Lineal", "Cuadrados Medios","Congruencial permutado"])
metodo_generacion_combobox.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
metodo_generacion_combobox.bind("<<ComboboxSelected>>", lambda event: mostrar_parametros())

semilla_label = tk.Label(frame_generacion, text="Semilla:")
semilla_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
semilla_entry = tk.Entry(frame_generacion)
semilla_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

a_label = tk.Label(frame_generacion, text="Multiplicador:")
a_entry = tk.Entry(frame_generacion)
c_label = tk.Label(frame_generacion, text="Corrimiento:")
c_entry = tk.Entry(frame_generacion)
m_label = tk.Label(frame_generacion, text="Módulo:")
m_entry = tk.Entry(frame_generacion)

n_label = tk.Label(frame_generacion, text="Cantidad (n):")
n_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
n_entry = tk.Entry(frame_generacion)
n_entry.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

frame_pruebas = ttk.LabelFrame(ventana, text="Pruebas Estadísticas")
frame_pruebas.pack(padx=10, pady=10, fill="x")

metodo_prueba_var = tk.StringVar()
metodo_prueba_combobox = ttk.Combobox(frame_pruebas, textvariable=metodo_prueba_var, values=["KS", "Chi-cuadrado", "Medias", "Varianza"])
metodo_prueba_combobox.pack()

ejecutar_button = tk.Button(ventana, text="Ejecutar Prueba", command=ejecutar_prueba)
ejecutar_button.pack(pady=10)

resultado_label = tk.Label(ventana, text="", wraplength=380)
resultado_label.pack()

ventana.mainloop()
