'''
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/LearnerFolder/Ui_Form_Use_Import.py

https://chatgpt.com/c/685ee7c4-ddec-800f-8063-5f06872a7ae9

I am trying to use multiple class/module inheritance  to import and setupUi(UiForm) which is commented at the bottom of this program.  I want to 're instantiate' the WIdgets from the pyuic5 generated python file (Ui_Form_Import.py) Can you correct my attempt to get the widgets to function? ANd provide helpful comments with the recommendations?
'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# from Ui_Form_Import import Ui_Form
# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here

#         # Your code ends here W e want to get the ui form in
#          ## creates an instance of the UI_Form OBJECT and assign to self.ui
#         self.ui =Ui_Form() ## self is the UI object
#         self.ui.setupUi(self) ## the ui object is being passed into the   builds th gui we designed on the QWidge
#         ## we call the .setupUi() method and pass  in the self whcih is the QWidget.  thhis command is going to build the QWidget onto the 
#         ## this is going to build the gui we designed on to QWidget(remember we are using QWidget and not QWidow)
        
#         ## now to connect the button to the callback
#         self.ui.submit_button.clicked.connect(self.authenticate)
        
        
        
        
#         ## now cna add functioanlity
#         def authenticate(self):
#             ##to access the widgets we access calling ui.instance
#             username =self.ui.username_edit.text()
#             password =self.ui.password_edit.text()
#             if username ==  'user' and password == 'pass':
#                 qtw.QMessageBox.information(self,'Success','You are looged in')
#             else:
#                 qtw.QMessageBox.critical(self,'fail','you did not log in')
    
        
        
#         self.show()
# if __name__ == '__main__':
    
#     app = qtw.QApplication(sys.argv)## creates an OBJECT
#     Form= qtw.QWidget() ## the form is QWidget
    
#     ui= Ui_Form() ## an instance of the Ui_Form() class, Ui_Form is SUB CLASSED From OBJECT, It is a python OBJECT not a PyQT5 OBJEXT
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

## below i created multiple inheritance

# RE:/PyQt5/LearnerFolder/Ui_Form_Use_Import.py
# I am trying to use multiple class/module inheritance  to import and setupUi(UiForm) which is commented at the bottom of this program.  I want to 're instantiate' the WIdgets from the pyuic5 generated python file (Ui_Form_Import.py) Can you correct my attempt to get the widgets to function? ANd provide helpful comments with the recommendations?
'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from Ui_Form_Import import Ui_Form
class MainWindow(qtw.QWidget,Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here

        # Your code ends here We want to get the ui form in
         ## creates an instance of the UI_Form OBJECT and assign to self.ui
        # self.ui =Ui_Form() ## self is the UI object
        # self.ui.setupUi(self) ## the ui object is being passed into the   builds th gui we designed on the QWidge
        ## we call the .setupUi() method and pass  in the self whcih is the QWidget.  thhis command is going to build the QWidget onto the 
        ## this is going to build the gui we designed on to QWidget(remember we are using QWidget and not QWidow)
        
        ### or 
        # Correct way: Call setupUi(self) to build the UI on this QWidget
        self.setupUi(self)
        
        
        ## now to connect the button to the callback
        # self.ui.submit_button.clicked.connect(self.authenticate)
        self.submit_button.clicked.connect(self.authenticate)
        self.checkBox.clicked.connect(self.DefCheckBox)
        
        
        self.show()
        ## now cna add functioanlity
    def authenticate(self):
        ##to access the widgets we access calling ui.instance
        username =self.ui.username_edit.text()
        password =self.ui.password_edit.text()
        if username ==  'user' and password == 'pass':
            qtw.QMessageBox.information(self,'Success','You are looged in')
        else:
            qtw.QMessageBox.critical(self,'fail','you did not log in')

    def DefCheckBox(self):
        print('checked')
    
        
if __name__ == '__main__':
    
    app = qtw.QApplication(sys.argv)## creates an OBJECT
    Form= qtw.QWidget() ## the form is QWidget
    
    ui= Ui_Form() ## an instance of the Ui_Form() class, Ui_Form is SUB CLASSED From OBJECT, It is a python OBJECT not a PyQT5 OBJEXT
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
'''
'''    
This is Ui_Form_import.py
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(160, 80, 99, 20))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(160, 120, 85, 20))
        self.checkBox.setObjectName("checkBox")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(150, 170, 120, 80))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 30, 100, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.pushButton.setText(_translate("Form", "PushButton"))
''' 
'''You have the right idea with using multiple inheritance in MainWindow(qtw.QWidget, Ui_Form) and calling self.setupUi(self) inside your custom widget class.

🔍 Key Corrections & Notes:
Use self.setupUi(self) inside the constructor. This sets up the widgets on self, which is your main QWidget.
Do not do self.ui = Ui_Form() — you're already inheriting from Ui_Form, so you can use the widgets like self.pushButton, self.checkBox, etc., directly.
Your if __name__ == '__main__' block was redundant:
You were manually creating Form = QWidget() and calling ui.setupUi(Form). That’s only necessary if you're not subclassing.
Since MainWindow subclasses both QWidget and Ui_Form, it should be instantiated directly, as done above.

However, there are a few key corrections and clarifications to make:'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# from Ui_Form_Import import Ui_Form

# class MainWindow(qtw.QWidget, Ui_Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)  # Initialize parent QWidget
#         ## note this setupUi is calling a method in the UiForm and sets up the widgets in the .ui file onto this QWidget(yes,the .ui file)
#         self.setupUi(self)  # Set up the UI from Ui_Form on this QWidget
#         ## now all the widgets are directly accessible
#         # Connect widgets directly (no need to use self.ui because setupUi made them part of self)
#         self.pushButton.clicked.connect(self.authenticate)
#         self.checkBox.clicked.connect(self.DefCheckBox)

#         self.show()  # Show the widget

#     def authenticate(self):
#         # For this demo, just show a message box (no username/password fields in your current UI)
#         qtw.QMessageBox.information(self, 'Login', 'Authenticate button clicked')

#     def DefCheckBox(self):
#         print('CheckBox clicked')

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec_())




''' only do this if not using multiple inheritance
# Don't do this when subclassing Ui_Form:
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(...)  
'''

#  A COMPLETE EXAMPLE WITH A NEW PYUIC5 GENERATED .py from a .ui
#  AND THEN A FUNCTIONING .py CONSTRUCTED USING MULTIPLE INHERITANCE
#  Below is a complete working example of using PyQt5 with:

# QLineEdit for username and password input
# QPushButton to trigger authentication
# QCheckBox for additional interaction
# .ui file converted using pyuic5
# Multiple inheritance from Ui_Form
# ✅ Step 1: Your Updated Ui_Form_Import.py (generated from Qt Designer)
# If you're using Qt Designer, include these widgets:

# QLineEdit named username_edit
# QLineEdit named password_edit
# QPushButton named submit_button
# QCheckBox named checkBox
# Here’s the simplified version you'd get from pyuic5:
'''
from PyQt5 import QtCore, QtGui, QtWidgets
## this is the Ui_Form .py file generated from the QtDesigner, i put in Ui_Form_Import2.py
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.username_edit = QtWidgets.QLineEdit(Form)
        self.username_edit.setGeometry(QtCore.QRect(130, 50, 140, 25))
        self.username_edit.setObjectName("username_edit")

        self.password_edit = QtWidgets.QLineEdit(Form)
        self.password_edit.setGeometry(QtCore.QRect(130, 90, 140, 25))
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")

        self.submit_button = QtWidgets.QPushButton(Form)
        self.submit_button.setGeometry(QtCore.QRect(130, 130, 140, 30))
        self.submit_button.setObjectName("submit_button")

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(130, 180, 140, 20))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Form"))
        self.submit_button.setText(_translate("Form", "Login"))
        self.checkBox.setText(_translate("Form", "Remember Me"))
'''

import sys
from PyQt5 import QtWidgets as qtw
from Ui_Form_Import2 import Ui_Form

class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI from the pyuic5 class

        # Connect signals to slots
        self.submit_button.clicked.connect(self.authenticate)
        self.checkBox.stateChanged.connect(self.checkbox_toggled)

        self.show()

    def authenticate(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'Success', 'Login successful!')
        else:
            qtw.QMessageBox.critical(self, 'Error', 'Invalid username or password.')

    def checkbox_toggled(self, state):
        if state == qtw.Qt.Checked:
            print("Remember Me: Checked")
        else:
            print("Remember Me: Unchecked")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
