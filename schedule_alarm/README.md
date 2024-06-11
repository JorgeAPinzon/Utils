

## shedule_alarm ##

En este directorio se puede encontrar una utilidad bastante sencilla pero versátil, es en esencia un reloj y fecha actuales con dos widgets (botones), que se encargan tanto de mostrar/ocultar los elementos, como de programar el cierre del aplicativo. El usuario ingresa la fecha/hora de apagado que traducen en las notificaciones (text1), y visualización en la pantalla antes de terminar.

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

Para crear el script utilice el menu de preferencias ubicado en editar, luego dirijase a la pestaña que dice Estilos ttk y oprima crear. Como recomendación utilice el mismo directorio que tiene la aplicación ya que esto le permite organizar estilos para cada proyecto que tenga y evitará errores de compilación y/o ejecución. Asi mismo podra buscar el estilo ttk manualmente, escribir el directorio segun sea el caso o borrar.

![pygubu](https://github.com/JorgeAPinzon/Utils/assets/159712640/a6e2ca23-8d8f-495e-9434-f3ddd807c262)


Nótese que para trabajar con la herramienta es necesario cargarla e incluirla en el generate code (generar), cada vez que se utiliza el aplicativo puesto que aparecerá como elemento tanto de la clase como de import, para mas documentación sobre su uso consulte los recursos de los desarrolladores; gráficamente lo seleccionaria desde el panel de propiedades (siempre y cuando el widget lo permita, parte derecha de la pantalla)   

![pygubu_generate_panel](https://github.com/JorgeAPinzon/Utils/assets/159712640/f863bfea-a39a-4c4d-ab74-2260c34bb7fb)

En última instancia se recomienda seguir la estructura del estilo ttk para evitar confusiones, si quiere generar código utilizando la pestaña de aplicación recuerde que deberá guardar el nombre de la interfaz (.ui) en el mismo directorio donde tiene alojado el proyecto o script de interfaz(PROJECT PATH) 

__reloj_off_gui.py__

Este es el script principal donde se ejecutan todas las tareas descritas anteriormente, su organización es bastante sencilla, en primera instancia se define la clase y se desarrolla la ui desde el estilo definido por el usuario independientemente de la cantidad de widgets a los que les halla asignado la definición, después esta el apartado de widgets donde se encuentran: 

- Label1: Es donde esta alojado el fondo de pantalla de la gui y como se ha determinado en anteriores proyectos, esta en el directorio raiz con el nombre __fondo_reloj_grafica.png__, fue asignado desde el panel de propiedades en pygubu-designer ("image" justo debajo de foreground)
- Label2: Este widget tiene la labor de mostrar la hora actual en formato 12H, ahora bien en el código otras operaciones son realizadas en formato militar (24H a partir de 00:00), no obstante esto no le quita comodidad o funcionalidad para programar la hora deseada
- Label3: Muestra la fecha actual, esto sera clave cuando programe el apagado
- Button1: Es el boton off, despliega u oculta los elementos para programar el "apagado" del aplicativo y captura la fecha seleccionada por el usuario para saber si corresponde a una entrada valida. Cada cierto accionar del botón se limpia el area de notificaciones (8 veces por global contador1)
- Button2: Programar es el widget que involucra varios de los elementos definidos para el aplicativo, ya que corrobora la hora y formato en entry1, la fecha y su conversión en calendar1, esto por supuesto para evitar que se haga antes de la fecha actual para finalmente desplegar los eventos relevantes en el area de notificaciones designada (text1)
- Entry1: Entrada de la hora de apagado en formato 24H, es utilizada la herramienta split para poder preguntar inclusive si el día de apagado corresponde a fecha actual; asi es posible evitar asignar horas ya transcurridas
- Text1: Es el área de notificaciones entonces muestra los eventos relevantes ingresados. Por la funcionalidad del widget es posible ingresar texto una vez complilada y ejecutada la herramienta, aunque esto particularmente no tenga ninguna funcionalidad asignada, salvo la que determinen los usuarios.

Por último se encuentran las funciones referenciadas a los widgets y el main loop que permite llamar a la clase principial __InterfazRelojOffApp__ 

- Función actualizar_reloj(self):

Propósito: Mostrar la hora y fecha actuales para facilitar la programación de apagado   
Uso: Establece la hora y fecha actual, en conjunto con el evento reloj cierra el aplicativo 

- Función run(self)

Proposito y uso: bucle de ejecución de la ventana principal

- Función botonpress(self):

Propósito: Desplegar o ocultar los elementos para programar el apagado del aplicativo   
Uso: Presionar el botón Off para desplegar la interfaz de programación del apagado y limpiar el área de notificaciones cada n veces

- Función botonprogram(self):

Propósito: Programar alarmas y notificaciones en la interfaz gráfica   
Uso: Seleccionar la fecha y hora deseada para que al presionar el botón y por supuesto respetando la lógica desarrollada, se cierre el aplicativo de forma autónoma   

- Función focus_entry(self, event):

Propósito: Realizar seguimiento al focus del usuario en el widget y limpiar la entrada una vez realizado el evento  
Uso: Referenciar al usuario la manera en que debe ingresar la hora por ejemplo 14:17 (2:17 PM)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## English Version ##

In this directory you can find a fairly simple but versatile utility, it is essentially a current clock and date with two widgets (buttons), which are responsible for both showing/hiding the elements, and for scheduling the closing of the application. The user enters the shutdown date/time that is translated into the notifications (text1), and displayed on the screen before finishing.

Following tools were used for the project (pip install + package or pip install + package == 'version')

- Spyder IDE 5.4.2 (Python 3.11.2 32bits x86), Linux
- Tkinter
- Time and datetime
- Pip 24.0
- Pygubu 0.34 and Pygubu-designer 0.38

__style_test2_custom.py__

As its name indicates, it is a style script generated from the pygubu-designer tool and comes by default with the comments and the necessary structure to work with ttk style for primary, secondary, warning... buttons.

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

To create the script use the preferences menu located in edit, then go to the tab that says ttk styles and press create. As a recommendation, use the same directory as the application since this allows you to organize styles for each project you have and will avoid compilation and/or execution errors. Likewise, you can search for the ttk style manually, write the directory as appropriate or delete it.

![pygubu](https://github.com/JorgeAPinzon/Utils/assets/159712640/a6e2ca23-8d8f-495e-9434-f3ddd807c262)

Note that to work with the tool it is necessary to load it and include it in the generate code, every time the application is used since it will appear as an element of both the class and import, for more documentation on its use consult the developers' resources; graphically you would select it from the properties panel (as long as the widget allows it, right side of the screen). 

![pygubu_generate_panel](https://github.com/JorgeAPinzon/Utils/assets/159712640/f863bfea-a39a-4c4d-ab74-2260c34bb7fb)

Ultimately, it is recommended to follow the ttk style structure to avoid confusion. If you want to generate code using the application tab, remember that you must save the interface name (.ui) in the same directory where the project or interface script is hosted. (PROJECT PATH)

__reloj_off_gui.py__

This is the main script where all the tasks described above are executed, its organization is quite simple, in first instance the class is defined and the ui is developed from the style defined by the user regardless of the number of widgets to which the definition is assigned, then there is the widgets section where they are located: 

- Label1: This is where the gui wallpaper is hosted and as has been determined in previous projects, it is in the root directory with the name __fondo_reloj_grafica.png__, it was assigned from the properties panel in pygubu-designer ("image" just below foreground)
- Label2: This widget has the task of showing the current time in 12H format, however in the code other operations are carried out in military format (24H from 00:00), however this does not take away from the convenience or functionality for programming the desired time
- Label3: Shows the current date, this will be key when scheduling the shutdown
- Button1: It is the off button, it displays or hides the elements to program the "shutdown" of the application and captures the date selected by the user to know if it corresponds to a valid entry. Every time the button is pressed the notification area is cleared (8 times per global counter1)
- Button2: Programar is the widget that involves several of the elements defined for the application, since it confirms the time and format in entry1, the date and its conversion into calendar1, this of course to prevent it from being done before the current date to finally display the relevant events in the designated notification area (text1)
- Entry1: Entry of the shutdown time in 24H format, the split tool is used to even ask if the shutdown day corresponds to the current date; This way it is possible to avoid assigning hours that have already passed
- Text1: It is the notification area so it shows the relevant events entered. Due to the functionality of the widget, it is possible to enter text once the tool is compiled and executed, although this does not particularly have any assigned functionality, except that determined by the users.

Finally, there are the functions referenced to the widgets and the main loop that allows calling the main class __InterfaceClockOffApp__. 

- function update_clock(self):

Purpose: Display the current time and date to facilitate shutdown scheduling
Use: Sets the current time and date, together with the clock event, closes the application

- run(self) function

Purpose and use: main window execution loop

- Buttonpress(self) function:

Purpose: Display or hide the elements to schedule the shutdown of the application
Usage: Press the Off button to display the shutdown scheduling interface and clear the notification area every n times

- Buttonprogram(self) function:

Purpose: Schedule alarms and notifications in the graphical interface
Use: Select the desired date and time so that when you press the button and of course respecting the developed logic, the application closes autonomously

- Focus_entry(self, event) function:

Purpose: Track the user's focus on the widget and clean up the entry once the event has taken place
Use: Reference the user how to enter the time, for example 14:17 (2:17 PM)


