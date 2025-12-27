import tkinter as tk

class VentanaTareas:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Gestor de Tareas")

        #Entrada de texto para nueva tarea
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=5)

        #Botón para agregar tarea
        self.btn_agregar = tk.Button(self.root, text="Agregar Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack(pady=5)

        #Lista para mostrar tareas
        self.lista_tareas = tk.Listbox(self.root, width=50, height=15)
        self.lista_tareas.pack(pady=5)

        #Botón para completar tarea
        self.btn_completar = tk.Button(self.root, text="Marcar como Completada", command=self.completar_tarea)
        self.btn_completar.pack(pady=5)

        #Boton para modificar tarea
        self.btn_modificar = tk.Button(self.root, text="Editar Tarea", command=self.editar_tarea)
        self.btn_modificar.pack(pady=5)

        #Botón para eliminar tarea
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=5)

    def agregar_tarea(self):
        titulo = self.entry.get()
        if titulo:
            self.controlador.agregar_tarea(titulo)
            self.entry.delete(0, tk.END)

    def completar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.controlador.completar_tarea(indice)

    def mostrar_tareas(self, tareas):
        self.lista_tareas.delete(0, tk.END)
        for idx, tarea in enumerate(tareas):
            estado = "✓" if tarea.completada else "✗"
            self.lista_tareas.insert(tk.END, f"{idx + 1}. [{estado}] {tarea.titulo}")

    def editar_tarea(self): 
        seleccion = self.lista_tareas.curselection() 
        nuevo_titulo = self.entry.get() 
        if seleccion and nuevo_titulo: 
            indice = seleccion[0] 
            self.controlador.editar_tarea(indice, nuevo_titulo) 
            self.entry.delete(0, tk.END)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.controlador.eliminar_tarea(indice)
    
    def iniciar(self):
        self.root.mainloop()