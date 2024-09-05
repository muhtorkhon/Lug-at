from PyQt5.QtWidgets import *

class AddWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size:20px")
        self.setFixedSize(400,500)
        self.v_main_lay = QVBoxLayout()
        self.h_edit_btn_lay = QHBoxLayout()
        self.v_edit_lay = QVBoxLayout()

        self.en_edit = QLineEdit()
        self.en_edit.setPlaceholderText("Eng...")

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("Uzb...")

        self.ok_btn = QPushButton("OK", clicked=self.Ok)
        self.lbl = QLabel()
        self.menu_btn = QPushButton("MENU", clicked=self.hide)

        self.v_edit_lay.addWidget(self.en_edit)
        self.v_edit_lay.addWidget(self.uz_edit)

        self.h_edit_btn_lay.addLayout(self.v_edit_lay)
        self.h_edit_btn_lay.addWidget(self.ok_btn)

        self.v_main_lay.addLayout(self.h_edit_btn_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)

    def Ok(self):
        f = open("lugat.txt", "a+")
        f.seek(0)
        matn = f.read()
        eng = self.en_edit.text()
        uzb = self.uz_edit.text()
        if f"{eng}-{uzb}".lower() not in matn.lower():
            f.write(f"{eng}-{uzb}\n")
            self.lbl.setStyleSheet("background-color: lightgreen")
            self.lbl.setText("Successfully Added")
            self.en_edit.clear()
            self.uz_edit.clear()
        else:
            self.lbl.setStyleSheet("background-color: red")
            self.lbl.setText("Dublicate Word")
        f.close()