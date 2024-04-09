"""
Crear los parámetros que faltan
permisos debe ser por defecto False
invocar la función con argumentos por nombre

"""


"""
Lo que hice:

def login(user: str, password:str, permisos=False):
    print(user)
    print(password)
    if permisos:
        print("Sí tiene permisos de administrador")
    else:
        print("Acceso denegado")

def user():
    return input("Indique nombre de usuario: ")

def password():
    return input("Indique su contraseña: ")

"""
### La del profe:

def login(user: str, password: str, permisos=False):
    print(user)
    print(password)
    if permisos:
        print("Sí tiene permisos de administrador")
    else:
        print("Acceso denegado")


# login("Bruno", "pinkvenom4")
# login(user="Bruno", password="pinkvenom4", permisos=True)
# login(user="Bruno", password="pinkvenom4", permisos=False)
login(user="Bruno", password="pinkvenom4")

def sumar(*args):
    resultado = sum(args)
    return resultado


resultado = sumar(1, 2, 3, 5, 7, 12, 19, 23.434)
print(resultado)