# Utils


Herramientas y funcionalidades de apoyo a proyectos

## Practica clases GUI py ##

En el siguiente directorio se puede encontrar un aplicativo sencillo, que basicamente consta de la realización de las 4 operaciones elementales (numéricas), por la entrada de dos datos por el usuario (tipo float) asi mismo se acciona el boton calcular y se efectua la operacion seleccionada (Radiobutton).

Para la realización del proyecto se utilizaron las siguientes herramientas (pip install + paquete ó pip install + paquete == 'version')

- Spyder IDE 5.4.2 (Python 3.11.2 32bits x86)
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

1. Como al elaborar el diseño con los mismos elementos (widgets), si generamos el codigo desde la pestaña aplicación pero hemos definido un aspecto diferente para el boton,fondo o incluso radiobutton (imagensuma2.png, imagenresta.png, imagencalcular.png...); obtendremos errores como imágenes no encontradas o elementos tk no compatibles esto por supuesto cuando se depure y compile el código en el intérprete de su preferencia. Esto se soluciona seleccionando script de codigo en lugar de aplicación en la pestaña de generar código.
2. Al generar y compilar el script de código (pygubu) hacia el intérprete deberá notar varias cosas entre ellas; que el código aunque más extenso incluye la ruta de las imágenes y por su puesto al ejecutar tanto en vista previa como en el IDE, el diseño es igual que en el asistente gráfico tk, adicionalmente ya no necesita inicializar los elementos si no más bien adquirir propiedades para su posterior uso, la organización se ve alterada pero se encuentra dentro de una función y una clase main lo que la hace relativamente sencilla de implementar  
3. Los elementos de la interfaz que fuesen cambiados y como es habitual en el lenguaje tienen que estar en el mismo directorio, por que si bien no esta la ruta completa referenciada en el código, esto es por una propiedad tk referenciada en pygubu en contraste a lo que se expreso con anterioridad con la herramienta Photoimage

Finalmente se crea un evento del botón presionado para que devuelva el valor definido dentro del asistente gráfico   

