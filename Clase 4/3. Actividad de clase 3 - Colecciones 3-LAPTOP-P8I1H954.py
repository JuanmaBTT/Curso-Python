"""
Descripción de la actividad. 

Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}. 

Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar. 

En el caso de ingresar una divisa no existente en nuestro diccionario, deberemos indicarle con un mensaje de notificación que la divisa no se encuentra disponible. 

"""
divisa = {'Dolar':'$','Euro':'€', 'Libra':'£'}

"""divisa.keys()
divisas_posibles = divisa.keys()
print(*divisas_posibles)
divisa.values()
values_posibles = divisa.values()
print(*values_posibles)"""
consulta_de_divisa = input("¿Qué divisa se quiere visualizar?").strip().capitalize()
valor= divisa.get(consulta_de_divisa)
if not valor : print("La divisa no se encuentra disponible")
else : print( f'La divisa {consulta_de_divisa} tiene el símbolo {valor}.')

"""""
# Creamos el diccionario de divisas
divisas = {'Dolar': '$', 'Euro': '€', 'Libra': '£'}

# Solicitamos al usuario que ingrese la divisa
entrada = input("Ingresa la divisa que deseas visualizar: ").strip().capitalize()

# Buscamos la divisa en el diccionar y la imprimimos
valor = divisas.get(entrada)
print(f"La divisa {entrada} tiene el símbolo {valor}")"""