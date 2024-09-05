from PyQt5.QtWidgets import *
from add import AddWindow
class Search(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color:blue; color:white; font-size:20px")
        self.setWindowTitle("\U0001F50DSearch")
        self.setFixedSize(400,500)
        self.v_main_lyt = QVBoxLayout()
        self.h_radio_lyt = QHBoxLayout()
        self.h_edit_lyt = QHBoxLayout()
        self.h_btn_lyt = QHBoxLayout()
        self.h_lbl_lyt = QHBoxLayout()

        self.radioE = QRadioButton("En")

        self.radioU = QRadioButton("Uz")

        self.srch_edit = QLineEdit()
        
        self.srch_btn = QPushButton("Search",clicked=self.srchMetod)
        self.srch_btn.setStyleSheet("background-color:lightblue; color:black")
        
        self.lbl = QLabel()

        self.menyu = QPushButton("Menyu",clicked=self.menyus)
        self.menyu.setStyleSheet("background-color:lightblue; color:black")
        self.add = QPushButton("Add",clicked=self.newWord)
        self.add.setStyleSheet("background-color:lightblue; color:black")

        self.h_radio_lyt.addWidget(self.radioE)
        self.h_radio_lyt.addWidget(self.radioU)

        self.h_edit_lyt.addWidget(self.srch_edit)
        self.h_edit_lyt.addWidget(self.srch_btn)

        self.h_btn_lyt.addWidget(self.menyu)
        self.h_btn_lyt.addWidget(self.add)
        self.add.hide()

        self.h_lbl_lyt.addStretch()
        self.h_lbl_lyt.addWidget(self.lbl)
        self.h_lbl_lyt.addStretch()

        self.v_main_lyt.addLayout(self.h_radio_lyt)
        self.v_main_lyt.addLayout(self.h_edit_lyt)
        self.v_main_lyt.addLayout(self.h_lbl_lyt)
        self.v_main_lyt.addLayout(self.h_btn_lyt)

        self.setLayout(self.v_main_lyt)

    def srchMetod(self):
        f = open("lugat.txt")
        f.seek(0)
        lts = []
        for i in f.read().split("\n"):
            if "-" in i:
                lts.append(" ".join(i.split("-")))
                eng = i.split("-")
                if self.radioE.isChecked():
                    if eng[0] == self.srch_edit.text():
                        self.lbl.setText(eng[1])
                if self.radioU.isChecked():
                    
                    if eng[1] == self.srch_edit.text():
                        self.lbl.setText(eng[0])   
        satr = " ".join(lts)
        if self.srch_edit.text() not in satr:
            self.add.show()
    def newWord(self):
        self.hide()
        self.add_window = AddWindow()
        self.add_window.show()
    def menyus(self):
        self.hide()
       


