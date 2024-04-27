#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:59:14 2024

@author: antiXLinux
"""
#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class Interfaz2App:
    
    def __init__(self, master=None):
        
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        toplevel1.geometry("480x480")
        frame1 = ttk.Frame(toplevel1)
        frame1.configure(height=200, width=200)
        
        # Fondo de la imagen
        self.fondoimagen = ttk.Label(frame1, name="fondoimagen")
        self.img_fondo = tk.PhotoImage(file="fondo.png")
        self.fondoimagen.configure(
            image=self.img_fondo,
            relief="flat",
            takefocus=False,
            text='label1')
        self.fondoimagen.grid(column=0, row=0, sticky="n")
        
        # Entradas de caja
        self.caja = ttk.Entry(frame1, name="caja")
        self.entry1 = tk.StringVar()
        self.caja.configure(font="{FreeMono} 12 {}", textvariable=self.entry1)
        self.caja.grid(column=0, pady=75, row=0, sticky="n")
        self.cajaII = ttk.Entry(frame1, name="cajaii")
        self.entry2 = tk.StringVar()
        self.cajaII.configure(
            font="{FreeMono} 12 {}",
            textvariable=self.entry2)
        self.cajaII.grid(column=0, pady=125, row=0, sticky="n")
        
        # RadioButton de suma 
        radiobutton1 = ttk.Radiobutton(frame1)
        self.img_imagensuma2 = tk.PhotoImage(file="imagensuma2.png")
        self.var = tk.StringVar(value='add')
        radiobutton1.configure(
            cursor="dotbox",
            image=self.img_imagensuma2,
            text='Suma',
            value="add",
            variable=self.var)
        radiobutton1.grid(column=0, pady=175, row=0, sticky="n")
        
        # RadioButton de resta 
        radiobutton2 = ttk.Radiobutton(frame1)
        self.img_imagenresta = tk.PhotoImage(file="imagenresta.png")
        radiobutton2.configure(
            cursor="dotbox",
            image=self.img_imagenresta,
            text='Resta',
            value="subtract",
            variable=self.var)
        radiobutton2.grid(column=0, pady=215, row=0, sticky="n")
        
        # RadioButton de multiplicacion
        radiobutton3 = ttk.Radiobutton(frame1)
        self.img_imagenmultiplicacion = tk.PhotoImage(
            file="imagenmultiplicacion.png")
        radiobutton3.configure(
            cursor="dotbox",
            image=self.img_imagenmultiplicacion,
            text='Multiplicación',
            value="multiply",
            variable=self.var)
        radiobutton3.grid(column=0, pady=255, row=0, sticky="n")
        
        # RadioButton de division
        radiobutton4 = ttk.Radiobutton(frame1)
        self.img_imagendivision = tk.PhotoImage(file="imagendivision.png")
        radiobutton4.configure(
            cursor="dotbox",
            image=self.img_imagendivision,
            text='División',
            value="divide",
            variable=self.var)
        radiobutton4.grid(column=0, pady=295, row=0, sticky="n")
        
        # Boton Calcular
        self.calculate_button = ttk.Button(frame1, name="calculate_button")
        self.img_imagencalcular = tk.PhotoImage(file="imagencalcular.png")
        self.calculate_button.configure(
            cursor="watch",
            image=self.img_imagencalcular,
            style="Toolbutton",
            text='Calcular')
        self.calculate_button.grid(column=0, pady=345, row=0, sticky="n")
        self.calculate_button.configure(command=self.botonpresionado)
        frame1.grid(column=0, row=0)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def botonpresionado(self):
        print(self.var.get())


if __name__ == "__main__":
    app = Interfaz2App()
    app.run()