class Tarea:
    def __init__(self, titulo, completada=False):
        self.titulo = titulo
        self.completada = completada

    def marcar_como_completada(self):
        self.completada = True