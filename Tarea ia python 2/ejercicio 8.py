import tkinter as tk
from tkinter import messagebox

def sumar_numeros():
    suma = 0
    while True:
        numero = int(entry_numero.get())
        if numero == 0:
            break
        suma += numero
    messagebox.showinfo("Resultado", f"La suma total es: {suma}")

root = tk.Tk()
root.title("Sumar Números hasta Ingresar 0")

label_numero = tk.Label(root, text="Ingrese un número:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

button_sumar = tk.Button(root, text="Sumar", command=sumar_numeros)
button_sumar.pack()

root.mainloop()