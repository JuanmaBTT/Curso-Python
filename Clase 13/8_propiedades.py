class Empleado:
    def __init__(self, especialidad, seguro, salario) -> None:
        self.especialidad = especialidad
        self.seguro = seguro
        self.__salario = salario

    @property
    def salario(self):  # propiedad
        return self.__salario

    @salario.getter     # GETTER (función de la propiedad salario)
    def salario(self):
        if self.__salario == 0:
            return "No tiene salario asignado"
        else:
            return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor >= 0:
            self.__salario = valor
        else:
            raise ValueError("El valor debe ser igual o superior a 0")

    def enviar_email(self):
        print("Enviando email de empleado")


empleado_1 = Empleado("albañil", True, 1000)
print(empleado_1.salario)
# empleado_1.__salario = 1500
# print(empleado_1.__dict__)
empleado_1.salario = 0
print(empleado_1.salario)
empleado_1.salario = 2000
print(empleado_1.salario)
empleado_1.salario = -10
print(empleado_1.salario)



