class Empleado:
    def __init__(self, especialidad, seguro, salario) -> None:
        self.especialidad = especialidad
        self.seguro = seguro
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, valor):
        self.__salario = valor

    def enviar_email(self):
        print("Enviando email de empleado")

class EmpleadoJefe(Empleado):
    def __init__(self, especialidad, seguro, salario, salario_vip) -> None:
        super().__init__(especialidad, seguro, salario)
        self.__salario = salario_vip

empleado_1 = Empleado("albañil", True, 1000)
# print(empleado_1.__salario)
print(empleado_1.get_salario())
# empleado_1.__salario = 1500
# print(empleado_1.__dict__)
empleado_1.set_salario(1500)
# print(empleado_1.__dict__)

empleado_2 = EmpleadoJefe("maestro", True, 1000, 200)
print(empleado_2.__dict__)
