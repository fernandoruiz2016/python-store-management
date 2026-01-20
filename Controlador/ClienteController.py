from Repository.clienteRepository import ClienteRepository
from Modelo.cliente import Cliente

class ClienteController():

    @staticmethod
    def registrar(datos):
        if not datos:
            raise ValueError("Faltan los datos del cliente")
        
        dni, nombres, ap_pat, ap_mat, direccion, telefono = datos
        if not dni:
            raise ValueError("DNI obligatorio")
        
        cli = Cliente(
            dni,
            nombres,
            ap_pat,
            ap_mat,
            direccion,
            telefono
        )
        return ClienteRepository.registrar(cli)

    @staticmethod
    def listar():
        try:
            return ClienteRepository.listar()
        except Exception:
            raise ValueError("Error al listar clientes")

    @staticmethod
    def buscar(dni):
        if not dni:
            raise ValueError("Debe ingresar un DNI")
        return ClienteRepository.buscar(dni)

    @staticmethod
    def modificar(datos):
        if not datos:
            raise ValueError("Faltan los datos del cliente")
        
        dni, nombres, ap_pat, ap_mat, direccion, telefono = datos
        if not dni:
            raise ValueError("DNI obligatorio")
        
        cli = Cliente(
            dni,
            nombres,
            ap_pat,
            ap_mat,
            direccion,
            telefono
        )
        return ClienteRepository.modificar(cli)

    @staticmethod
    def eliminar(dni):
        if not dni:
            raise ValueError("Debe seleccionar un cliente")

        if not ClienteRepository.buscar(dni):
            raise ValueError("El cliente no existe")

        return ClienteRepository.eliminar(dni)
