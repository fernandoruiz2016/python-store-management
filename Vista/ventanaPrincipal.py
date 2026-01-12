#Programando el comportamiento de la ventana ventanaPrincipal.py
#Y su comportamiento inicial

from PyQt5 import QtWidgets ,uic
from PyQt5 import QtGui
# QtGui --> usiliza los botones del formulario
from Vista.ventanaClientes import VentanaClientes
from Vista.ventanaEmpleados import VentanaEmpleados
from Vista.ventanaProductos import VentanaProductos
from Vista.ventanaComprobante import VentanaComprobante

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui", self)#==> se debe colocar el nombre y ruta del formulario
        self.show()
    
    # Eventos
        self.btnClientes.clicked.connect(self.abrirVentanaClientes)
        self.btnEmpleados.clicked.connect(self.abrirVentanaEmpleados)
        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnSalir.clicked.connect(self.cerrar)
        self.btnComprobante.clicked.connect(self.abrirVentanaComprobante)

    def abrirVentanaClientes(self):
        vclientes = VentanaClientes(self)
        vclientes.show()

    def abrirVentanaEmpleados(self):
        vempleados = VentanaEmpleados(self)
        vempleados.show()

    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()
    
    def cerrar(self):
        self.close()
    
    # Aviso para la opcion Comprobante
    def abrirVentanaComprobante(self):
        vComprobante = VentanaComprobante(self)
        vComprobante.show()
