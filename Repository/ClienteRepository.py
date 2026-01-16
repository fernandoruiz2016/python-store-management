from config.database import get_connection
from Modelo.clientes import cliente

class ClienteRepository:

    @staticmethod
    def insertar(cliente):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO clientes (
                dni,
                nombres,
                apellido_paterno,
                apellido_materno,
                direccion,
                telefono
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            cliente.getDniCliente(),
            cliente.getNombresCliente(),
            cliente.getApellidoPaternoCliente(),
            cliente.getApellidoMaternoCliente(),
            cliente.getDireccionCliente(),
            cliente.getTelefonoCliente()
        ))

        conn.commit()
        cursor.close()
        conn.close()
    
    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT dni, nombres, apellido_paterno, apellido_materno, direccion, telefono
            FROM clientes
        """
        cursor.execute(sql)
        clientes = []

        for fila in cursor.fetchall():
            clientes.append(cliente(*fila))

        cursor.close()
        conn.close()

        return clientes
    
    @staticmethod
    def buscar(dni):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT dni, nombres, apellido_paterno, apellido_materno, direccion, telefono
            FROM clientes
            WHERE dni = %s
        """
        cursor.execute(sql, (
            dni,
        ))
        clientes = []

        for fila in cursor.fetchall():
            clientes.append(cliente(*fila))

        cursor.close()
        conn.close()

        return clientes
    
    @staticmethod
    def modificar(cliente):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE clientes
            SET
                nombres = %s,
                apellido_paterno = %s,
                apellido_materno = %s,
                direccion = %s,
                telefono = %s
            WHERE dni = %s
        """

        cursor.execute(sql, (
            cliente.getNombresCliente(),
            cliente.getApellidoPaternoCliente(),
            cliente.getApellidoMaternoCliente(),
            cliente.getDireccionCliente(),
            cliente.getTelefonoCliente(),
            cliente.getDniCliente()
        ))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar(dni):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            DELETE FROM clientes WHERE dni = %s
        """

        cursor.execute(sql, (
            dni,
        ))

        conn.commit()
        cursor.close()
        conn.close()