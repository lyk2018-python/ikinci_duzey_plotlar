# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Wed Aug  1 02:03:29 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 790)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.all_of_them = QtWidgets.QPushButton(self.centralwidget)
        self.all_of_them.setGeometry(QtCore.QRect(10, 690, 221, 81))
        self.all_of_them.setObjectName("all_of_them")
        self.exchange_screen = QtWidgets.QLabel(self.centralwidget)
        self.exchange_screen.setGeometry(QtCore.QRect(10, 20, 731, 581))
        self.exchange_screen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exchange_screen.setText("")
        self.exchange_screen.setObjectName("exchange_screen")
        self.dolar = QtWidgets.QPushButton(self.centralwidget)
        self.dolar.setGeometry(QtCore.QRect(250, 640, 171, 51))
        self.dolar.setObjectName("dolar")
        self.euro = QtWidgets.QPushButton(self.centralwidget)
        self.euro.setGeometry(QtCore.QRect(480, 640, 171, 51))
        self.euro.setObjectName("euro")
        self.AUD = QtWidgets.QPushButton(self.centralwidget)
        self.AUD.setGeometry(QtCore.QRect(250, 700, 201, 51))
        self.AUD.setObjectName("AUD")
        self.DKK = QtWidgets.QPushButton(self.centralwidget)
        self.DKK.setGeometry(QtCore.QRect(470, 700, 201, 51))
        self.DKK.setObjectName("DKK")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.all_of_them.setText(QtWidgets.QApplication.translate("MainWindow", "ALL EXCANGE RATES", None, -1))
        self.dolar.setText(QtWidgets.QApplication.translate("MainWindow", "DOLAR", None, -1))
        self.euro.setText(QtWidgets.QApplication.translate("MainWindow", "EURO", None, -1))
        self.AUD.setText(QtWidgets.QApplication.translate("MainWindow", "AVUSTRALYA DOLARI", None, -1))
        self.DKK.setText(QtWidgets.QApplication.translate("MainWindow", "DANİMARKA KRONU", None, -1))

