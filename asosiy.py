from PyQt5.QtWidgets import *

from add import AddWindow
from search import Search
from list import Mylist

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menyu")
        self.setStyleSheet("background-color:blue; color:white; font-size:20px")
        self.setFixedSize(400,500)
        self.h_main_lay = QHBoxLayout()
        self.v_btn_lay = QVBoxLayout()

        self.add_btn = QPushButton("ADD", clicked=self.Add)
        self.add_btn.setStyleSheet("background-color:lightblue; color:black")
        self.search_btn = QPushButton("\U0001F50DSEARCH", clicked=self.Search)
        self.search_btn.setStyleSheet("background-color:lightblue; color:black")
        self.list_btn = QPushButton("\U0001F4C3 LIST", clicked=self.List)
        self.list_btn.setStyleSheet("background-color:lightblue; color:black")
        self.exit_btn = QPushButton("EXIT", clicked=exit)
        self.exit_btn.setStyleSheet("background-color:lightblue; color:black")

        self.v_btn_lay.addWidget(self.add_btn)
        self.v_btn_lay.addWidget(self.search_btn)
        self.v_btn_lay.addWidget(self.list_btn)
        self.v_btn_lay.addWidget(self.exit_btn)

        self.h_main_lay.addStretch()
        self.h_main_lay.addLayout(self.v_btn_lay)
        self.h_main_lay.addStretch()

        self.setLayout(self.h_main_lay)
    
    def Add(self):
        self.add_window = AddWindow()
        self.add_window.show()

    def Search(self):
        self.srch_win = Search()
        self.srch_win.show()

    def List(self):
        self.lts_win = Mylist()
        self.lts_win.show()
