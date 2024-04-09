class Bienvenida:
    def dar_bienvenida(self):
        print("bienvenido!")

class Despedida:
    def dar_despedida(self):
        print("adiós!")

class Saludos(Bienvenida, Despedida):
    pass

saludo = Saludos()
saludo.dar_bienvenida()
saludo.dar_despedida()
