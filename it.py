import cv2
import pytesseract

from PyQt5 import QtCore, QtGui, QtWidgets


pdfButtonStyle = "border:1px solid red; color: white"
txtButtonStyle = "border:1px solid red; color: white"
sucessButtonStyle = "border:1px solid red; color: white"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 619)
        MainWindow.setStyleSheet("background-image:url('bg.jpg');")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.txtButton = QtWidgets.QToolButton(self.centralwidget)
        self.txtButton.setGeometry(QtCore.QRect(150, 260, 101, 41))
        self.txtButton.setObjectName("txt Button")
        self.txtButton.setStyleSheet(txtButtonStyle)


        self.pdfButton = QtWidgets.QToolButton(self.centralwidget)
        self.pdfButton.setGeometry(QtCore.QRect(320, 260, 91, 41))
        self.pdfButton.setObjectName("pdf button")
        self.pdfButton.setStyleSheet(pdfButtonStyle)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image to Text or PDF"))
        self.txtButton.setText(_translate("MainWindow", "Image to text"))
        self.txtButton.clicked.connect(self.clickimgtoText)
        self.pdfButton.setText(_translate("MainWindow", "Image to PDF"))
        self.pdfButton.clicked.connect(self.clickimgtoPDF)



    def sucessButtonCall(self):
        _translate = QtCore.QCoreApplication.translate
        self.sucessButton = QtWidgets.QWidget
        self.sucessButton = QtWidgets.QToolButton(self.centralwidget)
        self.sucessButton.setGeometry(QtCore.QRect(250, 180, 91, 41))
        self.sucessButton.setObjectName("sucessButton")
        self.sucessButton.setStyleSheet(sucessButtonStyle)
        self.sucessButton.setText(_translate("MainWindow","Converted Succesfully"))



    def clickimgtoPDF(self):
        imgtoPDF()
        self.sucessButtonCall()



        
    def clickimgtoText(self):
        imgtoText()
        self.sucessButtonCall()
        
        
def imgtoText():
    img = cv2.imread('H:\\teste\\1.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # need to encode the image to RGB, it is how opencv works
    txt = pytesseract.image_to_string(img)
    print(txt)
    f = open("result.txt", "w")
    f.write(txt)
    f.close()
    



def imgtoPDF():
    img = cv2.imread('H:\\teste\\1.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # need to encode the image to RGB, it is how opencv works
    pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
    with open('test.pdf', 'w+b') as f:
        f.write(pdf)


if __name__ == "__main__":
    import sys

    pytesseract.pytesseract.tesseract_cmd = 'H:\\Tesseract-Ocr\\tesseract.exe'
    # tessdata_dir_config = '--tessdata-dir "<H:\\Tesseract-Ocr\\tessdata"'

    img = cv2.imread('H:\\teste\\1.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # need to encode the image to RGB, it is how opencv works
    # cv2.imshow("Result", img) #show the image to see if everything is ok
    # cv2.waitKey(0)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
