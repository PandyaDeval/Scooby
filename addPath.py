from PyQt5 import QtCore, QtGui, QtWidgets
from pywinauto.keyboard import SendKeys
class Ui_AddPath(object):

    def addclick(self):
        valueName = self.aName.text()
        valuePath = self.aPath.text()
        with open("paths.txt","a") as file:
            file.write(valueName+'-'+valuePath+'\n')
        SendKeys("%{F4}")
       

    def setupUi(self, AddPath):
        AddPath.setObjectName("AddPath")
        AddPath.resize(502, 212)
        self.centralwidget = QtWidgets.QWidget(AddPath)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 31)) 
        self.label.setObjectName("label")
        self.aName = QtWidgets.QLineEdit(self.centralwidget)
        self.aName.setGeometry(QtCore.QRect(150, 20, 281, 31))
        self.aName.setObjectName("aName")
        self.aPath = QtWidgets.QLineEdit(self.centralwidget)
        self.aPath.setGeometry(QtCore.QRect(150, 90, 281, 31))
        self.aPath.setObjectName("aPath")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 61, 21))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 24\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addclick)
        AddPath.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddPath)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        AddPath.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddPath)
        self.statusbar.setObjectName("statusbar")
        AddPath.setStatusBar(self.statusbar)
        


        self.retranslateUi(AddPath)
        QtCore.QMetaObject.connectSlotsByName(AddPath)

    def retranslateUi(self, AddPath):
        _translate = QtCore.QCoreApplication.translate
        AddPath.setWindowTitle(_translate("AddPath", "MainWindow"))
        self.label.setText(_translate("AddPath", "<html><head/><body><p><span style=\" font-size:16pt;\">Name :</span></p></body></html>"))
        self.label_2.setText(_translate("AddPath", "Path    :"))
        self.pushButton.setText(_translate("AddPath", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPath = QtWidgets.QMainWindow()
    ui = Ui_AddPath()
    ui.setupUi(AddPath)
    AddPath.show()
    sys.exit(app.exec_())

