import tkinter as tk
from tkinter import messagebox

def calcular_descuento():
    edad = int(entry_edad.get())
    precio = 50
    if edad < 10:
        precio -= precio * 0.25
    messagebox.showinfo("Resultado", f"Precio a pagar: {precio:.2f}")

root = tk.Tk()
root.title("Descuento Parque de Diversiones")

label_edad = tk.Label(root, text="Ingrese su edad:")
label_edad.pack()

entry_edad = tk.Entry(root)
entry_edad.pack()

button_calcular = tk.Button(root, text="Calcular Descuento", command=calcular_descuento)
button_calcular.pack()

root.mainloop()