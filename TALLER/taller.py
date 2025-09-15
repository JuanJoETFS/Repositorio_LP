import tkinter as tk
from tkinter import messagebox, Toplevel
import random

# Configuracion del icono
RUTA_DEL_LOGO = "icon.ico"

# --- Funciones del Juego ---

numero_secreto = 0
intentos_restantes = 0

def iniciar_juego_nuevo():
    """Inicia una nueva partida del juego de adivinar el número."""
    global numero_secreto, intentos_restantes
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 10  
    etiqueta_resultado.config(text=f"Adivina el número (1-100). Tienes {intentos_restantes} intentos.")
    entry_intento.delete(0, tk.END)
    entry_intento.config(state=tk.NORMAL)
    btn_adivinar.config(state=tk.NORMAL)

def verificar_intento():
    """Verifica el número ingresado por el usuario."""
    global intentos_restantes
    try:
        intento = int(entry_intento.get())
        if intento < 1 or intento > 100:
            messagebox.showwarning("Entrada inválida", "Por favor, ingresa un número entre 1 y 100.")
            return

        intentos_restantes -= 1

        if intento == numero_secreto:
            messagebox.showinfo("¡Felicidades!", f"¡Adivinaste! El número era {numero_secreto}.")
            entry_intento.config(state=tk.DISABLED)
            btn_adivinar.config(state=tk.DISABLED)
        elif intento < numero_secreto:
            etiqueta_resultado.config(text=f"El número es más alto. Intentos restantes: {intentos_restantes}")
        else:
            etiqueta_resultado.config(text=f"El número es más bajo. Intentos restantes: {intentos_restantes}")

        if intentos_restantes == 0 and intento != numero_secreto:
            messagebox.showinfo("Fin del juego", f"Te quedaste sin intentos. El número era {numero_secreto}.")
            entry_intento.config(state=tk.DISABLED)
            btn_adivinar.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def mostrar_ayuda():
    """Muestra una ventana de ayuda."""
    messagebox.showinfo(
        "Ayuda del Juego",
        "1. Presiona 'Juego > Nuevo Juego' para comenzar.\n"
        "2. Adivina un número entre 1 y 100.\n"
        "3. Tienes 10 intentos.\n\n"
        "¡Buena suerte!"
    )

def salir():
    """Cierra la aplicación."""
    ventana.quit()

# --- Configuración de la Interfaz Gráfica ---

ventana = tk.Tk()
ventana.title("Adivina el Número")
ventana.geometry("350x200")

try:
    ventana.iconbitmap(RUTA_DEL_LOGO)
except tk.TclError:
    print(f"Advertencia: No se pudo cargar el icono desde la ruta: {RUTA_DEL_LOGO}")

# --- Menú ---
barra_menu = tk.Menu(ventana)
menu_juego = tk.Menu(barra_menu, tearoff=0)
menu_juego.add_command(label="Nuevo Juego", command=iniciar_juego_nuevo)
menu_juego.add_separator()
menu_juego.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Juego", menu=menu_juego)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Mostrar Ayuda", command=mostrar_ayuda)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)

# --- Widgets de la ventana principal ---
etiqueta_instruccion = tk.Label(ventana, text="Ingresa tu intento:")
etiqueta_instruccion.pack(pady=10)

entry_intento = tk.Entry(ventana)
entry_intento.pack(pady=5)

btn_adivinar = tk.Button(ventana, text="Adivinar", command=verificar_intento)
btn_adivinar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Presiona 'Juego > Nuevo Juego' para empezar.")
etiqueta_resultado.pack(pady=10)

iniciar_juego_nuevo() 

ventana.mainloop()

