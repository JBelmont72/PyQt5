'''

/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_30_ImageViewer/image.py

'''
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QFileDialog
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('Codemy/Cod_30_ImageViewer/image.ui',self)
        self.button=self.findChild(QPushButton,'pushButton')
        self.label =self.findChild(QLabel,'label')
        self.label.setGeometry(10,10,400,400)
        self.edit =self.findChild(QTextEdit,'textEdit' )
        self.edit.setGeometry(10,400,200,20)
        
        self.button.clicked.connect(self.openImage)
        
        
    def openImage(self):
        fname=QFileDialog.getOpenFileName(self,'OpenFile','/Users/judsonbelmont/Documents/images','All Files (*);;PNG (*.png)' )
        # Open the image
        self.pixmap=QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)
        self.edit.setText(fname[0])
    
    # def openImage(self):
    #     fname,_ =QFileDialog.getOpenFileName(self,'OpenFile','/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Images','All Files (*);;PNG (*.png)' )
    #     # Open the image
    #     self.pixmap=QPixmap(fname)
    #     self.label.setPixmap(fname)
    #     self.edit.setText(fname)
            
        
if __name__ =='__main__':
    app=QApplication(sys.argv)
    w= MainWindow()
    w.show()
    sys.exit(app.exec_())
    