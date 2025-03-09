import sys
import os
import customtkinter as ctk
# Configuración inicial
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.generar import *
from modelo.probar import *



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Funciones
def ejecutar_prueba():
    metodo_generacion = metodo_generacion_var.get()
    metodo_prueba = metodo_prueba_var.get()
    try:
        iteraciones = int(n_entry.get())
        semilla = int(semilla_entry.get())
    except ValueError:
        resultado_label.configure(text="Error: Los valores deben ser numéricos.")
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
        elif metodo_generacion == "Congruencial permutado":
            multiplicador = int(a_entry.get())
            corrimiento = int(c_entry.get())
            modulo = int(m_entry.get())
            numeros = pcg(iteraciones, multiplicador, corrimiento, semilla, modulo)
        else:
            resultado_label.configure(text="Seleccione un método de generación válido.")
            return

        if not numeros:
            resultado_label.configure(text="No se generaron números.")
            return

        if metodo_prueba == "KS":
            resultado = kolmogorov_smirnov(numeros, numeros)
        elif metodo_prueba == "Chi-cuadrado":
            resultado = chi_cuadrada(numeros, 0, 1)
        elif metodo_prueba == "Medias":
            resultado = prueba_medias(numeros)
        elif metodo_prueba == "Varianza":
            resultado = varianzas(numeros)
        else:
            resultado = "Seleccione una prueba válida."

        resultado_label.configure(text=resultado)
    except Exception as e:
        resultado_label.configure(text=f"Error: {str(e)}")


def mostrar_parametros():
    metodo_generacion = metodo_generacion_var.get()
    ocultar_parametros()

    if metodo_generacion in ["Congruencial Lineal Multiplicativo", "Congruencial Lineal", "Congruencial permutado"]:
        a_label.pack()
        a_entry.pack()
        m_label.pack()
        m_entry.pack()
        if metodo_generacion in ["Congruencial Lineal", "Congruencial permutado"]:
            c_label.pack()
            c_entry.pack()


def ocultar_parametros():
    for widget in [a_label, a_entry, c_label, c_entry, m_label, m_entry]:
        widget.pack_forget()

# Interfaz Gráfica
ventana = ctk.CTk()
ventana.title("Pruebas de Números Aleatorios")
ventana.geometry("400x500")

frame_generacion = ctk.CTkFrame(ventana)
frame_generacion.pack(padx=10, pady=10, fill="x")

ctk.CTkLabel(frame_generacion, text="Método de Generación:").pack()
metodo_generacion_var = ctk.StringVar()
metodo_generacion_combobox = ctk.CTkComboBox(frame_generacion, variable=metodo_generacion_var, 
    values=["Congruencial Lineal Multiplicativo", "Congruencial Lineal", "Cuadrados Medios", "Congruencial permutado"],
    command=lambda event: mostrar_parametros())
metodo_generacion_combobox.pack()

semilla_label = ctk.CTkLabel(frame_generacion, text="Semilla:")
semilla_label.pack()
semilla_entry = ctk.CTkEntry(frame_generacion)
semilla_entry.pack()

a_label = ctk.CTkLabel(frame_generacion, text="Multiplicador:")
a_entry = ctk.CTkEntry(frame_generacion)
c_label = ctk.CTkLabel(frame_generacion, text="Corrimiento:")
c_entry = ctk.CTkEntry(frame_generacion)
m_label = ctk.CTkLabel(frame_generacion, text="Módulo:")
m_entry = ctk.CTkEntry(frame_generacion)

n_label = ctk.CTkLabel(frame_generacion, text="Cantidad (n):")
n_label.pack()
n_entry = ctk.CTkEntry(frame_generacion)
n_entry.pack()

frame_pruebas = ctk.CTkFrame(ventana)
frame_pruebas.pack(padx=10, pady=10, fill="x")

ctk.CTkLabel(frame_pruebas, text="Método de Prueba:").pack()
metodo_prueba_var = ctk.StringVar()
metodo_prueba_combobox = ctk.CTkComboBox(frame_pruebas, variable=metodo_prueba_var, 
    values=["KS", "Chi-cuadrado", "Medias", "Varianza"])
metodo_prueba_combobox.pack()

ejecutar_button = ctk.CTkButton(ventana, text="Ejecutar Prueba", command=ejecutar_prueba)
ejecutar_button.pack(pady=10)

resultado_label = ctk.CTkLabel(ventana, text="", wraplength=380)
resultado_label.pack()

ventana.mainloop()
