import tkinter as tk
from tkinter import messagebox

def calcular_pago():
    nombre = entry_nombre.get()
    horas_normales = float(entry_horas_normales.get())
    horas_extras = float(entry_horas_extras.get())
    hijos = int(entry_hijos.get())

    pago_hora_normal = 100
    pago_hora_extra = pago_hora_normal * 1.5
    bonificacion_hijos = hijos * 0.5

    pago_normales = horas_normales * pago_hora_normal
    pago_extras = horas_extras * pago_hora_extra
    total_pago = pago_normales + pago_extras + bonificacion_hijos

    messagebox.showinfo("Resultado", f"Nombre: {nombre}\nPago por horas normales: {pago_normales:.2f}\nPago por horas extras: {pago_extras:.2f}\nBonificación por hijos: {bonificacion_hijos:.2f}\nPago total: {total_pago:.2f}")

root = tk.Tk()
root.title("Cálculo de Pago")

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()

entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_horas_normales = tk.Label(root, text="Horas normales trabajadas:")
label_horas_normales.pack()

entry_horas_normales = tk.Entry(root)
entry_horas_normales.pack()

label_horas_extras = tk.Label(root, text="Horas extras trabajadas:")
label_horas_extras.pack()

entry_horas_extras = tk.Entry(root)
entry_horas_extras.pack()

label_hijos = tk.Label(root, text="Número de hijos:")
label_hijos.pack()

entry_hijos = tk.Entry(root)
entry_hijos.pack()

button_calcular = tk.Button(root, text="Calcular Pago", command=calcular_pago)
button_calcular.pack()

root.mainloop()