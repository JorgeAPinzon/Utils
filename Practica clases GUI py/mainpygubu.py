#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:38:46 2024

@author: antiXLinux
"""

from addition import add
from subtraction import subtract
from multiplication_division import multiply, divide
#import gui reemplace aqui para una interfaz solo con fondo
import personalizada_gui
import tkinter as tk
import tkinter.messagebox as messagebox

def main():
        
    #creando instancia de la aplicacion
    app = personalizada_gui.Interfaz2App()
       
    # Definiendo la función de suma
    def calcular():
        
        try:
            
            a = float(app.entry1.get())
            b = float(app.entry2.get())
            operation = app.var.get()
            
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
            
            messagebox.showerror("Error", "Entradas vacias o no validas.")
    
    app.calculate_button.config(command=calcular)
    #ejecutando aplicacion 
    app.run()
    
    
if __name__ == "__main__":  
    main()
    