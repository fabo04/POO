from domain.estado_pedido import EstadoPedido, RecibidoHandler, PreparandoHandler, ListoHandler, EntregadoHandler

class EstadoPedidoController:
    def __init__(self):
        self.estado_pedido = EstadoPedido()
        recibido_handler = RecibidoHandler()
        preparando_handler = PreparandoHandler()
        listo_handler = ListoHandler()
        entregado_handler = EntregadoHandler()

        self.estado_pedido.set_next_handler(recibido_handler)
        recibido_handler.set_next_handler(preparando_handler)
        preparando_handler.set_next_handler(listo_handler)
        listo_handler.set_next_handler(entregado_handler)

    def gestionar_estado_pedido(self, estado):
        self.estado_pedido.handle_request(estado)

