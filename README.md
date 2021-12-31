## Paso 1: Deste tu línea de comandos elige una carpeta donde albergar el proyecto
**Puede ser el home (~) o puedes crear otra carpeta para almacenarlo dentro de este.
**
*Puedes posicionarte directamente a tu directorio "Home" en cualquier momento con:*

	cd


## Paso 2: En la carpeta para el proyecto haz un clon del repositorio
Si no tienes una llave SSH configurada puedes usar la url HTTPS

*https://github.com/manuel-wh/refugio.git*

Si cuentas con tus llaves SSH:

*git@github.com:manuel-wh/refugio.git*

*Solo reemplaza la url por la indicada*

	git clone <url>

Después ingresa a la carpeta del proyecto.

	cd refugio

## Paso 3: Crear entorno virtual en la carpeta del proyecto
Asegurate de tener instalado el entorno virtual de Python `virtualenv`

	which virtualenv
Si no lo tienes instalado ejecuta:

	pip install virtualenv
Ahora crearemos el entorno virtual.

	virtualenv <nombre_de_tu_entorno>

Verifica que lo instalaste con la version 2.7 de Python

    python -V

Puedes usar este comando para instalar el entorno  con la versión que tú le especifíques.

	virtualenv -p /usr/bin/python2.7 <nombre_de_tu_entorno>


## Paso 4: Activar y desactivar el entorno
##### Para activar el entorno ingresamos a la carpeta en la que se creo el entorno y escribimos:

    source bin/activate
Si aparece un texto entre parentesis en tu linea de comandos es que lograste ingresar:

`(venv) usuario@usuario:~/refugio/venv$`
##### Para salir del entorno virtual soilo escribe
    deactivate

## Paso 5: instalamos dependencias con el entorno iniciado
    pip install  -r requeriments.txt

## Paso 6: Crear migraciones desde la carpeta del proyecto
    ./runserver makemigrations
## Paso 7: Hacer la migracion
    ./runserver migrate
## Paso 8: Iniciar el proyecto:
    ./manage.py runserver
## Paso 9: Para desactivar el proyecto:
    Ctrl+c
