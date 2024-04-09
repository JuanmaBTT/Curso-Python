"""Descripción de la actividad. 

Para aprobar un crédito, el cliente debe ser mayor de edad. Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.  En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. Si no cumple ninguna de las condiciones, no se aprueba el crédito

Datos iniciales
edad = 15
antigüedad = 10
ingreso = 1500
"""

edad = 15
antigüedad = 10
ingreso = 1500

cliente_mayor_de_edad=edad>18

print("¿El cliente es mayor de edad?",cliente_mayor_de_edad)

cliente_antiguedad_sistema_financiero=antigüedad>=3

print("¿El cliente presenta una antiguedad de al menos 3 años en el sistema financiero?",cliente_antiguedad_sistema_financiero)

cliente_ingresos_1=ingreso>=2500

print("¿El cliente presenta un ingreso mayor a 2.500 USD?",cliente_ingresos_1)

cliente_ingresos_2=ingreso>=4000

print("¿El cliente presenta un ingreso mayor a 4.000 USD?",cliente_ingresos_2)

###Resultado: 

if cliente_mayor_de_edad and cliente_antiguedad_sistema_financiero and cliente_ingresos_1 :
    print("Se concede el prestamo")
elif cliente_mayor_de_edad and cliente_ingresos_2 :
    print("Se concede el prestamo")
else : print("No se concede el préstamo")

"""Otra forma:"""

# Ingreso de datos
edad = int(input("Edad: "))
antigüedad = int(input("Antigüedad: "))
ingresos = float(input("Ingresos mensuales: "))

# Operaciones
mayor_edad = (edad >= 18)
condición_1 = (mayor_edad and antigüedad >=3 and ingresos > 2500)
condición_2 = (mayor_edad and antigüedad < 3 and ingresos >= 4000)

# Salida de datos
if condición_1 or condición_2:
    print("Crédito aprobado")
else:
    print("Crédito denegado")