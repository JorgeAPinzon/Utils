# Utils


Herramientas y funcionalidades de apoyo a proyectos

## Practica clases GUI py ##

En el siguiente directorio se puede encontrar un aplicativo sencillo, que basicamente consta de la realización de las 4 operaciones basicas (numericas), por la entrada de dos datos por el usuario (tipo float) asi mismo se acciona el boton calcular y se efectua la operacion seleccionada (Radiobutton).

Para la realizacion del proyecto se utilizaron las siguientes herramientas (pip install + paquete ó pip install + paquete == 'version')

- Spyder IDE 5.4.2 (Python 3.11.2 32bits x86)
- Tkinter
- Pillow 9.4.0
- Pip 24.0
- Pygubu 0.34 y Pygubu-designer 0.38

__gui.py__

En este script se realizan las cuatro operaciones basicas utilizando pygubu (asistente grafico para GUI basado en Tk) utilizando 4 radiobutton y un boton calcular; luego  generado el diseño y guardado el archivo 'interfaz.ui'(codigo <<y generar desde la pestaña aplicacion llamado PATH) e inicializados los elementos y sus respectivos valores para seleccionar etiquetas y nombres para el manejo de widgets dentro o fuera del codigo. Se llama el fondo utilizando Photoimage revise el directorio..., por ultimo para corroborar la ejecucion del diseño realizado en pygubu (comando f5), se llamaron los values o valores de radiobutton "var" (builder) para que al efectuar un evento del boton (pulsacion) imprimiese por consola el valor asignado. Tenga en cuenta que el radiobutton1 ó suma fue seleccionado por defecto __self.radiobutton1.invoke()__     


![simple_version_gui_pygubu](https://github.com/JorgeAPinzon/Utils/assets/159712640/80284745-f40d-4fc3-862c-6825be65fb4d)



