"""
Crear 2 clases:
    - Libro
        - titulo
        - autor
        - año
    
    - Biblioteca
        - nombre
        - libros: list[Libro]
        - agregar_libro()
        - eliminar_libro()
        - listar_libros()
"""
class Libro:

    def __init__(self, titulo, autor, año) -> None:

        self.titulo = titulo

        self.autor = autor

        self.año = año

class Biblioteca:

    def __init__(self, nombre) -> None:

        self.nombre = nombre

        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro):

        self.libros.append(libro)

    def eliminar_libro(self, libro: Libro):

        self.libros.remove(libro)

    def listar_libros(self):

        print(f"Libros en la biblioteca: '{self.nombre}':")

        for libro in self.libros:

            print(f"{libro.titulo} de {libro.autor} ({libro.año})")

# Creamos algunos objetos Libro

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

libro2 = Libro("1984", "George Orwell", 1949)

libro3 = Libro("Órganon", "Aristóteles", -384)

# Creamos un objeto Biblioteca y agregamos libros

mi_biblioteca = Biblioteca("Mi Biblioteca")

mi_biblioteca.agregar_libro(libro1)

mi_biblioteca.agregar_libro(libro2)

mi_biblioteca.agregar_libro(libro3)

# Listamos los libros

mi_biblioteca.listar_libros()

# Eliminamos un libro

mi_biblioteca.eliminar_libro(libro2)

# Listamos los libros

mi_biblioteca.listar_libros()