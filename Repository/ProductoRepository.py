from config.database import get_connection
from Modelo.productos import producto

class ProductoRepository:

    @staticmethod
    def registrar(producto):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO productos (
                codigo,
                nombre,
                descripcion,
                stock_minimo,
                stock_actual,
                precio_costo,
                precio_venta,
                proveedor,
                almacen
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(sql, (
                producto.getCodigoProducto(),
                producto.getNombreProducto(),
                producto.getDescripcionProducto(),
                producto.getStockMinimo(),
                producto.getStockActual(),
                producto.getPrecioCosto(),
                producto.getPrecioVenta(),
                producto.getProveedor(),
                producto.getAlmacen()
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
            SELECT codigo, nombre, descripcion, stock_minimo, stock_actual, precio_costo, precio_venta, proveedor, almacen
            FROM productos
        """

        try:
            cursor.execute(sql)
            productos = []

            for fila in cursor.fetchall():
                productos.append(producto(*fila))
            
            return productos

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def buscar(codigo):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT codigo, nombre, descripcion, stock_minimo, stock_actual, precio_costo, precio_venta, proveedor, almacen
            FROM productos
            WHERE codigo = %s
        """
        
        try:
            cursor.execute(sql, (
                codigo,
            ))
            productos = []

            for fila in cursor.fetchall():
                productos.append(producto(*fila))
            return productos

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def modificar(producto):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE productos
            SET
                nombre = %s,
                descripcion = %s,
                stock_minimo = %s,
                stock_actual = %s,
                precio_costo = %s,
                precio_venta = %s,
                proveedor = %s,
                almacen = %s
            WHERE codigo = %s
        """

        try:
            cursor.execute(sql, (
                producto.getNombreProducto(),
                producto.getDescripcionProducto(),
                producto.getStockMinimo(),
                producto.getStockActual(),
                producto.getPrecioCosto(),
                producto.getPrecioVenta(),
                producto.getProveedor(),
                producto.getAlmacen(),
                producto.getCodigoProducto(),
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
    def eliminar(codigo):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            DELETE FROM productos WHERE codigo = %s
        """

        try:
            cursor.execute(sql, (
                codigo,
            ))
            conn.commit()
            
            return True

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            cursor.close()
            conn.close()