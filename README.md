# Utils


Herramientas y funcionalidades de apoyo a proyectos

## Practica clases GUI py ##

En el siguiente directorio se puede encontrar un aplicativo sencillo, que basicamente consta de la realización de las 4 operaciones elementales (numéricas), por la entrada de dos datos por el usuario (tipo float) asi mismo se acciona el boton calcular y se efectua la operacion seleccionada (Radiobutton).

Para la realización del proyecto se utilizaron las siguientes herramientas (pip install + paquete ó pip install + paquete == 'version')

- Spyder IDE 5.4.2 (Python 3.11.2 32bits x86), Linux
- Tkinter
- Pillow 9.4.0
- Pip 24.0
- Pygubu 0.34 y Pygubu-designer 0.38

__gui.py__  (respaldo para mainpygubu.py)

En este script se realiza una GUI con las cuatro operaciones básicas utilizando pygubu (asistente grafico para GUI basado en Tk), ubicando 4 radiobutton y un boton calcular; luego  generado el diseño y guardado el archivo __'interfaz.ui'__ (código y generar desde la pestaña aplicación llamado a PATH) e inicializados los elementos y sus respectivos valores para trabajar etiquetas y nombres dentro o fuera del código. Es posible que el usuario ingrese los valores y seleccione la operacion que desea realizar y la efectúe con la ayuda del messagebox

Es incluido un fondo utilizando Photoimage revise el directorio de descarga..., por último para corroborar la ejecución del diseño realizado en pygubu (comando f5), se llamaron los values o valores de radiobutton "var" (builder) para que al realizar un evento del boton (pulsación) imprimiese por consola el valor asignado. Tenga en cuenta que el radiobutton1 ó suma fue seleccionado por defecto 

```
__self.radiobutton1.invoke()__  
```   
A continuación se puede previsualizar como queda el diseño en este punto 

