class HamburguesaView:
    def solicitar_carnes(self):
        return int(input("¿Con cuántas carnes quieres tu hamburguesa? "))

    def preguntar_cheddar(self):
        return input("¿Quieres agregarle cheddar a tu hamburguesa? (sí/no): ").lower() == "si"

    def preguntar_barbacoa(self):
        return input("¿Quieres agregarle barbacoa a tu hamburguesa? (sí/no): ").lower() == "si"

    def preguntar_papas_fritas(self):
        return input("¿Quieres agregar papas fritas? (sí/no): ").lower() == "si"

    def mostrar_pedido(self, hamburguesa):
        print("Pedido de hamburguesa:")
        print(f"Carnes: {hamburguesa.carnes}")
        print(f"Cheddar: {'Sí' if hamburguesa.cheddar else 'No'}")
        print(f"Barbacoa: {'Sí' if hamburguesa.barbacoa else 'No'}")
        print(f"Papas Fritas: {'Sí' if hamburguesa.papas_fritas else 'No'}")
