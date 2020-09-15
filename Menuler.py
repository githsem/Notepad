import sys

from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Duzenle")

        dosya_ac = QAction("Dosya Ac", self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Cikis", self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        ara_ve_degistir = duzenle.addMenu("Ara ve Degistir")
        ara = QAction("Ara", self)
        degistir = QAction("Duzenle", self)
        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)

        temizle =QAction("Temizle", self)
        duzenle.addAction(temizle)

        cikis.triggered.connect(self.cikis_yap)
        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menuler")

        self.show()
    def cikis_yap(self):
        qApp.quit()
    def response(self,action):
        if action.text() == "Dosya Ac":
            print("Dosya Acildi...")
        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydedildi...")
        elif action.text() == "Cikis":
            print("Dosyadan Cikildi...")

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
