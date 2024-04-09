class Vehiculo:
    def arrancar(self):
        print("arrancando...")


class Auto(Vehiculo):
    def tocar_bocina(self):
        print("tocando bocina...")


class MovimientosMarinos:  # esta clase no está destinada a ser instanciada
    def virar_estribor(self):
        print("virando a estribor")

    def virar_babor(self):
        print("virando a babor")


class Lancha(Vehiculo, MovimientosMarinos):  # mixin
    pass

lancha = Lancha()
lancha.arrancar()
lancha.virar_babor()
lancha.virar_estribor()
