class Persona:
    def __init__(self, nombres: str, apellidos: str):
        self.nombres = nombres
        self.apellidos = apellidos

    def nombre_completo(self) -> None:
        print(f"{self.apellidos}, {self.nombres}")


class Cliente(Persona):
    def __init__(self, nombres: str, apellidos: str, telefono: str):
        super().__init__(nombres, apellidos)
        self.telefono = telefono


persona = Persona(nombres="Guillermo Guillermino", apellidos="González")

cliente = Cliente(nombres="Guillermo Guillermino", apellidos="González",
                  telefono="123456789")

cliente.nombre_completo()
