#Programando el comportamiento de la ventana login.py

from PyQt5 import QtWidgets ,uic
from Vista.ventanaPrincipal import VentanaPrincipal

class Login(QtWidgets.QMainWindow):

    Conteo = 0

    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        uic.loadUi("UI/login.ui", self)#==> se debe colocar el nombre y ruta del formulario
        self.show()

    #Eventos
        self.btnIniciar.clicked.connect(self.iniciarSesion)

    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtPassword.text()
        if usuario == "kenny" and contraseña == "123456":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()
        else:
            self.Conteo +=1 #El contador se incrementa en 1
            QtWidgets.QMessageBox.information(self, "Error de intentos",
                                              "Intento Nro: " + str(self.Conteo), QtWidgets.QMessageBox.Ok)
            if self.Conteo == 3:
                QtWidgets.QMessageBox.information(self, "Salida del sistema",
                                              "Lo sentimos, has agotado tus 3 intentos", QtWidgets.QMessageBox.Ok)
                self.close()
