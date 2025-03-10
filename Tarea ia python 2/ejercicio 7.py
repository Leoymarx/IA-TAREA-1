import tkinter as tk
from tkinter import messagebox

def calcular_suma():
    n = int(entry_n.get())
    suma = sum(range(1, n+1))
    messagebox.showinfo("Resultado", f"La suma de los primeros {n} números es: {suma}")

root = tk.Tk()
root.title("Suma de Primeros N Números")

label_n = tk.Label(root, text="Ingrese un número:")
label_n.pack()

entry_n = tk.Entry(root)
entry_n.pack()

button_calcular = tk.Button(root, text="Calcular Suma", command=calcular_suma)
button_calcular.pack()

root.mainloop()