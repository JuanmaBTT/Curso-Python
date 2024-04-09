def mi_decorador(funcion):
    def envoltorio():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return envoltorio

@mi_decorador
def saludar():
    print("¡Saludos!")


saludar()