'''
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_29_QFileDialog/file.py
note the three places i place the window name! class, super, and the instantiation w=MainWindow()
'''


from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QFileDialog
import sys
from PyQt5 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('Codemy/Cod_29_QFileDialog/file.ui',self)
        self.label =self.findChild(QLabel,'label')
        self.button =self.findChild(QPushButton,'pushButton')
        self.edit=self.findChild(QTextEdit,'textEdit')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.clicker)
        
    def clicker(self,is_clicked):
        print('clicked',is_clicked)
        self.label.setText('')
        if is_clicked==False:
            self.label.setText('False')
        else:
            self.label.setText('True')
    ## both def clickers are sme, the second uses the ,_  to get only the first element of tuple
    # def clicker(self):
    #     # Open File Dialog returns a tuple
    #     fname = QFileDialog.getOpenFileName(self,'OPEN FILE',"  ","All Files (*);;Python Files(*.py)")
    #     # output filename to screen if something is returned
    #     if fname:
    #         self.label.setText(str(fname))
    #         # self.edit.setText(str(fname))  
    #         self.edit.setText(fname[0])  
    def clicker(self):
        # Open File Dialog returns a tuple, use underscore to just get the first element of tuple
        # fname,_ = QFileDialog.getOpenFileName(self,'OPEN FILE',"  ","All Files (*);;Python Files(*.py);;PNG Files (*.png)")
        fname,_ = QFileDialog.getOpenFileName(self,'OPEN FILE'," /Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1.ui.png ","All Files (*);;Python Files(*.py);;PNG Files (*.png)")
        # output filename to screen if something is returned
        if fname:
            self.label.setText(fname)
            # self.edit.setText(str(fname))  
            self.edit.setText(fname)  

if __name__ =='__main__':
    app=QApplication(sys.argv)
    w=MainWindow()
    w.show()
    sys.exit(app.exec_())


