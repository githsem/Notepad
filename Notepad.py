import sys
import os


from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")



app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec_())