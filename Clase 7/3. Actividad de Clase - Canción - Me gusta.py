"""
Descripción de la actividad. 

Escribir la letra de la canción Me gusta de Manu Chao, utilizando la sentencia de iteración for: 
 https://www.letras.com/manu-chao/7352/

Importante: Deberán crear también una lista con los párrafos de la canción para poder imprimirlos correctamente por pantalla.

Ejemplo: 
Me gustan los aviones, me gustas tú
Me gusta viajar, me gustas tú
Me gusta la mañana, me gustas tú
Me gusta el viento, me gustas tú
Me gusta soñar, me gustas tú
Me gusta la mar, me gustas tú

"""
estribillo = (
    "¿Qué voy a hacer? Je ne sais pas\n"
    "¿Qué voy a hacer? Je ne sais plus\n"
    "¿Qué voy a hacer? Je suis perdu\n"
    "¿Qué horas son, mi corazón?\n",
)

verso_1 = ("los aviones", "viajar", "la mañana",
           "el viento", "soñar", "la mar")
verso_2 = ("la moto", "correr", "la lluvia", "volver",
           "marihuana", "colombiana", "la montaña", "la noche")
verso_3 = ("la cena", "la vecina", "su cocina",
           "camelar", "la guitarra", "el reggae")
verso_4 = ("la canela", "el fuego", "menear", "la Coruña",
           "Malasaña", "la castaña", "Guatemala")
secuencia = (verso_1, estribillo, verso_2, estribillo,
             verso_3, estribillo, verso_4, estribillo, estribillo)

letra = ""

for verso_o_estribillo in secuencia:
    if len(verso_o_estribillo) > 1:   # verso
        for frase in verso_o_estribillo:
            letra += f"Me gusta {frase}, me gustas tú.\n"
    else:  # estribillo
        letra += verso_o_estribillo[0]
    letra += "\n"

print(letra)