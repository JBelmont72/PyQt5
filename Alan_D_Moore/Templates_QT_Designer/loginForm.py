'''  This is the second and third ways to open and use the .ui file
1. copy the Template.py 
'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# from myLogin import Ui_LoginForm


# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
#         self.ui=Ui_LoginForm()
#         self.ui.setupUi(self)
#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
    
###
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here
        
        # user_label =qtw.QLabel('username')## when we use the Form layout, we can add the labels directly and do NOT need QLabel!!
        # password_label = qtw.QLabel('password')
   
        self.user_input = qtw.QLineEdit() ## had to make these self. to be reocgnized by the methods we will develop now
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
        
        ## need an intermiary object called a layout
        # layout = qtw.QVBoxLayout() used this before but not here since we are using a grid
        layout.addRow('user_name',self.user_input,)
        layout.addRow('password',self.password_input,)
        
        check_box_widget=qtw.QWidget()
        check_box_widget.setLayout(qtw.QHBoxLayout())
        check_box_widget.layout().addWidget(check_box)
        layout.addRow('',check_box_widget)
        
        ## will create for this last eaxample a button_widget =qtw.QWidget()
        button_widget =qtw.QWidget() ## will place buttons inside
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.login_button)
        layout.addRow('', button_widget)
        self.setLayout(layout) ## this is where we connect the 'layout=qtw.QFormLayout (or H or V or Grid) to the class
        
        
        ## can add layouts to layouts,  cannot widget to layouots.  layouts can be added to either a widget or layouot
        ## need to tell this class that this layout is for this class
        self.setLayout(layout)
        ## want to start adding functioanality
        # cancel_button.clicked.connect(self.close)## close is the slot
        # cancel_button.pressxed.connect(self.close)## close is the slot
        
        self.cancel_button.released.connect(self.close)## close is the slot, toggle() is another option
        # self.login_button.clicked.connect(clicked = lambda : self.authenticate())
        self.login_button.clicked.connect(self.authenticate)
        # Your code ends here
        self.show() ## put it here so the window shows.

    def authenticate(self):

        username = self.user_input.text()
        password = self.password_input.text()

        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'Success', 'You are logged in.')
            self.authenticated.emit(username)
        else:
            qtw.QMessageBox.critical(self, 'Failed', 'You are not logged in.')

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
 