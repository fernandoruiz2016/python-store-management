class Empleado():

    #Atributos Encapsulados (Privados)
    __dniEmpleado =""; __nombresEmpleado= ""
    __apellidoPaternoEmpleado =""; __apellidoMaternoEmpleado= ""
    __direccionEmpleado= ""; __telefonoEmpleado=""

    #Construtor
    def __init__(self, dniempleado, nombresempleado, apellidopaternoempleado, apellidomaternoempleado, direccionempleado, telefonoempleado):
        self.__dniEmpleado = dniempleado
        self.__nombresEmpleado = nombresempleado
        self.__apellidoPaternoEmpleado = apellidopaternoempleado
        self.__apellidoMaternoEmpleado = apellidomaternoempleado
        self.__direccionEmpleado = direccionempleado
        self.__telefonoEmpleado = telefonoempleado

    def getDniEmpleado(self):
        return self.__dniEmpleado
    def setDniEmpleado(self, dniempleado):
        self.__dniEmpleado=dniempleado

    def getNombresEmpleado(self):
        return self.__nombresEmpleado
    def setNombresEmpleado(self, nombresempleado):
        self.__nombresEmpleado=nombresempleado

    def getApellidoPaternoEmpleado(self):
        return self.__apellidoPaternoEmpleado
    def setApellidoPaternoEmpleado(self, apellidoPaternoempleado):
        self.__apellidoPaternoEmpleado=apellidoPaternoempleado

    def getApellidoMaternoEmpleado(self):
        return self.__apellidoMaternoEmpleado
    def setApellidoMaternoEmpleado(self, apellidoMaternoempleado):
        self.__apellidoMaternoEmpleado=apellidoMaternoempleado

    def getDireccionEmpleado(self):
        return self.__direccionEmpleado
    def setDireccionEmpleado(self, direccionempleado):
        self.__direccionEmpleado=direccionempleado

    def getTelefonoEmpleado(self):
        return self.__telefonoEmpleado
    def setTelefonoEmpleado(self, telefonoempleado):
        self.__telefonoEmpleado=telefonoempleado
