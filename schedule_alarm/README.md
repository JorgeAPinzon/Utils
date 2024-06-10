

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

![pygubu](https://github.com/JorgeAPinzon/Utils/assets/159712640/a6e2ca23-8d8f-495e-9434-f3ddd807c262)


Notese que para trabajar con la herramienta es necesario cargarla e incluirla en el generate code (generar), cada vez que se utiliza el aplicativo puesto que aparecera como elemento tanto de la clase como de import, para mas documentación sobre su uso utilice los recursos de los desarrolladores; gráficamente lo seleccionaria desde el panel de propiedades (siempre y cuando el widget lo permita, parte derecha de la pantalla)   

![pygubu_generate_panel](https://github.com/JorgeAPinzon/Utils/assets/159712640/f863bfea-a39a-4c4d-ab74-2260c34bb7fb)

En ultima instancia se recomienda seguir la estructura del estilo ttk para evitar confusiones, si quiere generar código utilizando la pestaña de aplicación recuerde que deberá guardar el nombre de la interfaz (.ui) en el mismo directorio donde tiene alojado el proyecto o script de interfaz(PROJECT PATH) 

__reloj_off_gui.py__

Este es el script principal donde se ejecutan todas las tareas descritas anteriormente, su organización es bastante sencilla, en primera instancia se define la clase y se desarrolla la ui desde el estilo definido por el usuario independientemente de la cantidad de widgets a los que les halla asignado la definición, después esta el apartado de widgets donde se encuentran: 

- Label1: Es donde esta alojado el fondo de pantalla de la gui y como se ha determinado en anteriores proyectos, esta en el directorio raiz con el nombre __fondo_reloj_grafica.png__, fue asignado desde el panel de propiedades ("image" justo debajo de foreground)
- Label2: Este widget tiene la labor de mostrar la hora actual en formato 12H, ahora bien en el código otras operaciones son realizadas en formato militar (24H a partir de 00:00), no obstante esto no le quita comodidad o funcionalidad para programar la hora deseada
- Label3: Muestra la fecha actual, esto sera clave cuando programe el apagado
- Button1: Es el boton off, despliega u oculta los elementos para programar el "apagado" del aplicativo y captura la fecha seleccionada por el usuario para saber si corresponde a una entrada valida. Cada cierto accionar del boton se limpia el area de notificaciones (8 veces por global contador1)
- Button2: Programar es el widget que involucra varios de los elementos definidos para el aplicativo, ya que corrobora la hora y formato en entry1, la fecha y su conversión en calendar1, esto por supuesto para evitar que se haga antes de la fecha actual para finalmente desplegar los eventos relevantes en el area de notificaciones designada (text1)
- Entry1: Entrada de la hora de apagado en formato 24H, es utilizada la herramienta split para poder preguntar inclusive si el dia de apagado corresponde a fecha actual; asi es posible evitar asignar horas ya transcurridas
- Text1: Es el area de notificaciones entonces muestra los eventos relevantes ingresados. Por la funcionalidad del widget es posible ingresar texto una vez complilada y ejecutada la herramienta, aunque esto particularmente no tenga ninguna funcionalidad asignada, salvo la que determinen los usuarios.

Por último se encuentran las funciones referenciadas a los widgets y el main loop que permite ejecutar la clase principial  

