class Alumno:
    def __init__(self, nombre:str,nota:int) -> None:
        self.nombre = nombre
        self.nota = nota
    def mostrar_datos(self):
        print(f'El alumno {self.nombre}, terminó el curso con la nota {self.nota}.')

