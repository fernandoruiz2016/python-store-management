class producto():

    #Atributos Encapsulados (Privados)
    __codigoProducto = ""; __nombreProducto= ""
    __descripcionProducto = ""; __stockMinimo = 0
    __stockActual = 0; __precioCosto = 0.0
    __precioVenta = 0.0; __proveedor = ""
    __almacen = ""

    #Construtor
    def __init__(self, codigoproducto, nombreproducto, descripcionproducto, stockminimo, stockactual, preciocosto, precioventa, proveedor, almacen):
        self.__codigoProducto = codigoproducto
        self.__nombreProducto = nombreproducto
        self.__descripcionProducto = descripcionproducto
        self.__stockMinimo = stockminimo
        self.__stockActual = stockactual
        self.__precioVenta = precioventa
        self.__precioCosto = preciocosto
        self.__proveedor = proveedor
        self.__almacen = almacen

    def getCodigoProducto(self):
        return self.__codigoProducto
    def setCodigoProducto(self, codigoproducto):
        self.__codigoProducto=codigoproducto
    
    def getNombreProducto(self):
        return self.__nombreProducto
    def setNombreProducto(self, nombreproducto):
        self.__nombreProducto=nombreproducto

    def getDescripcionProducto(self):
        return self.__descripcionProducto
    def setDescripcionProducto(self, descripcionproducto):
        self.__descripcionProducto=descripcionproducto

    def getStockMinimo(self):
        return self.__stockMinimo
    def setStockMinimo(self, stockminimo):
        self.__stockMinimo=stockminimo
    
    def getStockActual(self):
        return self.__stockActual
    def setStockActual(self, stockactual):
        self.__stockActual=stockactual
    
    def getPrecioCosto(self):
        return self.__precioCosto
    def setPrecioCosto(self, preciocosto):
        self.__precioCosto=preciocosto

    def getPrecioVenta(self):
        return self.__precioVenta
    def setPrecioVenta(self, precioventa):
        self.__precioVenta=precioventa

    def getProveedor(self):
        return self.__proveedor
    def setProveedor(self, proveedor):
        self.__proveedor=proveedor
    
    def getAlmacen(self):
        return self.__almacen
    def setAlmacen(self, almacen):
        self.__almacen=almacen

