from modelos.tarea import Tarea
from vistas.ventana import VentanaTareas

class ControladorTareas:
    def __init__(self):
        self.tareas = []
        self.ventana = VentanaTareas(self)

    def agregar_tarea(self, titulo):
        nueva_tarea = Tarea(titulo)
        self.tareas.append(nueva_tarea)
        self.ventana.mostrar_tareas(self.tareas)

    def editar_tarea(self, indice, nuevo_titulo): 
        if 0 <= indice < len(self.tareas) and nuevo_titulo: 
            self.tareas[indice].editar_titulo(nuevo_titulo) 
            self.ventana.mostrar_tareas(self.tareas)

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            self.ventana.mostrar_tareas(self.tareas)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
            self.ventana.mostrar_tareas(self.tareas)

    def iniciar(self):
        self.ventana.iniciar()