# FilesToRoot
Este script combinado con el explorador de Windows te permite que mediante una opción del menú contextual de un directorio puedas extraer todos los archivos de video o subtítulos de tus subdirectorios y moverlos al directorio desde donde ejecutaste el script.

# Requisitos

* [Python3](https://www.python.org/downloads/).
* Tkinter Module

# Funcionamiento

El script a raiz de un directorio dado (directorio raiz), recorre todos sus subdirectorios, si existe un archivo cuya extensión sea:
* .rar
* .zip
* .mp4
* .mkv
* .srt

En mi caso son esos, editando el codigo puedes expresar los que te interesen, ya que esta todo comentado en el script.

Mueve ese archivo al directorio raíz, si dicha acción no fuera posible, quizás la propiedad ```ReadOnly``` está activa por lo que se elimina. Posteriormente se borran los directorios, pero si tamaño del directorio es superior a 300MB no se borrará dado que interpretará que algún archivo no se movió satisfactoriamente.

Una pequeña demostración:

<p align="center"><img src="http://g.recordit.co/EFqpGmOTdc.gif"></p>

Ante cualquier cambio en el código, eres libre de hacerlo.


# Añadir al menú contextual y ejecutarlo con el explorador de Windows

1. Abrir el menú de ejecutar con el atajo de teclado ```Windows+R``` y tecleando en él ```regedit.exe```.
2. Una vez tengamos abierto el editor de registro, nos desplazamos hasta la siguiente ruta:
    ```HKEY_CLASSES_ROOT\Directory\Background\shell```
3. Una vez aquí, pulsamos con el botón derecho sobre «shell» y en el menú contextual que nos aparece seleccionaremos ```Nuevo > Clave```. Le damos el nombre que queramos en mi caso ```FilesToRoot```
4. Ahora, sobre Firefox volvemos a hacer clic con el botón derecho y a seleccionar «Nuevo > Clave«. A esta nueva clave la llamaremos «command» y, por defecto, tendrá un nuevo valor Predeterminado. Hacemos doble clic sobre él y, en esta ocasión, introducimos el comando que se ejecutará, se debe poner esto ```C\ruta\a\python.exe "C\Ruta\a\FilesToRoot.py" "%V"```

Un ejemplo del comando anterior sería: ```C:\Users\Jorge\AppData\Local\Programs\Python\Python39\python.exe "C:\Scripts\Python Scripts\FilesToRoot\FilesToRoot.py" "%V"```

**Se debe mantener el formato del comando, el intérprete (python) sin comillas, el script entre comillas dobles seguido de ```"%V"```**

El resultado de los pasos anteriores deberia quedar tal que así:
<p align="center"><img src = "https://i.ibb.co/NCGTzMC/filestoroot.png"></p>

Estos cambios se realizan instantáneamente, así que tan pronto lo hagamos tendremos ya la opción disponible, clicando con el botón derecho en cualquier lugar a una carpeta.

## Author ✒️

* **Jorge Manuel Lozano Gómez**
