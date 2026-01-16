class cliente():

    #Atributos Encapsulados (Privados)
    __dniCliente =""; __nombresCliente= ""
    __apellidoPaternoCliente =""; __apellidoMaternoCliente= ""
    __direccionCliente= ""; __telefonoCliente=""

    #Construtor
    def __init__(self, dnicliente, nombrescliente, apellidopaternocliente, apellidomaternocliente, direccioncliente, telefonocliente):
        self.__dniCliente = dnicliente
        self.__nombresCliente = nombrescliente
        self.__apellidoPaternoCliente = apellidopaternocliente
        self.__apellidoMaternoCliente = apellidomaternocliente
        self.__direccionCliente = direccioncliente
        self.__telefonoCliente = telefonocliente

    def getDniCliente(self):
        return self.__dniCliente
    def setDniCliente(self, dnicliente):
        self.__dniCliente=dnicliente

    def getNombresCliente(self):
        return self.__nombresCliente
    def setNombresCliente(self, nombrescliente):
        self.__nombresCliente=nombrescliente

    def getApellidoPaternoCliente(self):
        return self.__apellidoPaternoCliente
    def setApellidoPaternoCliente(self, apellidoPaternocliente):
        self.__apellidoPaternoCliente=apellidoPaternocliente

    def getApellidoMaternoCliente(self):
        return self.__apellidoMaternoCliente
    def setApellidoMaternoCliente(self, apellidoMaternocliente):
        self.__apellidoMaternoCliente=apellidoMaternocliente

    def getDireccionCliente(self):
        return self.__direccionCliente
    def setDireccionCliente(self, direccioncliente):
        self.__direccionCliente=direccioncliente

    def getTelefonoCliente(self):
        return self.__telefonoCliente
    def setTelefonoCliente(self, telefonocliente):
        self.__telefonoCliente=telefonocliente
