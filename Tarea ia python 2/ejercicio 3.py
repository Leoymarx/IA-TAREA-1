import tkinter as tk
from tkinter import messagebox

def calcular_descuento():
    mes = entry_mes.get()
    importe = float(entry_importe.get())
    if mes.lower() == "octubre":
        importe -= importe * 0.15
    messagebox.showinfo("Resultado", f"Total a cobrar: {importe:.2f}")

root = tk.Tk()
root.title("Descuento Tienda Octubre")

label_mes = tk.Label(root, text="Ingrese el mes:")
label_mes.pack()

entry_mes = tk.Entry(root)
entry_mes.pack()

label_importe = tk.Label(root, text="Ingrese el importe:")
label_importe.pack()

entry_importe = tk.Entry(root)
entry_importe.pack()

button_calcular = tk.Button(root, text="Calcular Total", command=calcular_descuento)
button_calcular.pack()

root.mainloop()