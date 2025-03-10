import tkinter as tk
from tkinter import messagebox

def sumar_numeros():
    suma = 0
    while suma <= 100:
        numero = int(entry_numero.get())
        suma += numero
    messagebox.showinfo("Resultado", f"La suma total es: {suma}")

root = tk.Tk()
root.title("Sumar hasta que la suma sea superior a 100")

label_numero = tk.Label(root, text="Ingrese un número:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

button_sumar = tk.Button(root, text="Sumar", command=sumar_numeros)
button_sumar.pack()

root.mainloop()