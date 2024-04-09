per_juan = {
    "dni": 123,
    "nombres": "Juan",
    "apellidos": "Brusco",
    "nacimiento": "1/1/2000",
}
per_luis = {
    "dni": 888,
    "nombres": "Luis",
    "apellidos": "López",
    "nacimiento": "2/2/1990",
}
usuarios = [
    {
        "persona": per_juan,
        "username": "jbrusco",
        "password": "admin123",
    },
    {
        "persona": per_luis,
        "username": "llopez",
        "password": "user123",
    },
]
# from pprint import pprint
# pprint(usuarios)
nacimiento_luis = usuarios[1]["persona"]["nacimiento"]
print(f"Fecha de nacimiento de Luis:", nacimiento_luis)