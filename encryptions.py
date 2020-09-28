from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

import sdes
import Cesar
import des_
import aes
import xor


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(743, 299)
        self.encript = 1
        self.methods = {'sdes': {1: sdes.encript, 0: sdes.decript},
                        'cesar': {1: Cesar.encript, 0: Cesar.decript},
                        'aes': {1: aes.encript, 0: aes.decript},
                        'des': {1: des_.encript, 0: des_.decript},
                        'xor': {1: xor.encript, 0: xor.decript}}

        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.Mensagem_label = QtWidgets.QLabel(Dialog)
        self.Mensagem_label.setWordWrap(False)
        self.Mensagem_label.setObjectName("Mensagem_label")

        self.gridLayout_2.addWidget(self.Mensagem_label, 0, 0, 1, 2)

        self.Mensagem_textEdit = QtWidgets.QTextEdit(Dialog)
        self.Mensagem_textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Mensagem_textEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Mensagem_textEdit.setObjectName("Mensagem_textEdit")

        self.gridLayout_2.addWidget(self.Mensagem_textEdit, 1, 0, 1, 3)

        self.Chave_label = QtWidgets.QLabel(Dialog)
        self.Chave_label.setObjectName("Chave_label")

        self.gridLayout_2.addWidget(self.Chave_label, 2, 0, 1, 1)

        self.Chave_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.Chave_lineEdit.setObjectName("Chave_lineEdit")

        self.gridLayout_2.addWidget(self.Chave_lineEdit, 2, 1, 1, 2)

        self.Criptografar_rButton = QtWidgets.QRadioButton(Dialog)
        self.Criptografar_rButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Criptografar_rButton.setObjectName("Criptografar_rButton")
        self.Criptografar_rButton.clicked.connect(self.radio_button)

        self.gridLayout_2.addWidget(self.Criptografar_rButton, 3, 0, 1, 2)

        self.Descriptografar_rButton = QtWidgets.QRadioButton(Dialog)
        self.Descriptografar_rButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Descriptografar_rButton.setObjectName("Descriptografar_rButton")
        self.Descriptografar_rButton.clicked.connect(self.radio_button)

        self.gridLayout_2.addWidget(self.Descriptografar_rButton, 3, 2, 1, 1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.Cesar_Button = QtWidgets.QPushButton(Dialog)
        self.Cesar_Button.setMinimumSize(QtCore.QSize(93, 0))
        self.Cesar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cesar_Button.setObjectName("Cesar_Button")
        self.Cesar_Button.clicked.connect(self.botao_cesar_clicado)

        self.gridLayout.addWidget(self.Cesar_Button, 0, 0, 1, 1)

        self.Xor_Button = QtWidgets.QPushButton(Dialog)
        self.Xor_Button.setMinimumSize(QtCore.QSize(93, 0))
        self.Xor_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Xor_Button.setObjectName("Xor_Button")
        self.Xor_Button.clicked.connect(self.botao_xor_clicado)

        self.gridLayout.addWidget(self.Xor_Button, 0, 1, 1, 1)

        self.SDES_Button = QtWidgets.QPushButton(Dialog)
        self.SDES_Button.setMinimumSize(QtCore.QSize(93, 0))
        self.SDES_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SDES_Button.setObjectName("SDES_Button")
        self.SDES_Button.clicked.connect(self.botao_sdes_clicado)

        self.gridLayout.addWidget(self.SDES_Button, 0, 2, 1, 1)

        self.DES_Button = QtWidgets.QPushButton(Dialog)
        self.DES_Button.setMinimumSize(QtCore.QSize(93, 0))
        self.DES_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DES_Button.setObjectName("DES_Button")
        self.DES_Button.clicked.connect(self.botao_des_clicado)

        self.gridLayout.addWidget(self.DES_Button, 0, 3, 1, 1)

        self.AES_Button = QtWidgets.QPushButton(Dialog)
        self.AES_Button.setMinimumSize(QtCore.QSize(93, 0))
        self.AES_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AES_Button.setObjectName("AES_Button")
        self.AES_Button.clicked.connect(self.botao_aes_clicado)

        self.gridLayout.addWidget(self.AES_Button, 0, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Algoritmos de criptografias simétricos"))

        self.Mensagem_label.setText(_translate("Dialog", "Mensagem:"))
        self.Chave_label.setText(_translate("Dialog", "Chave:"))
        self.Criptografar_rButton.setText(_translate("Dialog", "Criptografar"))
        self.Descriptografar_rButton.setText(_translate("Dialog", "Descriptografar"))
        self.Cesar_Button.setText(_translate("Dialog", "Cesar"))
        self.Xor_Button.setText(_translate("Dialog", "Xor"))
        self.SDES_Button.setText(_translate("Dialog", "S-DES"))
        self.DES_Button.setText(_translate("Dialog", "DES"))
        self.AES_Button.setText(_translate("Dialog", "AES"))

    def call_encript(self, method, key, text, type):
        text = self.methods[method][type](key, text)
        return text

    def botao_cesar_clicado(self):
        texto = self.Mensagem_textEdit.toPlainText()
        chave = self.Chave_lineEdit.text()
        tipo = self.encript
        metodo = 'cesar'
        text_out = self.call_encript(metodo, chave, texto, tipo)
        self.Mensagem_textEdit.setText(text_out)

    def botao_xor_clicado(self):
        texto = self.Mensagem_textEdit.toPlainText()
        chave = self.Chave_lineEdit.text()
        tipo = self.encript
        metodo = 'xor'
        text_out = self.call_encript(metodo, chave, texto, tipo)
        self.Mensagem_textEdit.setText(text_out)

    def botao_sdes_clicado(self):
        texto = self.Mensagem_textEdit.toPlainText()
        chave = self.Chave_lineEdit.text()
        tipo = self.encript
        metodo = 'sdes'
        text_out = self.call_encript(metodo, chave, texto, tipo)
        self.Mensagem_textEdit.setText(text_out)

    def botao_des_clicado(self):
        texto = self.Mensagem_textEdit.toPlainText()
        chave = self.Chave_lineEdit.text()
        tipo = self.encript
        metodo = 'des'
        text_out = self.call_encript(metodo, chave, texto, tipo)
        self.Mensagem_textEdit.setText(text_out)

    def botao_aes_clicado(self):
        texto = self.Mensagem_textEdit.toPlainText()
        chave = self.Chave_lineEdit.text()
        tipo = self.encript
        metodo = 'aes'
        text_out = self.call_encript(metodo, chave, texto, tipo)
        self.Mensagem_textEdit.setText(text_out)

    def radio_button(self):
        if self.Criptografar_rButton.isChecked():
            # self.Mensagem_label.setText("Mensagem Criptografada: ")
            self.encript = 1
        elif self.Descriptografar_rButton.isChecked():
            # self.Mensagem_label.setText("Mensagem Descriptografada: ")
            self.encript = 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())