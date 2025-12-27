# modelo.py
class Tarea:
    def __init__(self, titulo, completada=False):
        self.titulo = titulo
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def editar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
