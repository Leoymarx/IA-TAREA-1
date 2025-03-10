import tkinter as tk
from tkinter import messagebox

intentos = 0

def verificar_numero():
    global intentos
    numero = int(entry_numero.get())
    intentos += 1
    if 0 < numero < 20:
        messagebox.showinfo("Resultado", f"Número válido: {numero}\nIntentos: {intentos}")
    else:
        messagebox.showerror("Error", "El número debe estar entre 0 y 20.")

root = tk.Tk()
root.title("Contar Intentos de Lectura")

label_numero = tk.Label(root, text="Ingrese un número entre 0 y 20:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

button_verificar = tk.Button(root, text="Verificar", command=verificar_numero)
button_verificar.pack()

root.mainloop()