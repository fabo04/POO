class EstadoPedido:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, estado):
        if self.next_handler:
            self.next_handler.handle_request(estado)

class RecibidoHandler(EstadoPedido):
    def handle_request(self, estado):
        if estado.lower() == "recibido":
            print("Pedido recibido. Preparando hamburguesa...")
        elif self.next_handler:
            self.next_handler.handle_request(estado)

class PreparandoHandler(EstadoPedido):
    def handle_request(self, estado):
        if estado.lower() == "preparando":
            print("Hamburguesa en preparación. Por favor, espere...")
        elif self.next_handler:
            self.next_handler.handle_request(estado)

class ListoHandler(EstadoPedido):
    def handle_request(self, estado):
        if estado.lower() == "listo":
            print("Su hamburguesa está lista para ser entregada.")
        elif self.next_handler:
            self.next_handler.handle_request(estado)

class EntregadoHandler(EstadoPedido):
    def handle_request(self, estado):
        if estado.lower() == "entregado":
            print("Pedido entregado. ¡Disfrute de su hamburguesa!")
        elif self.next_handler:
            self.next_handler.handle_request(estado)
