'''
tic tack toe game. lesson 31
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_30_TicTackToe/ticTackToe.py

'''
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QFileDialog
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_31_TicTackToe/ticTackToe.ui',self)
        self.but1=self.findChild(QPushButton,'pushButton')
        self.but2=self.findChild(QPushButton,'pushButton_2')
        self.but3=self.findChild(QPushButton,'pushButton_3')
        self.but4=self.findChild(QPushButton,'pushButton_4')
        self.but5=self.findChild(QPushButton,'pushButton_5')
        self.but6=self.findChild(QPushButton,'pushButton_6')
        self.but7=self.findChild(QPushButton,'pushButton_7')
        self.but8=self.findChild(QPushButton,'pushButton_8')
        self.but9=self.findChild(QPushButton,'pushButton_9')
        self.label=self.findChild(QLabel,'label')
        self.start=self.findChild(QPushButton,'Start')
        # click button
        self.counter =0
        self.but1.clicked.connect(lambda: self.clicker(self.but1))
        self.but2.clicked.connect(lambda: self.clicker(self.but2))
        self.but3.clicked.connect(lambda: self.clicker(self.but3))
        self.but4.clicked.connect(lambda: self.clicker(self.but4))
        self.but5.clicked.connect(lambda: self.clicker(self.but5))
        self.but6.clicked.connect(lambda: self.clicker(self.but6))
        self.but7.clicked.connect(lambda: self.clicker(self.but7))
        self.but8.clicked.connect(lambda: self.clicker(self.but8))
        self.but9.clicked.connect(lambda: self.clicker(self.but9))
        self.start.clicked.connect(lambda:self.reset())
        
    def clicker(self,b):
        if self.counter %2 ==0:
            mark='X'
            self.label.setText("0's turn")
        else:
            mark='O'
            self.label.setText("X's turn")
        
        
        
        b.setText(mark)
        b.setEnabled(False)
        self.counter +=1
    def reset(self):
        self.counter=0
        self.label.setText('')
        self.label.setText('start')
        button_list =[]
        button_list = [getattr(self, f'but{i}') for i in range(1, 10)]
        # for b in button_list:
        #     print(b)
        for b in button_list:
            b.setText('')
            b.setEnabled(True)
        self.label.setText('Start Again')
if __name__ =='__main__':
    app=QApplication(sys.argv)
    w= MainWindow()
    w.show()
    sys.exit(app.exec_())