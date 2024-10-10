# Malackathon App

## Ficheros y directorios

- `run.sh`. Script maestro para el mantenimiento y lanzamiento de la aplicación. Ejecutar `./run.sh -h` para ver un
  mensaje de ayuda.
- `configuration.yml`. Configuración en YAML de la aplicación.
- `requirements.txt`. Fichero de las dependencias de python.
- `app`. Módulo python de la aplicación.
    - `__init__.py`. Script de inicialización del módulo.
    - `__main__.py`. Ejecutable principal.
    - `ddbb`. Submódulo con los componentes de conexión a base de datos.
    - 