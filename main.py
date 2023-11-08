from controller.hamburguesa_controller import HamburguesaController
from view.hamburguesa_view import HamburguesaView
from controller.estado_pedido_controller import EstadoPedidoController

def main():
    view = HamburguesaView()
    controller = HamburguesaController()

    cantidad_carnes = view.solicitar_carnes()
    cheddar = view.preguntar_cheddar()
    barbacoa = view.preguntar_barbacoa()
    papas_fritas = view.preguntar_papas_fritas()

    hamburguesa = controller.crear_hamburguesa(cantidad_carnes, cheddar, barbacoa, papas_fritas)

    view.mostrar_pedido(hamburguesa)

    estado_pedido_controller = EstadoPedidoController()

    estado = input("Ingrese el estado del pedido (Recibido/Preparando/Listo/Entregado): ")
    estado_pedido_controller.gestionar_estado_pedido(estado)

if __name__ == "__main__":
    main()
