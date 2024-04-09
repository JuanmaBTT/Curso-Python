#Importamos del módulo "usuario.py" la clase Cliente. A su vez, de datetime y pprint a estas mismas clases, para tener sus funcionalidades. 
from modulo.usuario import Cliente
from datetime import datetime
from pprint import pprint

# Creación de Objetos, instanciamos la clase Cliente:
juan = Cliente("Juan","Brusco",datetime.strptime("21/05/2017","%d/%m/%Y"),"16021604","Uruguay","Matías Britos 1514","juanma666@gmail.com","hola")
pau = Cliente("Paula","Unzurrunzaga",datetime.strptime("21/05/2017","%d/%m/%Y"),"25082811","Uruguay","Mauricio Bruto 1414","paulita@gmail.com","123")
veronica = Cliente("Verónica","Parodi",datetime.strptime("16/08/1950","%d/%m/%Y"),"31032612","Uruguay","Luis Pierda 567","vero987@gmail.com","987")
fernando = Cliente("Fernando","Brusco",datetime.strptime("31/03/1960","%d/%m/%Y"),"23041107","Uruguay","Julio Cesar 555","fercho555@gmail.com","555")

#En un formato más cómodo para leer, con pprint, visualizamos un resumen de la lista de clientes con 4 atributos de cada cliente.'Usuario: {self.documento_de_identidad}, Nombre: {self.apellido},{self.nombre}, Fecha de nacimiento: {self.fecha_de_nacimiento}'

pprint(Cliente.lista_de_clientes)