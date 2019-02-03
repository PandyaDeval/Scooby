
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangePath(object):
    def setupUi(self, ChangePath):
        ChangePath.setObjectName("ChangePath")
        ChangePath.resize(501, 214)
        self.centralwidget = QtWidgets.QWidget(ChangePath)
        self.centralwidget.setObjectName("centralwidget")
        self.cPath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cPath.setGeometry(QtCore.QRect(180, 80, 281, 31))
        self.cPath.setObjectName("cPath")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 81, 31))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.cName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cName.setGeometry(QtCore.QRect(180, 20, 281, 31))
        self.cName.setObjectName("cName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 140, 91, 31))
        self.pushButton.setObjectName("pushButton")
        ChangePath.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChangePath)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.menubar.setObjectName("menubar")
        ChangePath.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChangePath)
        self.statusbar.setObjectName("statusbar")
        ChangePath.setStatusBar(self.statusbar)

        self.retranslateUi(ChangePath)
        QtCore.QMetaObject.connectSlotsByName(ChangePath)

    def retranslateUi(self, ChangePath):
        _translate = QtCore.QCoreApplication.translate
        ChangePath.setWindowTitle(_translate("ChangePath", "MainWindow"))
        self.label.setText(_translate("ChangePath", "Path :"))
        self.label_2.setText(_translate("ChangePath", "<html><head/><body><p><span style=\" font-size:16pt;\">Name :</span></p></body></html>"))
        self.pushButton.setText(_translate("ChangePath", "Change"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePath = QtWidgets.QMainWindow()
    ui = Ui_ChangePath()
    ui.setupUi(ChangePath)
    ChangePath.show()
    sys.exit(app.exec_())

