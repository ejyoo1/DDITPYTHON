import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 

form_class = uic.loadUiType("./myqt08.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        dan = int(self.le.text())
        result = ""
        for i in range(1,10):
            result = str(dan) + " * " + str(i) + " = " + str((dan*i))
            self.te.append(result)

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()