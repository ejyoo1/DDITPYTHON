import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui 
from PyQt5.Qt import QSize, QRect

form_class = uic.loadUiType("./myqt02_omk.ui")[0]

# getLE, getRI 왼쪽 오른쪽
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
        self.flag_wb = False
        
        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
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
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0:
            return
                
        stone = 0
        if self.flag_wb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.getUP(i,j,stone)
        dw = self.getDW(i,j,stone)
        le = self.getLE(i,j,stone)
        ri = self.getRI(i,j,stone)
        ur = self.getRI(i,j,stone) #오른쪽 위
        dl = self.getRI(i,j,stone) #왼쪽 아래
        print("le:",le,"ri",ri)
        
        self.myrander()
        self.flag_wb = not self.flag_wb
    
    def getUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                print(i)
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def getDW(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def getLE(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def getRI(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()