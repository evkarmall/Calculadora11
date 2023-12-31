# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setMinimumSize(QtCore.QSize(400, 650))
        MainWindow.setMaximumSize(QtCore.QSize(400, 650))
        MainWindow.setStyleSheet("background-color: rgb(207, 253, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 650))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 650))
        self.centralwidget.setObjectName("centralwidget")
        self.VisorCalculadora = QtWidgets.QFrame(self.centralwidget)
        self.VisorCalculadora.setEnabled(True)
        self.VisorCalculadora.setGeometry(QtCore.QRect(0, 0, 400, 150))
        self.VisorCalculadora.setMinimumSize(QtCore.QSize(400, 150))
        self.VisorCalculadora.setMaximumSize(QtCore.QSize(400, 150))
        self.VisorCalculadora.setStyleSheet("font: 80 40pt \"Arial Black\";\n"
"background-color: #DAA520;\n"
"color: #fff;")
        self.VisorCalculadora.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VisorCalculadora.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VisorCalculadora.setObjectName("VisorCalculadora")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.VisorCalculadora)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputLabel = QtWidgets.QLabel(self.VisorCalculadora)
        self.outputLabel.setStyleSheet("font: 55pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout.addWidget(self.outputLabel, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 250, 400, 100))
        self.frame_2.setMinimumSize(QtCore.QSize(400, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(400, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sete_botao = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sete_botao.setFont(font)
        self.sete_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.sete_botao.setObjectName("sete_botao")
        self.horizontalLayout_2.addWidget(self.sete_botao)
        self.oito_botao = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.oito_botao.setFont(font)
        self.oito_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.oito_botao.setObjectName("oito_botao")
        self.horizontalLayout_2.addWidget(self.oito_botao)
        self.nove_botao = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nove_botao.setFont(font)
        self.nove_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.nove_botao.setObjectName("nove_botao")
        self.horizontalLayout_2.addWidget(self.nove_botao)
        self.multiplicacaobotao = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.multiplicacaobotao.setFont(font)
        self.multiplicacaobotao.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 40pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.multiplicacaobotao.setObjectName("multiplicacaobotao")
        self.horizontalLayout_2.addWidget(self.multiplicacaobotao)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 350, 400, 100))
        self.frame_3.setMinimumSize(QtCore.QSize(400, 100))
        self.frame_3.setMaximumSize(QtCore.QSize(400, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.quatro_botao = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.quatro_botao.setFont(font)
        self.quatro_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.quatro_botao.setObjectName("quatro_botao")
        self.horizontalLayout_4.addWidget(self.quatro_botao)
        self.cinco_botao = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cinco_botao.setFont(font)
        self.cinco_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.cinco_botao.setObjectName("cinco_botao")
        self.horizontalLayout_4.addWidget(self.cinco_botao)
        self.seis_botao = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.seis_botao.setFont(font)
        self.seis_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.seis_botao.setObjectName("seis_botao")
        self.horizontalLayout_4.addWidget(self.seis_botao)
        self.subtracaobotao = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.subtracaobotao.setFont(font)
        self.subtracaobotao.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 40pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.subtracaobotao.setObjectName("subtracaobotao")
        self.horizontalLayout_4.addWidget(self.subtracaobotao)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 450, 400, 100))
        self.frame_4.setMinimumSize(QtCore.QSize(400, 100))
        self.frame_4.setMaximumSize(QtCore.QSize(400, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.um_botao = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.um_botao.setFont(font)
        self.um_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.um_botao.setObjectName("um_botao")
        self.horizontalLayout_5.addWidget(self.um_botao)
        self.dois_botao = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dois_botao.setFont(font)
        self.dois_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.dois_botao.setObjectName("dois_botao")
        self.horizontalLayout_5.addWidget(self.dois_botao)
        self.tres_botao = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tres_botao.setFont(font)
        self.tres_botao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.tres_botao.setObjectName("tres_botao")
        self.horizontalLayout_5.addWidget(self.tres_botao)
        self.adicao_botao = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.adicao_botao.setFont(font)
        self.adicao_botao.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 40pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.adicao_botao.setObjectName("adicao_botao")
        self.horizontalLayout_5.addWidget(self.adicao_botao)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 550, 400, 100))
        self.frame_5.setMinimumSize(QtCore.QSize(400, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(400, 100))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.zerobotao = QtWidgets.QPushButton(self.frame_5)
        self.zerobotao.setGeometry(QtCore.QRect(10, 15, 191, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.zerobotao.setFont(font)
        self.zerobotao.setStyleSheet("border-radius: 20px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.zerobotao.setObjectName("zerobotao")
        self.virgulabotao = QtWidgets.QPushButton(self.frame_5)
        self.virgulabotao.setGeometry(QtCore.QRect(220, 10, 71, 70))
        self.virgulabotao.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semiligh")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.virgulabotao.setFont(font)
        self.virgulabotao.setStyleSheet("border-radius: 18px;\n"
"background-color: #F0F8FF;\n"
"font: 40pt \"Segoe UI Variable Text Semiligh\";")
        self.virgulabotao.setObjectName("virgulabotao")
        self.igualbotao = QtWidgets.QToolButton(self.frame_5)
        self.igualbotao.setGeometry(QtCore.QRect(299, 11, 91, 77))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.igualbotao.setFont(font)
        self.igualbotao.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 40pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.igualbotao.setObjectName("igualbotao")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 150, 400, 100))
        self.frame.setMinimumSize(QtCore.QSize(400, 100))
        self.frame.setMaximumSize(QtCore.QSize(400, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.clearBottom = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.clearBottom.setFont(font)
        self.clearBottom.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: #D3D3D3;\n"
"font: 75 30pt \"MS Shell Dlg 2\";\n"
"border-radius: 22px;")
        self.clearBottom.setObjectName("clearBottom")
        self.gridLayout.addWidget(self.clearBottom, 0, 0, 1, 1)
        self.clearAllBottom = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.clearAllBottom.setFont(font)
        self.clearAllBottom.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: #D3D3D3;\n"
"font: 75 30pt \"MS Shell Dlg 2\";\n"
"border-radius: 22px;")
        self.clearAllBottom.setObjectName("clearAllBottom")
        self.gridLayout.addWidget(self.clearAllBottom, 0, 1, 1, 1)
        self.porcentagembotao = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.porcentagembotao.setFont(font)
        self.porcentagembotao.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: #D3D3D3;\n"
"font: 75 30pt \"MS Shell Dlg 2\";\n"
"border-radius: 22px;")
        self.porcentagembotao.setObjectName("porcentagembotao")
        self.gridLayout.addWidget(self.porcentagembotao, 0, 2, 1, 1)
        self.divisaoBotao = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.divisaoBotao.setFont(font)
        self.divisaoBotao.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 40pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.divisaoBotao.setObjectName("divisaoBotao")
        self.gridLayout.addWidget(self.divisaoBotao, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CalculadoraPython"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.sete_botao.setText(_translate("MainWindow", "7"))
        self.oito_botao.setText(_translate("MainWindow", "8"))
        self.nove_botao.setText(_translate("MainWindow", "9"))
        self.multiplicacaobotao.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.multiplicacaobotao.setText(_translate("MainWindow", "x"))
        self.quatro_botao.setText(_translate("MainWindow", "4"))
        self.cinco_botao.setText(_translate("MainWindow", "5"))
        self.seis_botao.setText(_translate("MainWindow", "6"))
        self.subtracaobotao.setText(_translate("MainWindow", "-"))
        self.um_botao.setText(_translate("MainWindow", "1"))
        self.dois_botao.setText(_translate("MainWindow", "2"))
        self.tres_botao.setText(_translate("MainWindow", "3"))
        self.adicao_botao.setText(_translate("MainWindow", "+"))
        self.zerobotao.setText(_translate("MainWindow", "0"))
        self.virgulabotao.setText(_translate("MainWindow", ","))
        self.igualbotao.setText(_translate("MainWindow", "="))
        self.clearBottom.setText(_translate("MainWindow", "CE"))
        self.clearAllBottom.setText(_translate("MainWindow", "C"))
        self.porcentagembotao.setText(_translate("MainWindow", "%"))
        self.divisaoBotao.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

