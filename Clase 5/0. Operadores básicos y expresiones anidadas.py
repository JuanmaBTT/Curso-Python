# Calcular mentalmente el resultado de cada expresión.
# Almacenarlo en una nueva lista que contendrá únicamente valores lógicos True y False.
# False == True
# 10 >= 2 * 4
# 33 / 3 == 11
# True > False
# True * 5 == 2.5 * 2

print([
False == True,
10 >= 2 * 4,
33 / 3 == 11,
True > False,
True * 5 == 2.5 * 2
])

""" Solución del Profe"""
expresiones = [
    False == True,
    10 >= 2 * 4,
    33 / 3 == 11,
    True > False,
    True * 5 == 2.5 * 2,
]

print(expresiones)

expresion_1 = False == True
expresion_2 = 10 >= 2 * 4
expresion_3 = 33 / 3 == 11
expresion_4 = True > False
expresion_5 = True * 5 == 2.5 * 2

expresiones_lista = (expresion_1, expresion_2, expresion_3, expresion_4, expresion_5)
print(expresiones_lista)
