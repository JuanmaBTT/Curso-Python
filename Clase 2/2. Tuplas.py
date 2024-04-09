mi_tupla = (2, 3, 10, 11)

print(type(mi_tupla))

mi_tupla_2 = (2,)

print(type(mi_tupla_2))


mi_tupla_3 = ()

print(type(mi_tupla_3))

 
cuenta = mi_tupla.count(2)

print(cuenta)

 
print(mi_tupla[2])

mi_tupla_lista = list(mi_tupla)

mi_tupla_lista[-1] = 22

mi_tupla = tuple(mi_tupla_lista)

print(mi_tupla)

