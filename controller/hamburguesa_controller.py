from service.hamburguesa_builder import HamburguesaBuilder
from dao.hamburguesa_dao import HamburguesaDAO
from controller.estado_pedido_controller import EstadoPedidoController

class HamburguesaController:
    def __init__(self):
        self.builder = HamburguesaBuilder()
        self.dao = HamburguesaDAO()
        self.estado_pedido_controller = EstadoPedidoController()

    def crear_hamburguesa(self, cantidad_carnes, cheddar, barbacoa, papas_fritas):
        hamburguesa = (
            self.builder
            .agregar_carnes(cantidad_carnes)
            .agregar_cheddar(cheddar)
            .agregar_barbacoa(barbacoa)
            .agregar_papas_fritas(papas_fritas)
            .construir_hamburguesa()
        )

        self.dao.guardar_pedido(hamburguesa.carnes, hamburguesa.cheddar,
                                hamburguesa.barbacoa, hamburguesa.papas_fritas)
        
        return hamburguesa

    def gestionar_estado_pedido(self, estado):
        self.estado_pedido_controller.gestionar_estado_pedido(estado)
