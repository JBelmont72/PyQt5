'''
Alan D Moore  'QtDesigner and PyQt5  : The Right and wrong way to use them together'
minute 31 is the meat of the video, where he shows how to import the .ui file and use it in a PyQt5 application.

#         self.accept()  # Accept the dialog (equivalent to clicking "OK" in the dialog)
#
    def reject_dialog(self):
        self.reject()  # Reject the dialog (equivalent to clicking "Cancel" in the dialog)
        
        
  these are from myLogin.py:
  if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()## note that this is a QMainWindow, not a QDialog and the class inherits from QMainWindow below
    # Create an instance of the Ui_LoginForm class
    ui = Ui_LoginForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())      
        
 class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")       
        
'''

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from myLogin import Ui_LoginForm  # Import the generated UI class from your .ui file
# This is a template for a PyQt5 application with a main window and a label.    

class Ui_LoginForm(qtw.QMainWindow, Ui_LoginForm):
    ##This class inherits from QMainWindow and the generated Ui_LoginForm class.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here
        self.setupUi(self)
        # You can add additional setup code here if needed
        self.setWindowTitle('My Login Form')
        self.setGeometry(100, 100, 400, 300)
        # Your code ends here
        # self.show() ## put it here so the window shows.
        self.cancelButton.clicked.connect(self.reject_dialog)
        self.loginButton.clicked.connect(self.accept_dialog)
        self.checkBox.setChecked(False)  # Set the checkbox to unchecked by default
        # self.checkBox.setText("legalese")  # Set the checkbox text already in the .ui file
        self.checkBox.clicked.connect(self.on_checkbox_clicked)  # Connect the checkbox click event to a method
    def on_checkbox_clicked(self):
        if self.checkBox.isChecked():
            self.accept_dialog()
    
        # You can add more logic here if needed when the checkbox is clicked
        
    def accept_dialog(self):
        print("Login accepted")
        username = self.username_lineEdit.text()
        password = self.password_line_edit.text()
        legalese = self.checkBox.isChecked()
        print(f"Username: {username}, Password: {password}, Legalese: {legalese}")
        qtw.QMessageBox.information(self, "Login Info", f"Username: {username}\nPassword: {password}\nLegalese: {legalese}")
    def reject_dialog(self):
        print("Login cancelled")
        qtw.QMessageBox.warning(self, "Login Cancelled", "You have cancelled the login process.")
        self.close()
        ## these are the methods that are called when the buttons are clicked
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Ui_LoginForm(windowTitle='My Window')
    w.show()  ## show the window, this is where the window is shown
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes


