#Programando el comportamiento de la ventana ventanaClientes.py
#Y su comportamiento inicial

from PyQt5 import QtWidgets ,uic
from PyQt5 import QtGui
from PyQt5.QtCore import QDate
import re

from Controlador.comprobanteController import ComprobanteController

# QtGui --> usiliza los botones del formulario

class VentanaComprobante(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaComprobante, self).__init__(parent)
        uic.loadUi("UI/ventanaComprobantes.ui", self)#==> se debe colocar el nombre y ruta del formulario
        # self.show()
        self.consultado = False #<- Para la funcion Eliminar

        # Eventos
        self.tblComprobantes.clicked.connect(self.seleccionarFilaTabla)

        self.btnConsultar.clicked.connect(self.consultar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        self.listar()

    def obtenerId(self):
        return self.txtId.text()
    
    def obtenerTipo(self):
        return self.cboTipo.currentText()

    def obtenerFecha(self):
        return self.dtFecha.date().toPyDate()

    def obtenerTotal(self):
        return self.txtTotal.text()

    def limpiarTabla(self):
        self.tblComprobantes.clearContents()
        self.tblComprobantes.setRowCount(0)

    def valida(self):
        if self.txtId.text() =="":
            self.txtId.setFocus()
            return "Id del comprobante...!!!"
        if self.obtenerTipo() == "Boleta":
            if not re.match(r"^B-\d{3}$", self.obtenerId()):
                self.txtId.setFocus()
                return "Formato inválido de Boleta. Ej: B-001"

        elif self.obtenerTipo() == "Factura":
            if not re.match(r"^F-\d{3}$", self.obtenerId()):
                self.txtId.setFocus()
                return "Formato inválido de Factura. Ej: F-001"

        if self.cboTipo.currentIndex()==0:
            self.cboTipo.setFocus()
            return "Tipo del comprobante...!!!"
        if self.dtFecha.date()==QDate(2000, 1, 1):
            self.dtFecha.setFocus()
            return "Fecha del comprobante...!!!"
        if self.dtFecha.date() > QDate.currentDate():
            self.dtFecha.setFocus()
            return "Fecha del comprobante no válida...!!!"
        if self.txtTotal.text()=="":
            self.txtTotal.setFocus()
            return "Importe total del comprobante...!!!"
        else:
            return ""

    def listar(self):
        try:
            comprobantes = ComprobanteController.listar()
            
            self.tblComprobantes.setRowCount(len(comprobantes))
            self.tblComprobantes.setColumnCount(4)
            #Cabecera
            self.tblComprobantes.verticalHeader().setVisible(False)
            for i,com in enumerate(comprobantes):
                self.tblComprobantes.setItem(i, 0, QtWidgets.QTableWidgetItem(com.getIdComprobante()))
                self.tblComprobantes.setItem(i, 1, QtWidgets.QTableWidgetItem(com.getTipo()))
                self.tblComprobantes.setItem(i, 2, QtWidgets.QTableWidgetItem(str(com.getFecha())))
                self.tblComprobantes.setItem(i, 3, QtWidgets.QTableWidgetItem(str(com.getTotal())))
            self.consultado = False
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def limpiarControles(self):
        self.txtId.clear()
        self.cboTipo.setCurrentIndex(0)
        self.dtFecha.setDate(QDate(2000, 1, 1))
        self.txtTotal.setText("")

    # Mantenimientos (Grabar (Registrar), Consultar, Modificar, Listar, Quitar)
    def registrar(self):
        try:
            if self.valida() == "":
                id=self.obtenerId()
                if not ComprobanteController.buscar(id):
                    ComprobanteController.registrar((self.obtenerId(), self.obtenerTipo(),
                            self.obtenerFecha(), self.obtenerTotal()))
                    self.limpiarControles()
                    self.listar()
                else:
                    QtWidgets.QMessageBox.information(self, "Registrar Comprobante",
                                                    "El Id ingresado ya existe... !!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Comprobante",
                                                    "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
        
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def consultar(self):

        try:
            #self.limpiarTabla()
            if len(ComprobanteController.listar()) == 0:
                    QtWidgets.QMessageBox.information(self, "Consultar Comprobante",
                                                    "No existe comprobantes a consultar... !!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                id, _ = QtWidgets.QInputDialog.getText(self, "Consultar Comprobante",
                                                    "Ingrese el Id a consultar")
                com = ComprobanteController.buscar(id)
                if not com:
                    QtWidgets.QMessageBox.information(self, "Consultar Comprobante",
                                                    "El Id ingresado no existe... !!!",
                                                    QtWidgets.QMessageBox.Ok)
                else:
                    self.txtId.setText(com[0].getIdComprobante())
                    self.cboTipo.setText(com[0].getTipo())
                    self.dtFecha.setText(com[0].getFecha())
                    self.txtTotal.setText(com[0].getTotal())

                    self.tblClientes.setRowCount(1)
                    self.tblClientes.setItem(0,0, QtWidgets.QTableWidgetItem(com[0].getIdComprobante()))
                    self.tblClientes.setItem(0,1, QtWidgets.QTableWidgetItem(com[0].getTipo()))
                    self.tblClientes.setItem(0,2, QtWidgets.QTableWidgetItem(str(com[0].getFecha())))
                    self.tblClientes.setItem(0,3, QtWidgets.QTableWidgetItem(str(com[0].getTotal())))

                    self.consultado = True
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def eliminar(self):
        try:
            if self.consultado == False:
                QtWidgets.QMessageBox.information(self, "Consulte Comprobante",
                                                "Por favor consultar el Id",
                                                QtWidgets.QMessageBox.Ok)
            else:
                id = self.txtId.text()
                ComprobanteController.eliminar(id)
                self.limpiarControles()
                self.listar()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def quitar(self):
        try:
            if len(ComprobanteController.listar()) ==0:
                QtWidgets.QMessageBox.information(self, "Eliminar Comprobante",
                                                "No existen comprobantes a eliminar... !!!",
                                                QtWidgets.QMessageBox.Ok)
            else:
                fila=self.tblClientes.selectedItems()
                if fila:
                    indiceFila=fila[0].row()
                    id=self.tblComprobantes.item(indiceFila, 0).text()
                    ComprobanteController.eliminar(id)
                    self.limpiarTabla()
                    self.listar()
                else:
                    QtWidgets.QMessageBox.information(self, "Eliminar Comprobante",
                                                    "Debe seleccionar una fila... !!!",
                                                    QtWidgets.QMessageBox.Ok)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def seleccionarFilaTabla(self):
        fila = self.tblComprobantes.currentRow()

        self.txtId.setText(self.tblComprobantes.item(fila,0).text())
        self.cboTipo.setCurrentText(self.tblComprobantes.item(fila,1).text())
        self.dtFecha.setDate(QDate.fromString(self.tblComprobantes.item(fila,2).text(), "yyyy-MM-dd"))
        self.txtTotal.setText(self.tblComprobantes.item(fila,3).text())

    def modificar(self):
        if len(ComprobanteController.listar()) == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Comprobante",
                                                  "No existen comprobantes a Modificar... !!!",
						   QtWidgets.QMessageBox.Ok)
        else:
            try:
                fila=self.tblComprobantes.selectedItems()
                
                indiceFila=fila[0].row()
                self.txtId.setText(self.tblComprobantes.item(indiceFila, 0).text())

                id= self.obtenerId()
                com= ComprobanteController.buscar(id)
                if com:
                    if self.valida() == "":
                        ComprobanteController.modificar((self.obtenerId(), self.obtenerTipo(),
                                        self.obtenerFecha(),
                                        self.obtenerTotal()))
                        self.limpiarControles()
                        self.listar()
                    else:
                        QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
            except ValueError as e:
                QtWidgets.QMessageBox.warning(self, "Error", str(e))