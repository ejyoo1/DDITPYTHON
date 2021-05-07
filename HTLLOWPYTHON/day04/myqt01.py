import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 

form_class = uic.loadUiType("./myqt01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)

        
    def btnClick(self):
        print("버튼이 클릭되었습니다.")
        self.lbl.setText("GootEvening")
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()

# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("My First Application");
#         self.move(300,300)
#         self.resize(400,200)
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec())