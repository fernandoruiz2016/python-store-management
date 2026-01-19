from Repository.ComprobanteRepository import ComprobanteRepository
from Modelo.comprobantes import comprobante

class ComprobanteController():

    @staticmethod
    def registrar(datos):
        if not datos:
            raise ValueError("Faltan los datos del comprobante")
        
        id, tipo, fecha, total = datos
        if not id:
            raise ValueError("Id obligatorio")
        
        com = comprobante(
            id,
            tipo, 
            fecha,
            total
        )
        return ComprobanteRepository.registrar(com)

    @staticmethod
    def listar():
        try:
            return ComprobanteRepository.listar()
        except Exception:
            raise ValueError("Error al listar comprobantes")

    @staticmethod
    def buscar(id):
        if not id:
            raise ValueError("Debe ingresar un Id")
        return ComprobanteRepository.buscar(id)

    @staticmethod
    def modificar(datos):
        if not datos:
            raise ValueError("Faltan los datos del comprobante")
        
        id, tipo, fecha, total = datos
        if not id:
            raise ValueError("Id obligatorio")
        
        com = comprobante(
            id,
            tipo, 
            fecha,
            total
        )
        return ComprobanteRepository.modificar(com)

    @staticmethod
    def eliminar(id):
        if not id:
            raise ValueError("Debe seleccionar un comprobante")

        if not ComprobanteRepository.buscar(id):
            raise ValueError("El comprobante no existe")

        return ComprobanteRepository.eliminar(id)
