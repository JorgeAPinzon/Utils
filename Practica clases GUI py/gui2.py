#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:02:48 2024

@author: antiXLinux
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Declarar background_image como una variable global
background_image = None

def create_gui(calculate):
    
    global background_image  # Acceder a la variable global para cargar fondo main
    root = tk.Tk()
    root.geometry('480x480')
    root.title("Calculadora simple")
    var = tk.StringVar()
    var.set('add')

    # Carga la imagen usando PIL
    image = Image.open("/home/antiXLinux/Documentos/Sistemas de Control Enfoque /scripts y programas/Practica clases GUI py/fondo.png")
    background_image = ImageTk.PhotoImage(image)

    # Crea un canvas y añade la imagen de fondo
    canvas = tk.Canvas(root, width=480, height=480)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    # Crea los widgets en el canvas en lugar de en la raíz
    entry1 = tk.Entry(canvas)
    canvas.create_window(240, 100, window=entry1)

    entry2 = tk.Entry(canvas)
    canvas.create_window(240, 150, window=entry2)

    addition_button = tk.Radiobutton(canvas, text='Suma', variable=var, value='add')
    canvas.create_window(240, 200, window=addition_button)

    subtraction_button = tk.Radiobutton(canvas, text='Resta', variable=var, value='subtract')
    canvas.create_window(240, 250, window=subtraction_button)

    multiplication_button = tk.Radiobutton(canvas, text='Multiplicacion', variable=var, value='multiply')
    canvas.create_window(240, 300, window=multiplication_button)

    division_button = tk.Radiobutton(canvas, text='Division', variable=var, value='divide')
    canvas.create_window(240, 350, window=division_button)

    calculate_button = tk.Button(canvas, text='Calcular', command=calculate)
    canvas.create_window(240, 400, window=calculate_button)

    return root, entry1, entry2, var