# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scooby.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from addPath import Ui_AddPath
from changePath import Ui_ChangePath

class Ui_MainWindow(object):

	def addPath_func(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_AddPath()
		self.ui.setupUi(self.window)
		self.window.show()
	def deletePath_func(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_ChangePath()
		self.ui.setupUi(self.window)
		self.window.show()
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1200, 1200)
		MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
		"background-color: rgb(255, 255, 255);\n"
		"")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(380, 800, 281, 51))
		self.pushButton.setStyleSheet("font: 10pt \"Arial\";\n"
		"font: 75 16pt \"Arial\";\n"
		"background-color: rgb(255, 255, 255);\n"
		"color: rgb(0, 0, 05);")
		self.pushButton.setObjectName("pushButton")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(220, -10, 621, 111))
		self.label.setStyleSheet("font: italic 50pt  \"Comic Sans MS\";\n"
		"color: rgb(0, 0, 0);\n"
		"background-color: rgb(255, 255,255);")
		self.label.setObjectName("label")
		self.addPathButton = QtWidgets.QPushButton(self.centralwidget)
		self.addPathButton.setGeometry(QtCore.QRect(80, 240, 93, 28))
		self.addPathButton.setObjectName("addPathButton")
		self.deletePathButton = QtWidgets.QPushButton(self.centralwidget)
		self.deletePathButton.setGeometry(QtCore.QRect(80, 310, 93, 28))
		self.deletePathButton.setObjectName("deletePathButton")
		self.viewPathbutton = QtWidgets.QPushButton(self.centralwidget)
		self.viewPathbutton.setGeometry(QtCore.QRect(780, 290, 93, 28))
		self.viewPathbutton.setObjectName("viewPathbutton")
		self.pushButton.clicked.connect(self.nlp_file) 
		self.addPathButton.clicked.connect(self.addPath_func) 
		self.deletePathButton.clicked.connect(self.deletePath_func) 
		self.viewPathbutton.clicked.connect(self.nlp_file) 
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 1002, 26))
		self.menuBar.setObjectName("menuBar")
		self.menuFile = QtWidgets.QMenu(self.menuBar)
		self.menuFile.setObjectName("menuFile")
		self.menuHelp = QtWidgets.QMenu(self.menuBar)
		self.menuHelp.setObjectName("menuHelp")
		MainWindow.setMenuBar(self.menuBar)
		self.actionAdd_Path = QtWidgets.QAction(MainWindow)
		self.actionAdd_Path.setObjectName("actionAdd_Path")
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
		self.label.setText(_translate("MainWindow", "Hey Scooby !"))
		self.addPathButton.setText(_translate("MainWindow", "AddPath"))
		self.deletePathButton.setText(_translate("MainWindow", "DeletePath"))
		self.viewPathbutton.setText(_translate("MainWindow", "ViewPath"))
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

