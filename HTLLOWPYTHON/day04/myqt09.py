import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("./myqt09.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        
        self.pb1.clicked.connect(self.pb1Click)
        self.pb2.clicked.connect(self.pb2Click)
        self.pb3.clicked.connect(self.pb3Click)
        self.pb4.clicked.connect(self.pb4Click)
        self.pb5.clicked.connect(self.pb5Click)
        self.pb6.clicked.connect(self.pb6Click)
        self.pb7.clicked.connect(self.pb7Click)
        self.pb8.clicked.connect(self.pb8Click)
        self.pb9.clicked.connect(self.pb9Click)
        self.pb0.clicked.connect(self.pb0Click)
        self.pbcall.clicked.connect(self.pbcallClick)

    


    def pb1Click(self):
        str_new = self.pb1.text()
        leInputText(self, str_new)
    
    def pb2Click(self):
        str_new = self.pb2.text()
        leInputText(self, str_new)
    
    def pb3Click(self):
        str_new = self.pb3.text()
        leInputText(self, str_new)
        
    def pb4Click(self):
        str_new = self.pb4.text()
        leInputText(self, str_new)
        
    def pb5Click(self):
        str_new = self.pb5.text()
        leInputText(self, str_new)
        
    def pb6Click(self):
        str_new = self.pb6.text()
        leInputText(self, str_new)
        
    def pb7Click(self):
        str_new = self.pb7.text()
        leInputText(self, str_new)
        
    def pb8Click(self):
        str_new = self.pb8.text()
        leInputText(self, str_new)
        
    def pb9Click(self):
        str_new = self.pb9.text()
        leInputText(self, str_new)
        
    def pb0Click(self):
        str_new = self.pb0.text()
        leInputText(self, str_new)
        
    def pbcallClick(self):
        print("버튼을 클릭함")
        str_old = self.le.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        msg.setText(str_old)
        msg.setWindowTitle("메시지 박스")
        
        retval = msg.exec_()
        
def leInputText(self, str_new):
    str_old = self.le.text()
    self.le.setText(str_old + str_new)

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