![simple_version_gui_pygubu](https://github.com/JorgeAPinzon/Utils/assets/159712640/80284745-f40d-4fc3-862c-6825be65fb4d)

__main.py__

Esta es una manera convencional de realizar las 4 operaciones con la distinción de crear los widgets con el metodo tk (4 radiobutton para operaciones elementales, 2 entradas de datos y boton de calculo), sin la necesidad de utilizar un import PATH como en el pygubu, en el mismo directorio se llaman las funciones que permiten efectuar las operaciones y el fondo del aplicativo (revise directorio)

```
from addition import add
from subtraction import subtract
from multiplication_division import multiply, divide
```  
Finalmente el usuario puede seleccionar la operación realizada (una vez ingresado los datos numéricos en caso contrario devuelve la excepción), el aplicativo y su diseño solo se puede ver cada vez que se depura y ejecuta el código asi que el resultado es 

![simple_version_gui](https://github.com/JorgeAPinzon/Utils/assets/159712640/ce6970df-bf11-4340-9cec-c5b732737102)


__personalizada_gui.py__

Aqui la lógica del proyecto se obvia para priorizar el aspecto y mejorar la experiencia del usuario, para ello se utiliza nuevamente pygubu solo que con unas particularidades por ejemplo:

1. Al elaborar el diseño con los mismos elementos (widgets), si generamos el código desde la pestaña aplicación pero hemos definido un aspecto diferente para el botón,fondo o incluso radiobutton (imagensuma2.png, imagenresta.png, imagencalcular.png...); obtendremos errores como imágenes no encontradas o elementos tk no compatibles esto por supuesto cuando se depure y compile el código en el intérprete de su preferencia. Esto se soluciona seleccionando script de codigo en lugar de aplicación en la pestaña de generar código.
2. Al generar y compilar el script de código (pygubu) hacia el intérprete deberá notar varias cosas entre ellas; que el código aunque más extenso incluye la ruta de las imágenes y por su puesto al ejecutar tanto en vista previa como en el IDE, el diseño es igual que en el asistente gráfico tk, adicionalmente ya no necesita inicializar los elementos si no más bien adquirir propiedades para su posterior uso, la organización se ve alterada pero se encuentra dentro de una función y una clase main lo que la hace relativamente sencilla de implementar  
3. Los elementos de la interfaz que fuesen cambiados y como es habitual en el lenguaje tienen que estar en el mismo directorio, por que si bien no esta la ruta completa referenciada en el código, esto es por una propiedad tk referenciada en pygubu en contraste a lo que se expreso con anterioridad con la herramienta Photoimage
4. La personalización adicional, como el cambio de cursor de acuerdo al elemento donde este el puntero del mouse, efectos de sombra, tipo de letra para los valores ingresados por el usuario (entry 1, 2), espaciado entre elementos o incluso el mismo empaquetamiento y distribución de los widgets; se realizo dentro de pygubu-designer con el uso de grid

Finalmente se crea un evento del botón presionado para que devuelva el valor definido dentro del asistente, dicho esto la interfaz resultante es:

![personalizadagui](https://github.com/JorgeAPinzon/Utils/assets/159712640/75de72e3-3ad9-40a4-ba80-bfe933b990e2)

__mainpygubu.py__

Tal y como lo indica su nombre fue elaborada para llamar a __personalizada_gui.py__ asi que luego de importar los scripts necesarios tanto para efectuar las operaciones, usar la interfaz personalizada (Interfaz2.app) y asociarla a una variable. Se generó la función main donde se desarrolla el código para las operaciones elementales con su respectiva excepción.

Como nota adicional a la organización, mantenimiento y extensión de funcionalidades al proyecto, se ha de destacar el simplismo que otorga este enfoque y uso de esta herramienta en mainpygubu.py. La interfaz y parte de su funcionamiento general se puede previsualizar a continuación

![personalizadagui2](https://github.com/JorgeAPinzon/Utils/assets/159712640/62c49c6e-34a2-4f7a-afe4-1bdff22c37ec)

Recuerde que algunos detalles pueden hacer que varie todas y cada una de las visualizaciones añadidas, la razón el sistema operativo, la versión de las librerías o inclusive el tema que tenga instalado en su ordenador o que halla preseleccionado en pygubu-designer

__normabotondiseñoopc1.odg__

Este archivo contiene las imágenes utilizadas para algunos de los elementos de la interfaz. Puede acomodarlos o rediseñarlos a su preferencia solo tenga en cuenta que:

- Fue realizado en LIbreOfficeDraw para una versión de 32bits
- Recuerde las dimensiones al momento de importar y exportar los elementos por separado, puesto que la perdida de la calidad es significativa de plataforma a plataforma
- Una vez halla elegido el tamaño y ubicación del elemento, no es posible que en pygubu-designer actualice cambios asi modifique el archivo; luego la recomendación es elaborar una o varias copias y las sobreescriba con el explorador que ofrece el asistente (icono lupa << propiedades del objeto << apartado imagen). Por supuesto no saturar el directorio o renombrar incontables veces los archivos puede agilizar su diseño.

## English Version ##

In the following directory you can find a simple application, which basically consist of carrying out the 4 elementary operations (+, -, *, /), by entering two data by the user (float type), also activating the calculate button and carrying out the select operation (Radiobutton) 

To carry out the project, the following tools were used (pip install + package or pip install + package == 'version')

- Spyder IDE 5.4.2 (Python 3.11.2 32bit x86), Linux
- Tkinter
-Pillow 9.4.0
- Pip 24.0
- Pygubu 0.34 and Pygubu-designer 0.38)

__gui.py__  (mainpygubu.py backup)

In this script a GUI is made with the four basic operations using pygubu (graphi assistant for GUI based on Tk), placing 4 radiobuttons and a calculate button; then generated the design and sabed the file __'interfaz.ui'__(code and generated from the application taba called PATH) and initialized the elements and their respective values to work labels and names inside or outside the code. Its possible for the user to enter the values and select the operation they want to perform and carry it out with the help of the messagebox

A background is included using Photoimage, check the download directory..., finally to corroborate the execution of the design made in pygubu (f5 command), the values of radiobutton "var"(builder) were  called so that when carrying out an event of the button (press), print the assigned value via console. Note radiobutton1 or sum element was selected by default

```
__self.radiobutton1.invoke()__  
```
Below you can preview how the design looks at this point.

![simple_version_gui_pygubu](https://github.com/JorgeAPinzon/Utils/assets/159712640/80284745-f40d-4fc3-862c-6825be65fb4d)




