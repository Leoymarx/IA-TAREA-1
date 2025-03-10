import tkinter as tk
from tkinter import messagebox

def verificar_numero():
    numero = int(entry_numero.get())
    if numero < 10:
        messagebox.showinfo("Resultado", f"Número válido: {numero}")
    else:
        messagebox.showerror("Error", "El número debe ser menor que 10.")

root = tk.Tk()
root.title("Validar Número Menor que 10")

label_numero = tk.Label(root, text="Ingrese un número menor que 10:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

button_verificar = tk.Button(root, text="Verificar", command=verificar_numero)
button_verificar.pack()

root.mainloop()