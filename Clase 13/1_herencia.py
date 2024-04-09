class ClasePadre:
    variables_clase_A = 123
    def metodo_Padre(self):
        print("Este es el método Padre")


class ClaseHija(ClasePadre):
    variables_clase_B = 789
    def metodo_Hija(self):
        print("Este es el método Hija")


instancia_de_clase_A = ClasePadre()
instancia_de_clase_A.metodo_Padre()
instancia_de_clase_B = ClaseHija()
instancia_de_clase_B.metodo_Padre()
instancia_de_clase_B.metodo_Hija()

print(instancia_de_clase_A.variables_clase_A)
print(instancia_de_clase_B.variables_clase_A)
print(instancia_de_clase_B.variables_clase_B)