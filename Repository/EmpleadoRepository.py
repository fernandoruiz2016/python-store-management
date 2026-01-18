from config.database import get_connection
from Modelo.empleados import empleado

class EmpleadoRepository:

    @staticmethod
    def registrar(empleado):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO empleados (
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
                empleado.getDniEmpleado(),
                empleado.getNombresEmpleado(),
                empleado.getApellidoPaternoEmpleado(),
                empleado.getApellidoMaternoEmpleado(),
                empleado.getDireccionEmpleado(),
                empleado.getTelefonoEmpleado()
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
            FROM empleados
        """

        try:
            cursor.execute(sql)
            empleados = []

            for fila in cursor.fetchall():
                empleados.append(empleado(*fila))
            
            return empleados

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
            FROM empleados
            WHERE dni = %s
        """
        
        try:
            cursor.execute(sql, (
                dni,
            ))
            empleados = []

            for fila in cursor.fetchall():
                empleados.append(empleado(*fila))
            return empleados

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def modificar(empleado):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE empleados
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
                empleado.getNombresEmpleado(),
                empleado.getApellidoPaternoEmpleado(),
                empleado.getApellidoMaternoEmpleado(),
                empleado.getDireccionEmpleado(),
                empleado.getTelefonoEmpleado(),
                empleado.getDniEmpleado()
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
            DELETE FROM empleados WHERE dni = %s
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