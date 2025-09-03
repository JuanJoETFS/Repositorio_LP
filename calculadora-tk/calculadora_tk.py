import tkinter as tk

from tkinter import messagebox
 
# --- Configuracion del Icono
RUTA_DEL_LOGO = "cal.ico"
 
# --- Funciones de la Calculadora 

def sumar():

    try:

        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:

        messagebox.showerror("Error", "Por favor, ingrese números válidos")
 
def restar():

    try:

        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:

        messagebox.showerror("Error", "Por favor, ingrese números válidos")
 
# --- Configuración de la Interfaz Gráfica ---

ventana = tk.Tk()
ventana.title("Calculadora Simple")
ventana.geometry("300x300")
 
try:

    ventana.iconbitmap(RUTA_DEL_LOGO)

except tk.TclError:

    print(f"Advertencia: No se pudo cargar el icono desde la ruta: {RUTA_DEL_LOGO}")
 
etiqueta_instruccion = tk.Label(ventana, text="Ingrese dos números para sumar o restar:")

etiqueta_instruccion.pack(pady=10)
 
entry_num1 = tk.Entry(ventana)

entry_num1.pack()
 
entry_num2 = tk.Entry(ventana)

entry_num2.pack()
 
btn_sumar = tk.Button(ventana, text="Sumar", command=sumar)

btn_sumar.pack(pady=5)
 
btn_restar = tk.Button(ventana, text="Restar", command=restar)

btn_restar.pack(pady=5)
 
etiqueta_resultado = tk.Label(ventana, text="Resultado:")

etiqueta_resultado.pack(pady=10)
 
ventana.mainloop()

 