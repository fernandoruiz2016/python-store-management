import sys
from PyQt5 import QtWidgets
from Vista.login import Login
from database.crearTablas import crear_Tablas

if __name__=='__main__':
    crear_Tablas()
    app=QtWidgets.QApplication(sys.argv)
    Window = Login()
    app.exec()