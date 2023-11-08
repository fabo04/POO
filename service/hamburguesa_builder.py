from domain.hamburguesa import Hamburguesa

class HamburguesaBuilder:
    def __init__(self):
        self.hamburguesa = Hamburguesa()

    def agregar_carnes(self, cantidad):
        self.hamburguesa.carnes = cantidad
        return self

    def agregar_cheddar(self, tiene_cheddar=True):
        self.hamburguesa.cheddar = tiene_cheddar
        return self

    def agregar_barbacoa(self, tiene_barbacoa=True):
        self.hamburguesa.barbacoa = tiene_barbacoa
        return self

    def agregar_papas_fritas(self, tiene_papas_fritas=True):
        self.hamburguesa.papas_fritas = tiene_papas_fritas
        return self

    def construir_hamburguesa(self):
        return self.hamburguesa


