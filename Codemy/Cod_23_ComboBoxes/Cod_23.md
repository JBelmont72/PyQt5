import the .py from the same directory, this is a relative import
the first sketch is to import the generated UI class from the .py file created by PyQt5's `pyuic5` tool.
-*- coding: utf-8 -*- Form implementation generated from reading ui file 'Codemy/ComboBoxes/Cod_23_ComboBoxes.ui'
I created a CustmonMainWindow class that inherits from QMainWindow.
Then I initialized the UI in the constructor of the CustomMainWindow class with the `setupUi` method.
THis is is a template for a PyQt5 application that uses a custom UI class generated from Qt Designer.

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from Cod_23_ComboBoxes import Ui_MainWindow  # Import the UI class from the generated file
 This is a template for a PyQt5 application that uses a custom UI class generated from Qt Designer.

class CustomMainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        # Initialize the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('My Window')  # Set the window title
        self.resize(800, 600)   # Set the window size
        self.setFixedSize(800, 600) # Set a fixed size for the window
    



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)  # Create the application
    w = CustomMainWindow(windowTitle='My Window')  # Create the main window
    w.show()  # Show the main window
    sys.exit(app.exec_())  # Exit the application

