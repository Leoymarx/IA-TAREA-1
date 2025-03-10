import tkinter as tk
from tkinter import messagebox

def verificar_numero():
    numero = int(entry_numero.get())
    if 0 < numero < 20:
        messagebox.showinfo("Resultado", f"Número válido: {numero}")
    else:
        messagebox.showerror("Error", "El número debe estar entre 0 y 20.")

root = tk.Tk()
root.title("Validar Número en Rango (0, 20)")

label_numero = tk.Label(root, text="Ingrese un número entre 0 y 20:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

button_verificar = tk.Button(root, text="Verificar", command=verificar_numero)
button_verificar.pack()

root.mainloop()