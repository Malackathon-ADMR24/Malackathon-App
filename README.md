# Malackathon App

## Ficheros y directorios

- `run.sh`. Script maestro para el mantenimiento y lanzamiento de la aplicación. Ejecutar `./run.sh -h` para ver un
  mensaje de ayuda.
- `configuration.yml`. Configuración en YAML de la aplicación.
- `requirements.txt`. Fichero de las dependencias de python.
- `app`. Módulo python de la aplicación.
    - `ddbb`. Submódulo con los componentes de conexión a base de datos.
    - `usecase`. Submódulo con las funciones de los casos de uso de la aplicación.
    - `domain`. Submódulo con las clases de dominio (entidades).
    - `templates`. Directorio con las plantillas HTML.
    - `controller.py`. Controlador HTTP para mapear URLs de la API a los casos de uso.
    - `__init__.py`. Script de inicialización del módulo principal.
    - `__main__.py`. Ejecutable principal.
