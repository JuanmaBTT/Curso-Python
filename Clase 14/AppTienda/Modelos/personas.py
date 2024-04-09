# Crear una clase Cliente con el atributo "nombre"

# Crear una clase Usuario que herede de Cliente

# Usuario tendrá 2 atributos: email y password


class Cliente:
    """Clase para crear clientes"""
    def __init__(self,nombre:str):
        self.nombre = nombre
    def __str__(self):
        return f'El nombre es: {self.nombre}'
class Usuario(Cliente):
    """Usuario hereda de cliente y tiene como atributos email y password"""
    def __init__(self, nombre, email:str, password:str):
        super().__init__(nombre)
        self.email = email
        self.password = password
    def __str__(self):
        return f'El usuario: {self.nombre}, cuyo email es: {self.email}'

#cliente = Usuario("Juan","juan@gmail.com","123")
#print(cliente)