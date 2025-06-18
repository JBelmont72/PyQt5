'''
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1_ui.py

'''
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QMenuBar,QStatusBar
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        # Load the ui file
        uic.loadUi('Codemy/Cod_27_Load_Ui_File/loader_1.ui',self)
        # uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1.ui',self)
        ## define widgets
        self.label=self.findChild(QLabel,'label')
        self.textedit=self.findChild(QTextEdit,'textEdit')
        self.open=self.findChild(QPushButton,'pushButton_2')
        self.submit=self.findChild(QPushButton,'pushButton')
        self.textedit.setPlaceholderText('Enter name')
        self.submit.clicked.connect(self.clicker)
        self.open.setText('Enter name ')
        self.open.clicked.connect(self.enter)
        
        
        self.show()
    def clicker(self):
        self.label.setText(f'Hello {self.textedit.toPlainText()}')
        self.textedit.setText('')
    def enter(self):
        self.textedit.setPlainText('') ## tthese clear the textedit and label
        self.label.setText('')
        # self.textedit.setPlaceholderText('Enter another name')## these create new text messages 
        # self.label.setText('Enter your name....')    
### initializwe the app
if __name__ =='__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())

