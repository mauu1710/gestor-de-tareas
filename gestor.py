"""
Logica de la aplicacion: agregar tareas, listarlas, marcarlas como
completadas, y guardarlas/cargarlas de un archivo JSON.
"""

import json
import os
from datetime import datetime

from config import Config


class GestorTareas:

    def __init__(self):

        self.config = Config()  
        self.tareas = []
        self.cargar_tareas()


    def agregar_tarea(self, descripcion):
        if not descripcion or not descripcion.strip():
            raise ValueError("La descripcion de la tarea no puede estar vacia")


        tarea = {
            "id": self._siguiente_id(),
            "descripcion": descripcion.strip(),
            "completada": False,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.tareas.append(tarea)

        if self.config.debug:
            print(f"[DEBUG] tarea agregada -> {tarea}")

        self.guardar_tareas()
        return tarea

    def listar_tareas(self):
        return self.tareas

    def completar_tarea(self, id_tarea):

        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                if self.config.debug:
                    print(f"[DEBUG] tarea {id_tarea} marcada como completada")
                self.guardar_tareas()
                return True
        return False

    def _siguiente_id(self):
        if len(self.tareas) == 0:
            return 1
        ids_existentes = []
        for tarea in self.tareas:
            ids_existentes.append(tarea["id"])
        return max(ids_existentes) + 1


    def guardar_tareas(self):
        with open(self.config.archivo_datos, "w", encoding="utf-8") as f:
            json.dump(self.tareas, f, ensure_ascii=False, indent=2)


    def cargar_tareas(self):
        ruta = self.config.archivo_datos
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                try:
                    self.tareas = json.load(f)
                except json.JSONDecodeError:
                   
                    self.tareas = []
        else:
            self.tareas = []
