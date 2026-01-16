from Modelo.clientes import cliente
from Repository.ClienteRepository import ClienteRepository

class ClienteController():

    @staticmethod
    def insertar(datos):
        cli = cliente(*datos)
        return ClienteRepository.insertar(cli)

    @staticmethod
    def listar():
        return ClienteRepository.listar()

    @staticmethod
    def buscar_por_dni(dni):
        return ClienteRepository.buscar(dni)

    @staticmethod
    def modificar(datos):
        cli = cliente(*datos)
        return ClienteRepository.modificar(cli)

    @staticmethod
    def eliminar(dni):
        return ClienteRepository.eliminar(dni)
