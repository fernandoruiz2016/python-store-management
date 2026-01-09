import sys
from PyQt5 import QtWidgets
from Vista.login import Login

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    Window = Login()
    app.exec()

# Ya no se toca
# ahi se queda