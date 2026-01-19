from Repository.ProductoRepository import ProductoRepository
from Modelo.productos import producto

class ProductoController():

    @staticmethod
    def registrar(datos):
        if not datos:
            raise ValueError("Faltan los datos del producto")
        
        codigo, nombre, descripcion, stock_min, stock_act, p_costo, p_venta, proveedor, almacen = datos
        if not codigo:
            raise ValueError("Código obligatorio")
        
        pro = producto(
            codigo,
            nombre, 
            descripcion, 
            stock_min, 
            stock_act, 
            p_costo, 
            p_venta, 
            proveedor, 
            almacen
        )
        return ProductoRepository.registrar(pro)

    @staticmethod
    def listar():
        try:
            return ProductoRepository.listar()
        except Exception:
            raise ValueError("Error al listar productos")

    @staticmethod
    def buscar(codigo):
        if not codigo:
            raise ValueError("Debe ingresar un código")
        return ProductoRepository.buscar(codigo)

    @staticmethod
    def modificar(datos):
        if not datos:
            raise ValueError("Faltan los datos del producto")
        
        codigo, nombre, descripcion, stock_min, stock_act, p_costo, p_venta, proveedor, almacen = datos
        if not codigo:
            raise ValueError("Código obligatorio")
        
        pro = producto(
            codigo,
            nombre, 
            descripcion, 
            stock_min, 
            stock_act, 
            p_costo, 
            p_venta, 
            proveedor, 
            almacen
        )
        return ProductoRepository.modificar(pro)

    @staticmethod
    def eliminar(codigo):
        if not codigo:
            raise ValueError("Debe seleccionar un producto")

        if not ProductoRepository.buscar(codigo):
            raise ValueError("El producto no existe")

        return ProductoRepository.eliminar(codigo)
