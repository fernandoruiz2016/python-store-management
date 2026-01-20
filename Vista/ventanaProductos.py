#Programando el comportamiento de la ventana ventanaProductos.py
#Y su comportamiento inicial

from PyQt5 import QtWidgets ,uic
from PyQt5 import QtGui
import re

from Controlador.productoController import ProductoController

# QtGui --> usiliza los botones del formulario

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("UI/ventanaProductos.ui", self)#==> se debe colocar el nombre y ruta del formulario
        # self.show()
        self.consultado = False #<- Para la funcion Eliminar

        # Eventos
        self.tblProductos.clicked.connect(self.seleccionarFilaTabla)

        self.btnConsultar.clicked.connect(self.consultar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        self.listar()

    def obtenerCodigo(self):
        return self.txtCodigo.text()
    
    def obtenerNombre(self):
        return self.txtNombre.text()

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()

    def obtenerStockMinimo(self):
        return self.txtStockMinimo.text()

    def obtenerStockActual(self):
        return self.txtStockActual.text()

    def obtenerPrecioCosto(self):
        return self.txtPrecioCosto.text()

    def obtenerPrecioVenta(self):
        return self.txtPrecioVenta.text()

    def obtenerProveedor(self):
        return self.cboProveedor.currentText()

    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text() =="":
            self.txtCodigo.setFocus()
            return "Codigo del producto...!!!"
        if not re.match(r"^P\d{3}$", self.txtCodigo.text()):
            self.txtCodigo.setFocus()
            return "Código inválido. Ejemplo: P001, P002, P003"
        elif self.txtNombre.text()=="":
            self.txtNombre.setFocus()
            return "Nombre del producto...!!!"
        elif self.txtDescripcion.text()=="":
            self.txtDescripcion.setFocus()
            return "Descripcion del producto...!!!"
        elif self.txtStockMinimo.text()=="":
            self.txtStockMinimo.setFocus()
            return "Stock Minimo del producto...!!!"
        elif self.txtStockActual.text()=="":
            self.txtStockActual.setFocus()
            return "Stock Actual del producto...!!!"
        elif self.txtPrecioCosto.text()=="":
            self.txtPrecioCosto.setFocus()
            return "Precio Costo del producto...!!!"
        elif self.txtPrecioVenta.text()=="":
            self.txtPrecioVenta.setFocus()
            return "Precio Venta del producto...!!!"
        elif self.cboProveedor.currentIndex()==0:
            self.cboProveedor.setFocus()
            return "Proveedor del producto...!!!"
        elif self.cboAlmacen.currentIndex()==0:
            self.cboAlmacen.setFocus()
            return "Almacen del producto...!!!"
        else:
            return ""

    def listar(self):
        try:
            productos = ProductoController.listar()
            
            self.tblProductos.setRowCount(len(productos))
            self.tblProductos.setColumnCount(9)
            #Cabecera
            self.tblProductos.verticalHeader().setVisible(False)
            for i,pro in enumerate(productos):
                self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(pro.getCodigoProducto()))
                self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(pro.getNombreProducto()))
                self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(pro.getDescripcionProducto()))
                self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(str(pro.getStockMinimo())))
                self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(str(pro.getStockActual())))
                self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pro.getPrecioCosto())))
                self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(str(pro.getPrecioVenta())))
                self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(pro.getProveedor()))
                self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(pro.getAlmacen()))
            self.consultado = False
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.setText("")
        self.txtPrecioVenta.setText("")
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)

    # Mantenimientos (Grabar (Registrar), Consultar, Modificar, Listar, Quitar)
    def registrar(self):
        try:
            if self.valida() == "":
                codigo=self.obtenerCodigo()
                if not ProductoController.buscar(codigo):
                    ProductoController.registrar((self.obtenerCodigo(), self.obtenerNombre(),
                                self.obtenerDescripcion(), self.obtenerStockMinimo(),
                                self.obtenerStockActual(), self.obtenerPrecioCosto(),
                                self.obtenerPrecioVenta(), self.obtenerProveedor(), self.obtenerAlmacen()))
                    self.limpiarControles()
                    self.listar()
                else:
                    QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                    "El Código ingresado ya existe... !!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                    "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
        
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def consultar(self):
        try:
            #self.limpiarTabla()
            if len(ProductoController.listar()) == 0:
                    QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                    "No existe productos a consultar... !!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto",
                                                    "Ingrese el Código a consultar")
                pro = ProductoController.buscar(codigo)
                if not pro:
                    QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                    "El Código ingresado no existe... !!!",
                                                    QtWidgets.QMessageBox.Ok)
                else:
                    self.txtCodigo.setText(pro[0].getCodigoProducto())
                    self.txtNombre.setText(pro[0].getNombreProducto())
                    self.txtDescripcion.setText(pro[0].getDescripcionProducto())
                    self.txtStockMinimo.setText(pro[0].getStockMinimo())
                    self.txtStockActual.setText(pro[0].getStockActual())
                    self.txtPrecioCosto.setText(pro[0].getPrecioCosto())
                    self.txtPrecioVenta.setText(pro[0].getPrecioVenta())
                    self.cboProveedor.setCurrentText(pro[0].getProveedor())
                    self.cboAlmacen.setCurrentText(pro[0].getAlmacen())

                    self.tblProductos.setRowCount(1)
                    self.tblProductos.setItem(0,0, QtWidgets.QTableWidgetItem(pro[0].getCodigoProducto()))
                    self.tblProductos.setItem(0,1, QtWidgets.QTableWidgetItem(pro[0].getNombreProducto()))
                    self.tblProductos.setItem(0,2, QtWidgets.QTableWidgetItem(pro[0].getDescripcionProducto()))
                    self.tblProductos.setItem(0,3, QtWidgets.QTableWidgetItem(pro[0].getStockMinimo()))
                    self.tblProductos.setItem(0,4, QtWidgets.QTableWidgetItem(pro[0].getStockActual()))
                    self.tblProductos.setItem(0,5, QtWidgets.QTableWidgetItem(pro[0].getPrecioCosto()))
                    self.tblProductos.setItem(0,6, QtWidgets.QTableWidgetItem(pro[0].getPrecioVenta()))
                    self.tblProductos.setItem(0,7, QtWidgets.QTableWidgetItem(pro[0].getProveedor()))
                    self.tblProductos.setItem(0,8, QtWidgets.QTableWidgetItem(pro[0].getAlmacen()))

                    self.consultado = True
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def eliminar(self):
        try:
            if self.consultado == False:
                QtWidgets.QMessageBox.information(self, "Consulte Producto",
                                                "Por favor consultar el codigo",
                                                QtWidgets.QMessageBox.Ok)
            else:
                codigo = self.txtCodigo.text()
                ProductoController.eliminar(codigo)
                self.limpiarControles()
                self.listar()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def quitar(self):
        try:
            if len(ProductoController.listar()) ==0:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                "No existe productos a eliminar... !!!",
                                                QtWidgets.QMessageBox.Ok)
            else:
                fila=self.tblProductos.selectedItems()
                if fila:
                    indiceFila=fila[0].row()
                    codigo=self.tblProductos.item(indiceFila, 0).text()
                    ProductoController.eliminar(codigo)
                    self.limpiarTabla()
                    self.listar()
                else:
                    QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                    "Debe seleccionar una fila... !!!",
                                                    QtWidgets.QMessageBox.Ok)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def seleccionarFilaTabla(self):
        fila = self.tblProductos.currentRow()

        self.txtCodigo.setText(self.tblProductos.item(fila,0).text())
        self.txtNombre.setText(self.tblProductos.item(fila,1).text())
        self.txtDescripcion.setText(self.tblProductos.item(fila,2).text())
        self.txtStockMinimo.setText(self.tblProductos.item(fila,3).text())
        self.txtStockActual.setText(self.tblProductos.item(fila,4).text())
        self.txtPrecioCosto.setText(self.tblProductos.item(fila,5).text())
        self.txtPrecioVenta.setText(self.tblProductos.item(fila,6).text())
        self.cboProveedor.setCurrentText(self.tblProductos.item(fila,7).text())
        self.cboAlmacen.setCurrentText(self.tblProductos.item(fila,8).text())

    def modificar(self):
        if len(ProductoController.listar()) == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                                  "No existen productos a Modificar... !!!",
						   QtWidgets.QMessageBox.Ok)
        else:
            try:
                fila=self.tblProductos.selectedItems()
                
                indiceFila=fila[0].row()
                self.txtCodigo.setText(self.tblProductos.item(indiceFila, 0).text())

                codigo= self.obtenerCodigo()
                pro= ProductoController.buscar(codigo)
                if pro:
                    if self.valida() == "":
                        ProductoController.modificar((self.obtenerCodigo(), self.obtenerNombre(),
                                self.obtenerDescripcion(), self.obtenerStockMinimo(),
                                self.obtenerStockActual(), self.obtenerPrecioCosto(),
                                self.obtenerPrecioVenta(), self.obtenerProveedor(), self.obtenerAlmacen()))
                        self.limpiarControles()
                        self.listar()
                    else:
                        QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
            except ValueError as e:
                QtWidgets.QMessageBox.warning(self, "Error", str(e))

