per_juan = {"dni": 123, "nombres": "Juan",
            "apellidos": "Brusco", "nacimiento": "1/1/2000", }

per_luis = {"dni": 888, "nombres": "Luis",
            "apellidos": "López", "nacimiento": "2/2/1990", }

usuarios = [{"persona": per_juan, "username": "jbrusco", "password": "admin123", },
            {"persona": per_luis, "username": "llopez", "password": "user123", },
            ]

# nacimiento_luis = usuarios[1]["persona"]["nacimiento"]
# print(f"Fecha de nacimiento de Luis:", nacimiento_luis)


from dataclasses import dataclass

@dataclass
class Persona:
    dni: int
    nombres: str
    apellidos: str
    nacimiento: str

@dataclass
class Usuario:
    username: str
    password: str
    persona: Persona

juan = Persona(123, "Juan", "brusco", "1/1/2000")
luis = Persona(888, "Luis", "López", "2/2/1990")

usuario_1 = Usuario("jbrusco", "admin123", juan)
usuario_2 = Usuario("llopez", "user123", luis)

# print(luis.nacimiento)

print(f"La persona {luis.apellidos.upper()}, {luis.nombres} nació el {luis.nacimiento}")
print(f"Su nombre de usuario es <{usuario_2.username}> y su password es <{usuario_2.password}>")
print()
print("Otra forma de ver a esta persona es haciendo:")
print(f"{usuario_2.persona.apellidos}, {usuario_2.persona.nombres}, {usuario_2.username}, {usuario_2.password}")