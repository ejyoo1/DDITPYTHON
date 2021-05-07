import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 

form_class = uic.loadUiType("./myqt03.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        self.pb_2.clicked.connect(self.btnClick2)
        self.pb_3.clicked.connect(self.btnClick3)
        self.pb_4.clicked.connect(self.btnClick4)

        
    def btnClick(self):
        le1 = self.le1.text()
        le2 = self.le2.text()
        
        sum = int(le1) + int(le2)
        
        self.le3.setText(str(sum))
    
    def btnClick2(self):  
        le1_2 = self.le1_2.text()
        le2_2 = self.le2_2.text()  
        
        sub = int(le1_2) - int(le2_2)
        
        self.le3_2.setText(str(sub))
        
    def btnClick3(self):  
        le1_3 = self.le1_3.text()
        le2_3 = self.le2_3.text()  
        
        div = int(le1_3) * int(le2_3)
        
        self.le3_3.setText(str(div))
    
    def btnClick4(self):  
        le1_4 = self.le1_4.text()
        le2_4 = self.le2_4.text()  
        
        mul = int(le1_4) / int(le2_4)
        
        self.le3_4.setText(str(mul))
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()