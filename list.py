from PyQt5.QtWidgets import *
class Mylist(QListWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,500)
        self.setWindowTitle("\U0001F4C3 Lug'at")
        self.setStyleSheet("background-color:purple; color:yellow; font-size:20px")
        self.menyu_btn = QPushButton("Menyu",clicked=self.menyu)
        self.h_lts_lyt = QHBoxLayout()
        self.menyu_btn.setStyleSheet("background-color:yellow; color: red") 
        self.h_lts_lyt.addStretch()
        self.h_lts_lyt.addWidget(self.menyu_btn)

        self.setLayout(self.h_lts_lyt)
        
        f = open("lugat.txt")
        lts = []
        for i in f.read().split("\n"):
            lts.append(i)
        self.addItems(lts)

    def menyu(self):
        self.hide()

      

