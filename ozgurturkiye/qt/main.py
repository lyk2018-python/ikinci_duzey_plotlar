"""
İhtiyaç olan untitled dosyası için şu komut ile untitled.ui'den untitled.py oluşturabiliriz

$ pyside2-uic -o untitled.py untitled.ui
"""

from PySide2 import QtCore, QtWidgets

from mychallenge.untitled import Ui_MainWindow

import requests


class CustomWindow(Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.islem = []

    def center(self, MainWindow):
        """credits to https://gist.github.com/saleph/163d73e0933044d0e2c4"""
        qr = MainWindow.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.center(MainWindow)

        QtCore.QObject.connect(self.all_of_them, QtCore.SIGNAL("clicked()"), self.get_doviz)
        QtCore.QObject.connect(self.dolar, QtCore.SIGNAL("clicked()"), self.get_dolar)
        QtCore.QObject.connect(self.euro, QtCore.SIGNAL("clicked()"), self.get_euro)
        QtCore.QObject.connect(self.AUD, QtCore.SIGNAL("clicked()"), self.get_generic_aud)
        QtCore.QObject.connect(self.DKK, QtCore.SIGNAL("clicked()"), self.get_generic_dkk)

    def veri_yaz(self, sunucu_cevap):
        self.exchange_screen.setText(sunucu_cevap.text)

    def get_doviz(self):
        self.r = requests.get('http://127.0.0.1:5000/exchange_rates')
        self.veri_yaz(self.r)

    def get_dolar(self):
        self.r = requests.get('http://127.0.0.1:5000/dolar')
        self.veri_yaz(self.r)

    def get_euro(self):
        self.r = requests.get('http://127.0.0.1:5000/euro')
        self.veri_yaz(self.r)

    def get_generic_aud(self):
        self.r = requests.get('http://127.0.0.1:5000/AUD')
        self.veri_yaz(self.r)

    def get_generic_dkk(self):
        self.r = requests.get('http://127.0.0.1:5000/DKK')
        self.veri_yaz(self.r)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CustomWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())