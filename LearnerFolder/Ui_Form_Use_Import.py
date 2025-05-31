'''



'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from Ui_Form_Import import Ui_Form
class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here

        # Your code ends here W e want to get the ui form in
         ## creates an instance of the UI_Form OBJECT and assign to self.ui
        self.ui =Ui_Form() ## self is the UI object
        self.ui.setupUi(self) ## the ui object is being passed into the   builds th gui we designed on the QWidge
        ## we call the .setupUi() method and pass  in the self whcih is the QWidget.  thhis command is going to build the QWidget onto the 
        ## this is going to build the gui we designed on to QWidget(remember we are using QWidget and not QWidow)
        
        ## now to connect the button to the callback
        self.ui.submit_button.clicked.connect(self.authenticate)
        
        
        
        
        ## now cna add functioanlity
        def authenticate(self):
            ##to access the widgets we access calling ui.instance
            username =self.ui.username_edit.text()
            password =self.ui.password_edit.text()
            if username ==  'user' and password == 'pass':
                qtw.QMessageBox.information(self,'Success','You are looged in')
            else:
                qtw.QMessageBox.critical(self,'fail','you did not log in')
    
        
        
        self.show()
if __name__ == '__main__':
    
    app = qtw.QApplication(sys.argv)## creates an OBJECT
    Form= qtw.QWidget() ## the form is QWidget
    
    ui= Ui_Form() ## an instance of the Ui_Form() class, Ui_Form is SUB CLASSED From OBJECT, It is a python OBJECT not a PyQT5 OBJEXT
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

