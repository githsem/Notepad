import sys

from  PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Duzenle")

        dosya_ac = QAction("Dosya Ac",self)
        

        self.setWindowTitle("Menuler")

        self.show()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
