import tkinter as tk
from tkinter import messagebox

def calcular_aumento():
    sueldo = float(entry_sueldo.get())
    if sueldo < 4000:
        aumento = sueldo * 0.15
    else:
        aumento = sueldo * 0.08
    messagebox.showinfo("Resultado", f"Aumento: {aumento:.2f}")

root = tk.Tk()
root.title("Aumento de Sueldo")

label_sueldo = tk.Label(root, text="Ingrese el sueldo básico:")
label_sueldo.pack()

entry_sueldo = tk.Entry(root)
entry_sueldo.pack()

button_calcular = tk.Button(root, text="Calcular Aumento", command=calcular_aumento)
button_calcular.pack()

root.mainloop()