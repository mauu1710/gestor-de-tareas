**Gestor de Tareas:**

Este proyecto fue desarrollado para la Actividad 1 de la Unidad 2, y aplica el patrón de diseño Singleton para la configuración global de la aplicación (por ejemplo, el modo debug).


Esta actividad en resumen nos permite agregar tareas nuevas, listarlas, marcarlas como completadas, y guarda todo automáticamente en un archivo JSON para que nada se pierda al cerrar el programa.


**Estructura del proyecto:**

config.py —> clase Config, esta clase fue implementada como Singleton, para el modo debug y el nombre del archivo de datos.

gestor.py —> clase GestorTareas, cumple con la lógica de agregar, listar, completar y guardar/cargar tareas en JSON.

main.py —> es la interfaz de nuesrto proyecto (el menú que ve el usuario).

test\_gestor.py —> son las pruebas unitarias hechas con unittest.

tareas.json —> este json se genera solo al usar la aplicación (no viene incluido en el repositorio).


**Cómo ejecutarlo:**

Para ejecutarlo, solamente necesitamos tener Python.

Para correr la aplicación normal:

bash
python3 main.py

Para correr la aplicación con el modo debug activado (muestra mensajes extra de lo que va pasando internamente):

bash
python3 main.py debug


Una vez adentro, se muestra el menu de main.py


**Cómo correr las pruebas unitarias:**

bash
python3 -m unittest test\_gestor -v


Las pruebas cubren lo siguiente: que se agreguen tareas correctamente, que los ids sean consecutivos, que no se pueda agregar una tarea vacía, que se puedan marcar tareas como completadas, que el guardado y la carga del JSON funcionen, y que Config efectivamente se comporte como Singleton.

