class Perro:
    def __init__(self, su_nombre: str, su_edad: int) -> None:
        self.nombre = su_nombre
        self.edad = su_edad
        pasos = int(input("Dime cuántos pasos caminaré contigo: "))
        self.caminar(pasos)


    def presentarse(self) -> str:
        mensaje = f"Nombre: {self.nombre}. Edad: {self.edad}"
        return mensaje

    def caminar(self, pasos: int):  # método de instancia
        print(f"Soy {self.nombre}, y estoy caminando {pasos} pasos...")

perrito = Perro("Luna", 5)
# print(perrito.edad)
# perrito.caminar()
# mensaje = perrito.presentarse()
# print(mensaje)
# perrito.caminar(pasos=20)
