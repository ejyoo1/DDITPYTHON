import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
import random

form_class = uic.loadUiType("./myqt05.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        mine = self.le1.text()
        com = ""
        result = ""
        
        rand = random.random()
        
        if rand < 0.5:
            com = "홀"
        else:
            com = "짝"
            
        if mine == com:
            result = "이김"
        else:
            result = "짐"
        
        self.le2.setText(com);
        self.le3.setText(result);

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()