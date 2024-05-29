
import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.display = tk.Entry(master, width=25, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '%', '√', 'x²', '='
        ]

        fila = 1
        columna = 0
        for boton in botones:
            comando = lambda x=boton: self.click(x)
            ttk.Button(master, text=boton, command=comando, width=6).grid(row=fila, column=columna, padx=5, pady=5)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

    def click(self, valor):
        if valor == '=':
            try:
                resultado = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif valor == 'C':
            self.display.delete(0, tk.END)
        elif valor == '√':
            try:
                num = float(self.display.get())
                if num >= 0:
                    resultado = num ** 0.5
                    self.display.delete(0, tk.END)
                    self.display.insert(0, resultado)
                else:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error (num negativo)")
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif valor == 'x²':
            try:
                num = float(self.display.get())
                resultado = num ** 2
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif valor == '%':
            try:
                num = float(self.display.get())
                resultado = num / 100
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            texto_actual = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, texto_actual + valor)

root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()
