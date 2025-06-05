'''

june 1 2025 chat refer to lambda authenicaiton issue
self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(qtw.QLineEdit.Password) ## uses the ACCESS METHOD
        ## below an alternative if lots of properites to enter, but not always works, bundle properties with the QLineEdit() CONSTRUCTOR
        # password_input=qtw.QLineEdit(echoMode=qtw.QLineEdit.Password)
    check_box = qtw.QCheckBox('legalese accept')
        check_box.setGeometry(qtc.QRect(130, 190, 85, 20))# my addition. no wffect?
        self.login_button= qtw.QPushButton('login')

        self.cancel_button = qtw.QPushButton('cancel')
        
        ## need an intermiary object called a layout
        layout = qtw.QFormLayout() ## now need to give positional arguemtns of rows and columns
            
'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        user1 =qtw.QLabel('user',self)
        userEdit1=qtw.QLineEdit(self)
    
        self.passLabel=qtw.QLabel('password',self)
        self.passEdit1 = qtw.QLineEdit(self)
        layout = qtw.QGridLayout()
        self.setLayout(layout)
        layout.addWidget(user1,2,0)
        layout.addWidget(userEdit1,2,2)
        layout.addWidget(self.passLabel,3,0)
        layout.addWidget(self.passEdit1,3,2)
        ## set Echo Mode for password
        self.passEdit1.setEchoMode(qtw.QLineEdit.Password)## password here is an attribute of the 
        checkBox =qtw.QCheckBox('accept',self)
        layout.addWidget(checkBox,4,1)
        # create login and cancel
        self.login_button= qtw.QPushButton('login',self)
        self.cancel_button = qtw.QPushButton('cancel',self)
        layout.addWidget(self.login_button,5,0)
        layout.addWidget(self.cancel_button,5,2)
        ## cancel to close
        self.cancel_button.pressed.connect(self.close)
        self.login_button.pressed.connect(self.autheniicate)
        self.show()
    def autheniicate(self):
        print('login')
        user = self.
        password =self.passEdit1.text()
        print(f'{user}')

     
    
        
        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

