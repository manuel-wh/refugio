## Paso 1: Deste tu línea de comandos elige una carpeta donde albergar el proyecto
**Puede ser el home (~) o puedes crear otra carpeta para almacenarlo dentro de este.
**
*Puedes posicionarte directamente a tu directorio "Home" en cualquier momento con:*

```bash
$ cd
```


## Paso 2: En la carpeta para el proyecto haz un clon del repositorio
Si no tienes una llave SSH configurada puedes usar la url HTTPS
*https://github.com/manuel-wh/refugio.git*

Si cuentas con tus llaves SSH:
*git@github.com:manuel-wh/refugio.git*

*Solo reemplaza la url por la indicada*

    $ git clone <url>

## Paso 3: Crear entorno en la carpeta para el entorno
    mkvirtualenv refugioenv -p=2.7
#### Confirmar que sea en python 2.7
    python -V
## Paso 4: Desactivar e iniciar entorno
#### Para desactivar podemos hacer:
    deactivate
#### Para iniciar podemos hacer
    workon refugioenv
#### o estando en la carpeta del entorno
    source bin/activate
## Paso 5: instalamos dependencias con el entorno iniciado
    pip install  -r requeriments.txt
## Paso 6: Crear base de datos
    sudo -u postgres createdb refugio
## Paso 7: Crear usuario y dar privilegios en postgresql:
    sudo -u postgres psql template1
    CREATE USER refugio WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE refugio to refugio;
    \c refugio
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO refugio;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO refugio;
#### para salir usar:
    \q
## Paso 8: Crear migraciones desde la carpeta del proyecto
    ./runserver makemigrations
## Paso 9: Hacer la migracion
    ./runserver migrate
## Paso 10: Iniciar el proyecto:
    ./manage.py runserver
## Paso 11: Para desactivar el proyecto:
    Ctrl+c
