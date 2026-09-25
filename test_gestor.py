

import json
import os
import unittest

from config import Config
from gestor import GestorTareas


class TestGestorTareas(unittest.TestCase):

    ARCHIVO_PRUEBA = "tareas_test.json"

    def setUp(self):
        Config._instancia = None
        Config(debug=False, archivo_datos=self.ARCHIVO_PRUEBA)
        self.gestor = GestorTareas()

    def tearDown(self):
        if os.path.exists(self.ARCHIVO_PRUEBA):
            os.remove(self.ARCHIVO_PRUEBA)
        Config._instancia = None

    def test_agregar_tarea_incrementa_la_lista(self):
        self.gestor.agregar_tarea("Comprar despensa")
        self.assertEqual(len(self.gestor.listar_tareas()), 1)

    def test_agregar_tarea_asigna_id_consecutivo(self):
        t1 = self.gestor.agregar_tarea("Tarea 1")
        t2 = self.gestor.agregar_tarea("Tarea 2")
        self.assertEqual(t1["id"], 1)
        self.assertEqual(t2["id"], 2)

    def test_agregar_tarea_vacia_lanza_error(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("   ")

    def test_tarea_nueva_no_esta_completada(self):
        tarea = self.gestor.agregar_tarea("Lavar el carro")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea_existente(self):
        tarea = self.gestor.agregar_tarea("Estudiar para el examen")
        resultado = self.gestor.completar_tarea(tarea["id"])
        self.assertTrue(resultado)
        self.assertTrue(self.gestor.listar_tareas()[0]["completada"])

    def test_completar_tarea_inexistente_regresa_false(self):
        resultado = self.gestor.completar_tarea(999)
        self.assertFalse(resultado)

    def test_las_tareas_se_guardan_en_json(self):
        self.gestor.agregar_tarea("Pagar el internet")
        with open(self.ARCHIVO_PRUEBA, "r", encoding="utf-8") as f:
            datos = json.load(f)
        self.assertEqual(len(datos), 1)
        self.assertEqual(datos[0]["descripcion"], "Pagar el internet")

    def test_las_tareas_se_cargan_al_reiniciar_el_gestor(self):
        self.gestor.agregar_tarea("Tarea que debe seguir")
        gestor_nuevo = GestorTareas()
        self.assertEqual(len(gestor_nuevo.listar_tareas()), 1)
        self.assertEqual(gestor_nuevo.listar_tareas()[0]["descripcion"], "Tarea que debe seguir")

    def test_config_es_singleton(self):
        config_a = Config()
        config_b = Config()
        self.assertIs(config_a, config_b)


if __name__ == "__main__":
    unittest.main()
