from Repository.ClienteRepository import ClienteRepository

class ClienteController():

    @staticmethod
    def registrar(cliente):
        return ClienteRepository.registrar(cliente)

    @staticmethod
    def listar():
        return ClienteRepository.listar()

    @staticmethod
    def buscar(dni):
        return ClienteRepository.buscar(dni)

    @staticmethod
    def modificar(cliente):
        return ClienteRepository.modificar(cliente)

    @staticmethod
    def eliminar(dni):
        return ClienteRepository.eliminar(dni)
