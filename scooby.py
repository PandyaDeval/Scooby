from PyQt5 import QtCore, QtGui, QtWidgets
from addPath import Ui_AddPath
from changePath import Ui_ChangePath

class Ui_MainWindow(object):
    
    def addPath_func(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddPath()
        self.ui.setupUi(self.window)
        self.window.show()
    def changePath_func(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChangePath()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 968)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 800, 121, 51))
        self.pushButton.setStyleSheet("font: 10pt \"Arial\";\n"
"font: 75 16pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 05);")
        self.pushButton.clicked.connect(self.nlp_file)   #new line enetered 
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, -10, 411, 111))
        self.label.setStyleSheet("font: italic 50pt  \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255,255);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdd_Path = QtWidgets.QAction(MainWindow)
        self.actionAdd_Path.setObjectName("actionAdd_Path")
        self.menuFile.triggered[QtWidgets.QAction].connect(self.addPath_func)
        self.actionChange_Path = QtWidgets.QAction(MainWindow)
        self.actionChange_Path.setObjectName("actionChange_Path")
        self.menuFile.addAction(self.actionAdd_Path)
        self.menuFile.addAction(self.actionChange_Path)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click Here!"))
        self.label.setText(_translate("MainWindow", "Hey Scooby!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd_Path.setText(_translate("MainWindow", "Add Path"))
        self.actionChange_Path.setText(_translate("MainWindow", "Change Path"))


    def nlp_file(self):  # new func defined
        import nlp

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

