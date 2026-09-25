
import sys

from config import Config
from gestor import GestorTareas


def mostrar_menu():
    print("\n Gestor de Tareas:")
    print("1. Agregar tarea/s")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")


def imprimir_tareas(tareas):

    if len(tareas) == 0:
        print("No hay tareas registradas todavia.")
        return
    for t in tareas:
        estado = "[X]" if t["completada"] else "[ ]"
        print(f"{estado} #{t['id']} - {t['descripcion']} (creada: {t['fecha_creacion']})")


def main():
    # si se corre el programa como "python3 main.py debug" se activa el modo debug
    modo_debug = "debug" in sys.argv
    Config(debug=modo_debug, archivo_datos="tareas.json")


    gestor = GestorTareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            descripcion = input("Descripcion de la nueva tarea: ")
            try:
                tarea = gestor.agregar_tarea(descripcion)
                print(f"Tarea agregada con el id {tarea['id']}")
            except ValueError as error:
                print(f"No se pudo agregar la tarea: {error}")


        elif opcion == "2":
            imprimir_tareas(gestor.listar_tareas())


        elif opcion == "3":
            id_texto = input("Id de la tarea a completar: ").strip()
            if id_texto.isdigit():
                exito = gestor.completar_tarea(int(id_texto))
                if exito:
                    print("Tarea marcada como completada.")
                else:
                    print("No existe una tarea con ese id.")
            else:
                print("Escriba un numero de id valido.")

        elif opcion == "4":
            print("Cerrando la aplicacion. Tareas guardadas en tareas.json")
            break

        else:
            print("Opcion no reconocida, intenta de nuevo.")


if __name__ == "__main__":
    main()
