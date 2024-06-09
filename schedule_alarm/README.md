

## shedule_alarm ##

En este directorio se puede encontrar una utilidad bastante sencilla pero versatil, es en esencia un reloj y fecha actuales con dos widgets (botones), que se encargan tanto de mostrar/ocultar los elementos, como de programar el cierre del aplicativo. El usuario ingresa la fecha/hora de apagado que traducen en las notificaciones (text1), y visualización en la pantalla antes de terminar.

Para la realización del proyecto se utilizaron las siguientes herramientas (pip install + paquete ó pip install + paquete == 'version')

- Spyder IDE 5.4.2 (Python 3.11.2 32bits x86), Linux
- Tkinter
- Time y datetime
- Pip 24.0
- Pygubu 0.34 y Pygubu-designer 0.38

__style_test2_custom.py__

Como su nombre lo indica es un script de estilo generado desde la herramienta pygubu-designer y viene por defecto con los comentarios y la estructura necesaria para trabajar con estilo ttk para botones, donde destacan primary, secondary, warning... 

```
import tkinter as tk
import tkinter.ttk as ttk


def setup_ttk_styles(master=None):
    my_font = ("console", 12, "bold")
    
    style = ttk.Style(master)
    
    style.configure("primary.TButton",
                    font=my_font,
                    background="#4582EC",
                    foreground="white")
    style.configure("secondary.TButton",
                    font=my_font,
                    background="#ADB5BD", 
                    foreground="white")
    style.configure("warning.TButton",
                    font=my_font,
                    background="#F0AD4E", 
                    foreground="white")    
    style.configure("danger.TButton",
                    font=my_font,
                    background="#D9534F", 
                    foreground="white")
    style.configure("MyStyle.TLabel",
                    font=my_font,
                    background="#e4e0d3", 
                    foreground="#444648")
    style.configure("Entrada.TLabel",
                    font=my_font, 
                    background="#aca6a3", 
                    foreground="black")
```
Para crear el script utilice el menu de preferencias ubicado en editar, luego dirijase a la pestaña que dice Estilos ttk y oprima crear. Como recomendación utilice el mismo directorio que tiene la aplicación ya que esto le permite organizar estilos para cada proyecto que tenga y evitara errores de compilación y/o ejecución. Asi mismo podra buscar el estilo ttk manualmente, escribir el directorio segun sea el caso o borrar.

Notese que para trabajar con la herramienta es necesario cargarla e incluirla en el generate code (generar) cada vez que se utiliza el aplicativo puesto que aparecera como elemento tanto de la clase como de import  

