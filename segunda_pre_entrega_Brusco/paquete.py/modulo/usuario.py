"""
Sugerencias
La Clase Cliente debe tener mínimo 4 atributos y 2 métodos.
Se debe utilizar el método __str__() para darle nombre a los objetos.
Es opcional el uso de herencia.
"""
#Sugiero seleccionar (Alt+Z) para una mejor lectura. Para agregarle complejidad a la entrega importamos datetime para solicitar fecha de nacimiento a la persona.

from datetime import datetime

class Persona:
    """Clase para crear clientes"""
    #Constructor de la clase
    def __init__(self,nombre:str,apellido:str,fecha_de_nacimiento:datetime,documento_de_identidad:str,pais_de_origen:str,direccion:str):
    
        #Atributos de la instancia
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento.strftime("%d/%m/%Y")
        self.documento_de_identidad = documento_de_identidad
        self.pais_de_origen = pais_de_origen
        self.direccion = direccion
    #Método que devuelve la representación de Persona.
    def __str__(self):
        return f'El nombre es: {self.nombre} y el usuario es:{self.documento_de_identidad}'


class Cliente(Persona):

    #Variable de clase

    lista_de_clientes: list["Cliente"] = []

    """Cliente hereda los métodos y atributos de Persona y añade email y password"""

    #Con super() accedemos a los métodos y atributos de la clase Padre, que es Persona.
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: datetime, documento_de_identidad: str, pais_de_origen: str, direccion: str,email:str,password:str):
        super().__init__(nombre, apellido, fecha_de_nacimiento, documento_de_identidad, pais_de_origen, direccion)

        #Atributos de la instancia
        self.email = email
        self.password = password
        Cliente.lista_de_clientes.append(self)
    
    #Método que devuelve la representación de Cliente.
    def __str__(self):
        return f'Usuario: {self.documento_de_identidad}, Nombre: {self.apellido},{self.nombre}, Fecha de nacimiento: {self.fecha_de_nacimiento}'
    def __repr__(self):
        return f'Usuario: {self.documento_de_identidad}, Nombre: {self.apellido},{self.nombre}, Fecha de nacimiento: {self.fecha_de_nacimiento}'