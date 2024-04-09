#Mensaje de Bienvenida
print ("-" * 30)

saludo_bienvenida = "    **** Bienvenido! ****"
print(saludo_bienvenida)
print ("-"*30)

#Ingresar Datos
nombre = input("¿Cuál es tu nombre?")
edad = input ("¿Cuántos años tienes?")

#Mostrar Datos
resultado = nombre + " tiene " + edad + " años"
print(resultado)

#Mostrar Datos / Otra Forma
print(nombre, "tiene", edad, "años")

#Tipos
edad = 28
print(type(edad))
temperatura = 38.5
print(type(temperatura))

#Redondear
temperatura_2 = round(temperatura,0)
print (temperatura_2)
print(type(temperatura_2))
print (int(temperatura_2))
print(type(int((temperatura_2))))

#Fórmulas
import math
PI= math.pi
print (PI)

#IDs para saber el identificador de cada variable
print(id(PI))
print(id(nombre))
print(id(edad))
print(id(temperatura))
print(id(temperatura_2))

#
