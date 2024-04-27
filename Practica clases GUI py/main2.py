#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:03:58 2024

@author: antiXLinux
"""

from addition import add
from subtraction import subtract
from multiplication_division import multiply, divide
from gui2 import create_gui
from tkinter import messagebox


def calculate():
    
    try:
        
        a = float(entry1.get())
        b = float(entry2.get())
        operation = var.get()

        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)

        messagebox.showinfo("Resultado", "El resultado es: " + str(result))

    except ValueError:
        
        messagebox.showerror("Error", "Error: entradas vacias o no validas.")

root, entry1, entry2, var = create_gui(calculate)
root.mainloop()