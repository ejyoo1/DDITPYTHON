import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui 

form_class = uic.loadUiType("./myqt01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.index = 0;
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        self.index += 1
        loc_index = self.index % 3
        self.pb.setIcon(QtGui.QIcon(str(loc_index)+'.png'))
        print("버튼이 클릭되었습니다.")

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()