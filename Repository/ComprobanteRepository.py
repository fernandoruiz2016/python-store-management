from config.database import get_connection
from Modelo.comprobantes import comprobante

class ComprobanteRepository:

    @staticmethod
    def registrar(comprobante):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO comprobantes (
                id_comprobante,
                tipo,
                fecha,
                total
            )
            VALUES (%s, %s, %s, %s)
        """

        try:
            cursor.execute(sql, (
                comprobante.getIdComprobante(),
                comprobante.getTipo(),
                comprobante.getFecha(),
                comprobante.getTotal()
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
            SELECT id_comprobante, tipo, fecha, total
            FROM comprobantes
        """

        try:
            cursor.execute(sql)
            comprobantes = []

            for fila in cursor.fetchall():
                comprobantes.append(comprobante(*fila))
            
            return comprobantes

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def buscar(id):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT id_comprobante, tipo, fecha, total
            FROM comprobantes
            WHERE id_comprobante = %s
        """
        
        try:
            cursor.execute(sql, (
                id,
            ))
            comprobantes = []

            for fila in cursor.fetchall():
                comprobantes.append(comprobante(*fila))
            return comprobantes

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def modificar(comprobante):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE comprobantes
            SET
                tipo = %s,
                fecha = %s,
                total = %s
            WHERE id_comprobante = %s
        """

        try:
            cursor.execute(sql, (
                comprobante.getTipo(),
                comprobante.getFecha(),
                comprobante.getTotal(),
                comprobante.getIdComprobante(),
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
    def eliminar(id):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            DELETE FROM comprobantes WHERE id_comprobante = %s
        """

        try:
            cursor.execute(sql, (
                id,
            ))
            conn.commit()
            
            return True

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()