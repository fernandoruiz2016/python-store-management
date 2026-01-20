class Comprobante():

    #Atributos Encapsulados (Privados)
    __idComprobante =""; __tipo= ""
    __fecha =""; __total= ""

    #Construtor
    def __init__(self, idComprobante, tipo, fecha, total):
        self.__idComprobante = idComprobante
        self.__tipo = tipo
        self.__fecha = fecha
        self.__total = total

    def getIdComprobante(self):
        return self.__idComprobante
    def setIdComprobante(self, idcomprobante):
        self.__idComprobante=idcomprobante

    def getTipo(self):
        return self.__tipo
    def setTipo(self, tipo):
        self.__tipo=tipo

    def getFecha(self):
        return self.__fecha
    def setFecha(self, fecha):
        self.__fecha=fecha

    def getTotal(self):
        return self.__total
    def setTotal(self, total):
        self.__total=total