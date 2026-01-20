from config.database import get_connection
from Modelo.cliente import Cliente

class ClienteRepository:

    @staticmethod
    def registrar(Cliente):
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

        try:
            cursor.execute(sql, (
                Cliente.getDniCliente(),
                Cliente.getNombresCliente(),
                Cliente.getApellidoPaternoCliente(),
                Cliente.getApellidoMaternoCliente(),
                Cliente.getDireccionCliente(),
                Cliente.getTelefonoCliente()
            ))

            conn.commit()
            return True
        
        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
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

        try:
            cursor.execute(sql)
            clientes = []

            for fila in cursor.fetchall():
                clientes.append(Cliente(*fila))
            
            return clientes

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def buscar(dni):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT dni, nombres, apellido_paterno, apellido_materno, direccion, telefono
            FROM clientes
            WHERE dni = %s
        """
        
        try:
            cursor.execute(sql, (
                dni,
            ))
            clientes = []

            for fila in cursor.fetchall():
                clientes.append(Cliente(*fila))
            return clientes

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def modificar(Cliente):
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

        try:
            cursor.execute(sql, (
                Cliente.getNombresCliente(),
                Cliente.getApellidoPaternoCliente(),
                Cliente.getApellidoMaternoCliente(),
                Cliente.getDireccionCliente(),
                Cliente.getTelefonoCliente(),
                Cliente.getDniCliente()
            ))
            conn.commit()
            return True
        
        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def eliminar(dni):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            DELETE FROM clientes WHERE dni = %s
        """

        try:
            cursor.execute(sql, (
                dni,
            ))
            conn.commit()
            
            return True

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()