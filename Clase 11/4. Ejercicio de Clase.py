"""
Crear una clase llamada Usuario.
Debe tener 2 variables de instancia: username y password
Solicitar al usuario los datos por input()
Crear una instancia de la clase Usuario
Imprimir los atributos de la instancia
"""

username = input("¿Cual es tu nombre de usuario?:")
password = input("¿Cual es tu contraseña?:")

class Ingreso:
    def __init__(self, username: str, password: str):  # método o constructor
        self.username = username  # atributo / variable de instancia
        self.password = password  # atributo / variable de instancia

usuario = Ingreso(username, password)
# ☝🏻 objeto. Instancia de la clase Persona
print(usuario.username,usuario.password)