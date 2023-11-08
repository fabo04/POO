import sqlite3

class HamburguesaDAO:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect("hamburguesasPedidas.db")
            cls._instance.create_table()
        return cls._instance

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                carnes INTEGER,
                cheddar INTEGER,
                barbacoa INTEGER,
                papas_fritas INTEGER
            )
        ''')
        self.conn.commit()

    def guardar_pedido(self, carnes, cheddar, barbacoa, papas_fritas):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO pedidos (carnes, cheddar, barbacoa, papas_fritas)
            VALUES (?, ?, ?, ?)
        ''', (carnes, cheddar, barbacoa, papas_fritas))
        self.conn.commit()
