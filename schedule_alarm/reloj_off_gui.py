#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:18:16 2024

@author: antiXLinux
"""

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.calendarframe import CalendarFrame
import time
import style_test2_custom_
import datetime


class InterfazRelojOffApp:
    
    def __init__(self, master=None):
        
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        
        style_test2_custom_.setup_ttk_styles(toplevel1) # comentarear esta linea activa custom
        frame1 = ttk.Frame(toplevel1)                     # x asistente pygubu ojo
        frame1.configure(height=200, width=200)
        self.contador =0
        
        # Declaracion de widgets pyg
        
        label1 = ttk.Label(frame1)
        self.img_fondo_reloj_grafica = tk.PhotoImage(
            file="fondo_reloj_grafica.png")
        label1.configure(image=self.img_fondo_reloj_grafica, text='label1')
        label1.grid(column=0, row=0)
        
        label2 = ttk.Label(frame1)
        label2.configure(
            font="{MathJax_Vector} 12 {bold}",
            style="MyStyle.TLabel")  # Estilo dinamico
        label2.configure(style="MyStyle.TLabel", text='HORA ') # Estilo estatico 
        label2.grid(column=0, padx=100, pady=100, row=0, sticky="nw")
        self.label2 = label2 # instancia de la clase ttklabel para label2.config
        
        label3 = ttk.Label(frame1)
        label3.configure(
            font="{MathJax_Vector} 12 {bold}",
            style="MyStyle.TLabel")  # Estilo dinamico
        label3.configure(style="MyStyle.TLabel", text='HORA ') # Estilo estatico
        label3.configure(style="MyStyle.TLabel", text='FECHA')
        label3.grid(column=0, padx=100, pady=200, row=0, sticky="nw")
        self.label3 = label3
        
        button1 = ttk.Button(frame1)
        button1.configure(style="secondary.TButton", text='Boton OFF')
        button1.grid(column=0, padx=300, pady=150, row=0, sticky="nw")
        button1.configure(command=self.botonpress)
        
        calendarframe1 = CalendarFrame(frame1)
        calendarframe1.configure(
            calendarbg="#dedce0",
            calendarfg="#1b191b",
            cursor="X_cursor",
            firstweekday=6,
            headerbg="#ffffff",
            headerfg="#000000",
            linewidth=3,
            relief="groove",
            selectbg="#5c4634",
            selectfg="#ffffff")
        #calendarframe1.grid(column=0, row=0) mostrar calendario en la gui pygubu por defecto
        self.calendarframe1 = calendarframe1
        self.calendar_visible = False
        
        button2 = ttk.Button(frame1)
        button2.configure(style="primary.TButton", text='Programar')
        #button2.grid(column=0, padx=210, row=0, sticky="w")
        button2.configure(command=self.botonprogram)
        self.button2 = button2      # ES LINEA IMPORTANTE POR QUE SON ATRIBUTOS Fu() .desplegable
        self.button2_visible = False
        
        entry1 = ttk.Entry(frame1)
        _text_ = 'Formato(Militar H y Min) 00:00'
        entry1.delete("0", "end")
        entry1.insert("0", _text_)
        #entry1.grid(column=0, ipadx=20, padx=160, pady=270, row=0, sticky="sw") por defecto
        self.entry1= entry1
        entry1.bind("<FocusIn>", self.focus_entry)
        self.entry_focused = False
        #self.entry1_visible = False linea hasta el momento innecesaria OJO
        
        text1 = tk.Text(frame1)
        text1.configure(
            background="#594329",
            borderwidth=0,
            font="{DejaVu Sans} 10 {}",
            foreground="#d9c491",
            height=10,
            insertborderwidth=0,
            width=50)
        _text_ = 'Area de Notificaciones'
        text1.insert("0.0", _text_)
        text1.grid(column=0, padx=20, pady=20, row=0, sticky="se")
        self.text1 = text1
        
        # para el apagado automatico las dos siguientes bucle de reloj
        self.hora =0
        self.minutos=0
        
        frame1.grid(column=0, row=0)
        self.frame1 = frame1
        
        # Main widget
        self.mainwindow = toplevel1
        self.actualizar_reloj()
        
        
    def actualizar_reloj(self):
        
        self.tiempo_actual = time.strftime('%I:%M:%S %p')  # Formato de 12 horas con AM/PM
        self.tiempo_actual2 = time.strftime('%H:%M:%S')  # Formato de 24 horas
        fecha_actual = time.strftime('%A, %d de %B de %Y')
        self.label2.config(text='Hora:  ' + self.tiempo_actual)
        self.label3.config(text='Fecha:  ' + fecha_actual)
        
        horareal = self.tiempo_actual2.split(":")[0]
        minutoreal = self.tiempo_actual2.split(":")[1]
        
        # Temporizador de apagado
        
        if self.hora == int(horareal) and self.minutos == int(minutoreal):
            
            self.mainwindow.destroy()
        
        self.mainwindow.after(1000, self.actualizar_reloj)
        
        
    def run(self):
        
        self.mainwindow.mainloop()
        
        
    def botonpress(self):
        
        if self.calendar_visible:
            
            self.calendarframe1.grid_remove()
            self.entry1.grid_remove()
            self.button2.grid_remove()
                      
        else:
            
            self.calendarframe1.grid(column=0, row=0)
            self.entry1.grid(column=0, ipadx=20, padx=160, pady=270, row=0, sticky="sw")
            self.button2.grid(column=0, padx=210, row=0, sticky="w")
            
        self.calendar_visible = not self.calendar_visible
        
        # Obtener la fecha seleccionada
        
        selected_date = self.calendarframe1.selection
        
        print(self.contador) # Elemento auxiliar para borrado area de notificaciones 
        
        if self.contador == 8:
       
            self.text1.delete("1.0", "end")
            self.contador = 1
            
        else:
    
            self.contador += 1
        
        if selected_date is not None and self.entry_focused and self.contador==0: #comando sin nada
            
            print("Fecha no programada")
            self.text1.insert("1.0", "Fecha no programada\n")
            
        else:
            
            print ("Seleccione una fecha")
            self.text1.insert("1.0", "Seleccione fecha\n")
            
        
            
    def botonprogram(self):
        
        global contador # se utiliza para llamar lo que antes de clase es una variable global
        
        if not self.entry_focused:
            
            print("No ha seleccionado la hora en formato 00:00")
            self.text1.insert("1.0", "No ha seleccionado la hora en formato 00:00\n")
        
        # Obtener la fecha seleccionada 
        
        selected_date = self.calendarframe1.selection
        fecha_actual = datetime.date.today() # pendiente para preguntar a partir de hoy
        
        if selected_date is not None and self.entry_focused:
            
            # Convertir la fecha seleccionada a un objeto datetime.date
            # pasado a esta ubicacion y no en linea antes del if por excepcion de primera ejecucion
            
            selected_date_obj = datetime.date(selected_date.year, selected_date.month, selected_date.day)
            
            if selected_date_obj >= fecha_actual:
                
                hora_minutos = self.entry1.get().split(":")
                
            #minutos = self.tiempo_actual.split(":")[0] # [0] para horas [2] segundos usar en print 
                
                if len(hora_minutos) == 2:
                    
                    self.hora = int(hora_minutos[0])
                    self.minutos = int(hora_minutos[1])
                    horareal = self.tiempo_actual2.split(":")[0]
                    minutoreal = self.tiempo_actual2.split(":")[1]
                    
                    if self.hora <=23 and self.minutos <=60:
                        
                        if selected_date_obj == fecha_actual and self.hora <= int(horareal) and self.minutos < int(minutoreal):
                            
                            print("Verifique la hora ingresada")
                            self.text1.insert("1.0", "Verifique la hora ingresada\n")
                       
                        else:
                            
                            # pseudo - animacion del boton programar
                            
                            self.style = ttk.Style()
                            self.style.configure('primary.TButton', foreground='green', background='light green')
                            self.button2.config(style='primary.TButton', text = 'Programado')
                                
                            print(f"Hora Programada: {self.hora}:{self.minutos}")
                            self.text1.insert("1.0", f"Hora Programada: {self.hora}:{self.minutos}\n")
                            print (f"Fecha Programada: {selected_date_obj}")
                            self.text1.insert("1.0", f"Fecha Programada: {selected_date_obj}\n")
                            #print (f"Minuto real 24H: {minutoreal}")
                            self.contador +=1
            
                    else:
                        
                        print("Solo formato militar H : min")
                        self.text1.insert("1.0", "Solo formato militar H : min\n")
                        
                else:
                    
                    print("Por favor, ingrese la hora en formato HH:MM")
                    self.text1.insert("1.0", "Por favor, ingrese la hora en formato HH:MM\n")
                
                print(f"Ejecutado a las: {self.tiempo_actual}") # todos los print como aux gui
                self.text1.insert("1.0", f"Ejecutado a las: {self.tiempo_actual}\n")
                
            else:
                
                print("La fecha seleccionada debe ser igual o posterior a la fecha actual.")
                self.text1.insert("1.0", "La fecha seleccionada debe ser igual o posterior a la fecha actual.\n")
            
        else:
            
            print ("Seleccione una fecha")
            self.text1.insert("1.0", "Seleccione una fecha\n")
            
    def focus_entry(self, event): # necesita el event por que no es un widget atribuido
                                   # y se usa la palabra clave arriba .bind focusin
                                   
        self.entry1.delete("0", "end")
        self.entry1.focus_set()
        self.entry_focused = True
        

if __name__ == "__main__":

    app = InterfazRelojOffApp()
    app.run()

    