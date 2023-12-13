import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from tela import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.zerobotao.clicked.connect()
        self.ui.um_botao.clicked.connect()
        self.ui.dois_botao.clicked.connect()
        self.ui.tres_botao.clicked.connect()
        self.ui.quatro_botao.clicked.connect()
        self.ui.cinco_botao.clicked.connect()
        self.ui.seis_botao.clicked.connect()
        self.ui.sete_botao.clicked.connect()
        self.ui.oito_botao.clicked.connect()
        self.ui.nove_botao.clicked.connect()
        self.ui.virgulabotao.clicked.connect()
        self.ui.multiplicacaobotao.clicked.connect()
        self.ui.subtracaobotao.connect()
        self.ui.adicao_botao.clicked.connect()
        self.ui.divisaoBotao.clicked.connect()
        self.ui.porcentagembotao.clicked.connect()
        self.ui.clearBottom.clicked.connect()
        self.ui.clearAllBottom.clicked.connect()
        self.ui.igualbotao.clicked.connect()
        

        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())