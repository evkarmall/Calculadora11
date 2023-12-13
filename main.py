import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from tela import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.zerobotao.clicked.connect(lambda: self.pressionado("0"))
        self.ui.um_botao.clicked.connect(lambda: self.pressionado("1"))
        self.ui.dois_botao.clicked.connect(lambda: self.pressionado("2"))
        self.ui.tres_botao.clicked.connect(lambda: self.pressionado("3"))
        self.ui.quatro_botao.clicked.connect(lambda: self.pressionado("4"))
        self.ui.cinco_botao.clicked.connect(lambda: self.pressionado("5"))
        self.ui.seis_botao.clicked.connect(lambda: self.pressionado("6"))
        self.ui.sete_botao.clicked.connect(lambda: self.pressionado("7"))
        self.ui.oito_botao.clicked.connect(lambda: self.pressionado("8"))
        self.ui.nove_botao.clicked.connect(lambda: self.pressionado("9"))
        self.ui.virgulabotao.clicked.connect(lambda: self.pressionado(","))
        self.ui.multiplicacaobotao.clicked.connect(lambda: self.pressionado("*"))
        self.ui.subtracaobotao.clicked.connect(lambda: self.pressionado("-"))
        self.ui.adicao_botao.clicked.connect(lambda: self.pressionado("+"))
        self.ui.divisaoBotao.clicked.connect(lambda: self.pressionado("/"))
        self.ui.porcentagembotao.clicked.connect(lambda: self.pressionado("%"))
        self.ui.clearBottom.clicked.connect(lambda: self.backspace())
        self.ui.clearAllBottom.clicked.connect(lambda: self.clearAllOutput())
        self.ui.igualbotao.clicked.connect(lambda: self.resultado())

    def pressionado(self, tecla):
        saida = self.ui.outputLabel.text()
        if tecla == "," and "," in saida:
            return
        if saida == "0":
            saida = " "
        if tecla in ["+", "-", "*", "/", ","] and saida[-1] in ["+", "-", "*", "/", ","]:
            saida = saida[:-1]
        saida += tecla
        self.ui.outputLabel.setText(saida)

    def resultado(self):
        saida = self.ui.outputLabel.text()
        try:
            resposta = eval(saida)
            self.ui.outputLabel.setText(f"{resposta}")
            if saida == "%":
                saida /= 100
        except:
            self.ui.outputLabel.setText("ERRO")
            

    def backspace(self):
        saida = self.ui.outputLabel.text()
        self.ui.outputLabel.setText(saida[:-1])
        if not len(saida[:-1]):
            self.clearAllOutput()

    def clearAllOutput(self):
        self.ui.outputLabel.setText(" ")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())