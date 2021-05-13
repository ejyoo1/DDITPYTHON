import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui 
from PyQt5.Qt import QSize, QRect

form_class = uic.loadUiType("./myqt02_omk.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.arr2D = [
                 [0,1,0,0,0, 0,0,0,0,0]
                ,[0,1,0,0,0, 0,0,0,0,0]
                ,[0,0,2,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
            ]
        self.pb2D = []
        self.setIconType = 0
        
        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
                tmp.setStatusTip("false")
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect(j*40,i*40,40,40))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
            
        self.myrander()
      
    def myrander(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
    
      
    def btnClick(self):
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        str_status = self.sender().statusTip()
        print(str_status, "false")
        if str_status == "false":
            if self.setIconType > 1:
                self.setIconType = 0
            self.setIconType += 1
            print(self.setIconType)
            self.setIconType %= 3
            self.arr2D[int(arr_ij[0])][int(arr_ij[1])] = self.setIconType
            self.pb2D[int(arr_ij[0])][int(arr_ij[1])].setStatusTip("True")
        else:
            print("바둑알 세팅 불가")
        
        self.myrander()

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()