#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:19:30 2024

@author: antiXLinux
"""

#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Interfaz.ui"

class InterfazApp:
    
    def __init__(self, master=None):
        
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        
        # Main widget
        
        self.mainwindow: tk.Toplevel = builder.get_object("toplevel1", master)
        
        # Cargar la imagen de fondo
        self.background_image = tk.PhotoImage(file="/home/antiXLinux/Documentos/Sistemas de Control Enfoque /scripts y programas/Practica clases GUI py/fondo.png")  # Reemplaza esto con la ruta a tu imagen
        background_label = tk.Label(self.mainwindow, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.entry1: tk.StringVar = None
        self.entry2: tk.StringVar = None
        
        #self.calculate_button: tk.StringVar = None
        
        #inicializa el boton o elementos de la interfaz 
        self.calculate_button: tk.Button = builder.get_object('calculate_button', master)
        
        # llama las variables guardadas en interfaz ui en este caso iguales en ese campo ojo
        self.var = builder.get_variable("var")
        self.radiobutton1 = builder.get_object("radiobutton1")
        self.radiobutton2 = builder.get_object("radiobutton2")
        self.radiobutton3 = builder.get_object("radiobutton3")
        self.radiobutton4 = builder.get_object("radiobutton4")
        
        builder.import_variables(self)
        
        # Mover la imagen de fondo al fondo
        background_label.lower()
        
        builder.connect_callbacks(self)
        
        # predeterminar seleccion radiobutton por interfaz 
        self.radiobutton1.invoke()

    def run(self):
        self.mainwindow.mainloop()
    
    # modo test a boton presionado uselo con cuidado por que la clase puede darle problemas    
    def botonpresionado(self):
        print(self.var.get())
        

if __name__ == "__main__":
    
    app = InterfazApp()
    app.run()
