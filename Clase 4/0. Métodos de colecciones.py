cadena = " esta es una prueba con Pithon    🔥🔥  "

print("upper:", cadena.upper())
print("lower:", cadena.lower())
print("title:", cadena.title())
cadena_strip = cadena.strip()
print("strip:", cadena_strip, end="✨")  # 🔴 
print("capitalize:", cadena_strip.capitalize())
print("replace:", cadena.replace("Pithon", "Python"))
print("find:", cadena.find("a"))   # 🔴 
print("find:", cadena.find("A"))
print("startwith:", cadena.startswith(" esta"))   # 🔴 
print("count:", cadena.count("🔥"))
print("isdigit:", "1234".isdigit())  # 🔴 
print("isdigit:", "a1234".isdigit())
print("123Esta es una Prueba231".strip("123"))  # 🔴 

print(" Esta es una Prueba".strip().upper().replace("P", "p").find("a"))

cadena = " esta es una prueba con Pithon    🔥🔥  "

print("upper:", cadena.upper())
print("lower:", cadena.lower())
print("title:", cadena.title())
cadena_strip = cadena.strip()
print("strip:", cadena_strip, end="✨")  # 🔴 
print("capitalize:", cadena_strip.capitalize())
print("replace:", cadena.replace("Pithon", "Python"))
print("find:", cadena.find("a"))   # 🔴 
print("find:", cadena.find("A"))
print("startwith:", cadena.startswith(" esta"))   # 🔴 
print("count:", cadena.count("🔥"))
print("isdigit:", "1234".isdigit())  # 🔴 
print("isdigit:", "a1234".isdigit())
print("123Esta es una Prueba231".strip("123"))  # 🔴 

print(" Esta es una Prueba".strip().upper().replace("P", "p").find("a"))

# cadena_split = cadena.split("una")
cadena_split = cadena.split()
print(cadena_split)

cajón_de_frutas = ["limón", "palta", "sandía"]
frutas_juntas = " - ".join(cajón_de_frutas)
print(frutas_juntas)

# Crea una cadena de texto
texto = input("Ingresa una oración: ")
print(texto)

# Convertir el texto a una lista de palabras
palabras = texto.split()
print(palabras)

# Converitr la lista de palabras en un conjunto para eliminar duplicados
palabras_unicas = set(palabras)
print(palabras_unicas)

# Convertir el conjunto de palabras unicas en una lista
lista_palabras_unicas = list(palabras_unicas)
print(lista_palabras_unicas)
lista_palabras_unicas.sort()
# lista_palabras_unicas.sort(reverse=True)
print(lista_palabras_unicas)

conjunto = {"11", "22", "33"}
lista_palabras_unicas.extend(conjunto)
print(lista_palabras_unicas)
lista_palabras_unicas.insert(0, "hola")
print(lista_palabras_unicas)
lista_palabras_unicas.reverse()
print(lista_palabras_unicas)

# nueva_lista = lista_palabras_unicas
nueva_lista = lista_palabras_unicas.copy()
nueva_lista.append("10000")
print(lista_palabras_unicas)
print(nueva_lista)

# *** COPY & CLEAR
diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25, "vino": 100.00}

# diccionario_igual = diccionario
diccionario_copia = diccionario.copy()
diccionario_copia["fideos"] = 200.2

print(diccionario)
print(diccionario_copia)

# diccionario_copia = {}
diccionario_copia.clear()

print(diccionario)
print(diccionario_copia)

# *** KEYS & VALUES
print(diccionario.keys())
claves = diccionario.keys()
a, b, c, d = claves
print(a, b, c, d)
print(*claves)

print(diccionario.values())
valores = diccionario.values()
print(*valores)

# *** ITEMS
claves_valores = diccionario.items()
print(claves_valores)
a, b, c, d = diccionario.items()
print(a, b, c, d)
print(*a, *b, *c, *d)
producto = a[0]
precio = a[1]
print(f"{producto}: ${precio}")
print()

for clave, valor in diccionario.items():
    print(f"{clave}: ${valor}")


    # *** COPY & CLEAR
diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25, "vino": 100.00}

# diccionario_igual = diccionario
diccionario_copia = diccionario.copy()
diccionario_copia["fideos"] = 200.2

print(diccionario)
print(diccionario_copia)

# diccionario_copia = {}
diccionario_copia.clear()

print(diccionario)
print(diccionario_copia)

# *** KEYS & VALUES
print(diccionario.keys())
claves = diccionario.keys()
a, b, c, d = claves
print(a, b, c, d)
print(*claves)

print(diccionario.values())
valores = diccionario.values()
print(*valores)

# *** ITEMS
claves_valores = diccionario.items()
print(claves_valores)
a, b, c, d = diccionario.items()
print(a, b, c, d)
print(*a, *b, *c, *d)
producto = a[0]
precio = a[1]
print(f"{producto}: ${precio}")
print()

for clave, valor in diccionario.items():
    print(f"{clave}: ${valor}")

 # UPDATE
otro_dict = {"carne": 500, "verduras": 500}
diccionario.update(otro_dict)
print(diccionario)