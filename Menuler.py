import sys

from  PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Duzenle")

        dosya_ac = QAction("Dosya Ac",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Cikis",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        ara_ve_degistir = duzenle.addMenu("Ara ve Degistir")
        



        self.setWindowTitle("Menuler")

        self.show()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
