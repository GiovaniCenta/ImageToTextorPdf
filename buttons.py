import cv2
import pytesseract

from PyQt5 import QtCore, QtGui, QtWidgets


class SucessButton(QtWidgets.QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Converted Succesfully")
        self.resize(183, 173)
        self.setStyleSheet("Background-color:Purple")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.pushButton.setStyleSheet("background-color:white")
        self.pushButton.setObjectName("ok")
        self.pushButton.clicked.connect(self.closeAction)

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 70, 75, 23))
        self.pushButton_2.setStyleSheet("background-color:white;")
        self.pushButton_2.setObjectName("openexplorer")
        self.pushButton.clicked.connect(self.explorerAction)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Converted Succesfully!"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton_2.setText(_translate("Dialog", "Open Explorer"))

    def closeAction(self):
        print("hello")
        self.close()

    def explorerAction(self):
        self.w = App()
        self.w.show()
        self.close()


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.close()


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName








