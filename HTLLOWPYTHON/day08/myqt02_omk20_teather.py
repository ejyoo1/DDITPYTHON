import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtWidgets 
from PyQt5.Qt import QSize, QRect

form_class = uic.loadUiType("./myqt02_omk.ui")[0]

# getUR, getDL 오른쪽 위, 왼쪽 아래
class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__()
        self.column = 19
        self.setupUi(self)
        self.arr2D = [[0 for i in range(self.column)] for j in range(self.column)] 
        self.pb2D = []
        self.setIconType = 0
        self.flag_wb = False
        self.flag_ing = True
        
        for i in range(self.column):
            pb_line = []
            for j in range(self.column):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect(j*40,i*40,40,40))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
        
        self.pb_reset.clicked.connect(self.btnReset)

        self.myrander()
        
    def btnReset(self):
        self.flag_wb = False
        self.flag_ing = True
        for i in range(self.column):
            for j in range(self.column):
                self.arr2D[i][j] = 0
        self.myrander()    
        
      
    def myrander(self):
        for i in range(self.column): # 얖은 복사 깊은복사 개념
            for j in range(self.column):
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
    
      
    def btnClick(self):
        if not self.flag_ing:
            return
            
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
        ur = self.getUR(i,j,stone) #오른쪽 위
        dl = self.getDL(i,j,stone) #왼쪽 아래
        ul = self.getUL(i,j,stone) #오른쪽 위
        dr = self.getDR(i,j,stone) #왼쪽 아래
        
        d1 = up + 1 + dw
        d2 = le + 1 + ri
        d3 = ur + 1 + dl
        d4 = ul + 1 + dr
        
        
        self.myrander()
        
        if d1==5 or d2==5 or d3==5 or d4==5:
            if self.flag_wb:
                QtWidgets.QMessageBox.information(self, "오목", "흑돌이 이겼습니다.")
            else:
                QtWidgets.QMessageBox.information(self, "오목", "백돌이 이겼습니다.")
            self.flag_ing = False
        
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
    
    def getUR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
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
        
    def getDL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
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
    
    def getUL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
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
        
    def getDR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
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