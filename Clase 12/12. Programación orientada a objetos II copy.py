class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    def __str__(self) -> str:
        return f"{self.nombre}: ${self.precio:.2f}"
    
    def __repr__(self) -> str:
        return f"Producto(nombre:'{self.nombre}', precio:{self.precio:.2f})"
    
class Pedido:
    lista_de_pedidos: list[Producto] = []
    def __init__(self) -> None:
        self.pedidos: list[Producto] = []
    def agregar_producto(self, *args: Producto):
        for producto in args:
            self.pedidos.append(producto)
            Pedido.lista_de_pedidos.append(producto)
producto1 = Producto("Camisa", 100)
producto2 = Producto("Camisa blanca", 100)
producto3 = Producto("Pantalón", 50)
producto4 = Producto("Pantalón vestir", 250)
tienda_A = Pedido()
tienda_B = Pedido()
tienda_A.agregar_producto(producto2, producto4)
tienda_B.agregar_producto(producto1, producto3)
print(Pedido.lista_de_pedidos)
print(tienda_A.pedidos)
print(tienda_B.pedidos)

# Crea un programa que consista en una clase Población.
# Tendrá como atributos a "ciudad" y "población",
# y una variable de clase "población_total"
# que será una lista que guardará cada objeto de Población
# en el mismo momento en que es instanciado.
# 1. Crear las instancias de la clase Población
# 2. Imprimir la información de las instancias creadas
# 3. Imprimir la información de la variable población_total
# 4. Crear un método ver_población_total que itere sobre la lista para
# mostrar la información ciudad por ciudad
# Invocar el método ver_población_total

class Poblacion:
    poblacion_total = []
    def __init__(self, ciudad, poblacion) -> None:
        self.ciudad = ciudad
        self.poblacion = poblacion
        Poblacion.poblacion_total.append(self)
    def __str__(self) -> str:
        return f"La ciudad de {self.ciudad} tiene una población de {self.poblacion} habitantes"
    
    @classmethod
    def ver_poblacion_total(cls):
        for ciudad in cls.poblacion_total:
            print(ciudad)
lima = Poblacion(ciudad="Lima, Perú", poblacion=9_000_000)
mexico = Poblacion(ciudad="Ciudad de México, México", poblacion=120_000_000)
# print(lima)
Poblacion.ver_poblacion_total()

class Vehiculo1:
    def __init__(self, modelo, potencia) -> None:
        self.modelo= modelo
        self.motor = self.Motor(potencia)
    class Motor:
        def __init__(self, potencia) -> None:
            self.potencia = potencia
mi_auto = Vehiculo1(modelo="Mustang", potencia=5000)
print(mi_auto.modelo)
print(mi_auto.motor.potencia)

class Motor:
    def __init__(self, cilindrada) -> None:
        self.cilindrada = cilindrada
    def encender(self):
        print("Motor encendido...")
    def apagar(self):
        print("Motor apagado.")
class Vehiculo:
    def __init__(self, modelo, cilindrada) -> None:
        self.modelo = modelo
        self.motor = Motor(cilindrada)
    def arrancar(self):
        print("Arrancando el auto...")
        self.motor.encender()
    def parar(self):
        print("Parando el auto...")
        self.motor.apagar()
mi_auto = Vehiculo("Ford Mustang", 5000)
mi_auto.arrancar()
mi_auto.parar()
