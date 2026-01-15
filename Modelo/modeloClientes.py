from config.database import get_connection

class ModeloClientes:

    @staticmethod
    def obtenerClientes():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombres FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()

        return clientes