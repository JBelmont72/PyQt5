''' import the .py from the same directory, this is a relative import
the first sketch is to import the generated UI class from the .py file created by PyQt5's `pyuic5` tool.
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Codemy/ComboBoxes/Cod_23_ComboBoxes.ui'
I created a CustmonMainWindow class that inherits from QMainWindow.
Then I initialized the UI in the constructor of the CustomMainWindow class with the `setupUi` method.
THis is is a template for a PyQt5 application that uses a custom UI class generated from Qt Designer.

chat about custom widgets  https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_23_ComboBoxes
'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# from Cod_23_ComboBoxes import Ui_MainWindow  # Import the UI class from the generated file
# # This is a template for a PyQt5 application that uses a custom UI class generated from Qt Designer.

# class CustomMainWindow(qtw.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         # Initialize the UI
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.setWindowTitle('My Window')  # Set the window title
#         self.resize(800, 600)   # Set the window size
#         self.setFixedSize(800, 600) # Set a fixed size for the window
#         self.label = self.ui.label  # Access the label from the UI
#         self.comboBox = self.ui.comboBox
#         self.pushButton = self.ui.pushButton
#         self.pushButton.clicked.connect(self.on_button_click)
#         self.comboBox.addItems(['Item 1', 'Item 2', 'Item 3'])
#     def on_button_click(self):
#         selected_item = self.comboBox.currentText()
#         self.label.setText(f'Selected Item: {selected_item}')
#         # Update the label with the selected item from the combo box
#         print(f'Selected Item: {selected_item}')
#         # Print the selected item to the console



# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)  # Create the application
#     w = CustomMainWindow(windowTitle='My Window')  # Create the main window
#     w.show()  # Show the main window
#     sys.exit(app.exec_())  # Exit the application

####### use this code to run the application, i have two functions to call the def  #######

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from Cod_23_ComboBoxes import Ui_MainWindow  
# This is a template for a PyQt5 application that uses a custom UI class generated from Qt Designer.

class CustomMainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        # Initialize the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('My Window')  # Set the window title
        self.resize(800, 600)   # Set the window size
        self.setFixedSize(800, 600) # Set a fixed size for the window
        self.label = self.ui.label  # Access the label from the UI
        self.comboBox = self.ui.comboBox
        self.pushButton = self.ui.pushButton
        # self.pushButton.clicked.connect(self.on_button_click)
        self.pushButton.clicked.connect(lambda : self.on_button_click(self))
        self.comboBox.addItems(['Item 1', 'Item 2', 'Item 3']) #adding a list of items to the combo box
        self.comboBox.currentIndexChanged.connect(lambda s: self.on_button_index_change(s))## this connects the currentIndexChanged signal of the comboBox to the on_button_click method
        # self.comboBox.currentIndexChanged.connect(self.on_button_index_change)## this connects the currentIndexChanged signal of the comboBox to the on_button_click method
        self.comboBox.activated.connect(lambda s: self.on_button_index_change(s))## this connects the activated signal of the comboBox to the on_button_click method
        # self.comboBox.activated.connect(self.clicker)## this connects the activated signal of the comboBox to the on_button_click method
        ## activated signal is emitted when the user selects an item from the combo box, this is used to update the label with the selected item from the combo box and No need to click the button to update the label with the selected item from the combo box!!!
        
        
    # def on_button_click(self):
    def on_button_click(self,s):
        selected_item = self.comboBox.currentText()
        self.label.setText(f'Selected Item from Button Click: {selected_item}')
        # Update the label with the selected item from the combo box
        print(f'Selected Item: {selected_item}')
        # Print the selected item to the console
    def on_button_index_change(self,s):
        print(f'Index Changed: {s}')
        selected_item = self.comboBox.currentText()
        self.label.setText(f'Selected Item: {selected_item}')
        # Update the label with the selected item from the combo box
        print(f'Selected Item: {selected_item}')
        # Print the selected item to the console
    def clicker(self):
        selected_item = self.comboBox.currentText()
        self.label.setText(f'Selected Item using comboBox: {selected_item}')
        # Update the label with the selected item from the combo box
        print(f'Selected Item using comboBox: {selected_item}')
        # Print the selected item to the console


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)  # Create the application
    w = CustomMainWindow(windowTitle='My Window')  # Create the main window
    w.show()  # Show the main window
    sys.exit(app.exec_())  # Exit the application
      