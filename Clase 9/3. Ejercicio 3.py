def promediar(*args):
    resultado = sum(args)/(len(args))
    return resultado

resultado = promediar(1, 2, 3, 5, 7, 12, 19, 23.434)
print(resultado)


x = promediar(5)
y = promediar(5, 7)
z = promediar(5, 7, 10, 9)

lista_promedios = [x, y, z]

for elemento in lista_promedios:
    print(f"El promedio es {elemento:.1f}")

def datos_personales(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


datos_personales(email="email@mi_casilla.com", telefono=1234)

