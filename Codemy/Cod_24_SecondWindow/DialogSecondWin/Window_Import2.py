''' /Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_24_SecondWindow/Codemy_SecondWindow/Window_Import2.py
Here's how you can wrap your third window dialog (Ui_Dialog) into a reusable ThirdDialog class using QDialog and keep all your .ui-generated layout and logic intact.
this is a code snippet that imports three different UI classes from separate files.
Note this has the same functionality asCodemy_SecondWindow/Window_Import.py BUT moves the Dialog UI into a separate class for better organization and reusability.
# This allows you to create a main window that can open two additional windows, each with its own UI as follows:
# 1. Main Window (Ui_MainWindow1)
# 2. Second Window (Ui_MainWindow2)
# 3. Third Window (Ui_Dialog)
# It sets up a main window and two additional windows, each with their own UI class, for example, a main window that can open a second window and a third dialog.
# This code is part of a PyQt5 application that demonstrates how to import and use multiple UI classes.
Summary of Benefits
✅ Keeps your .ui layout and pyuic5 flow intact.
✅ Adds the flexibility of class-based customization.
✅ Lets you access and extend dialog logic more cleanly.
✅ Can now return Accepted or Rejected status via .exec_().


 https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
 
from Window1 import Ui_MainWindow as Ui_MainWindow1
from Window2 import Ui_SecondWindow as Ui_MainWindow2
from Window3 import Ui_ThirdWindow as Ui_MainWindow3
from PyQt5 import QtCore, QtGui, QtWidgets as qtc,qtg,qtw



class Ui_MainWindow(object): #     from Window_1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 301)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        
class Ui_SecondWindow(object):  #  from Window_2
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")   
        
class Ui_ThirdWindow(object):    #  from Window_3
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        
        
self.third_window = qtw.QMainWindow()  # ❌ This is a QMainWindow
self.third_ui = Ui_MainWindow3()       # ✅ This is a QDialog-based layout
self.third_ui.setupUi(self.third_window)  # ❌ Passing QMainWindow into a QDialog setup
Use .exec_() if the dialog is meant to collect input or block other windows (e.g., a "Save" dialog).
Use .show() if it’s just a notification or something casual (like “Success!”).

'''
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
import sys
# import the UI classes generated by pyuic5
from Window1 import Ui_MainWindow as Ui_MainWindow1
from Window2 import Ui_SecondWindow as Ui_MainWindow2
# from Window3 import Ui_ThirdWindow as Ui_MainWindow3
from Window4_Dialog import Ui_Dialog as Ui_MainWindow3


# Define a proper Main Window class to encapsulate logic
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_second_window)  # Connect pushButton to open second window
        self.statusBar=self.ui.statusbar
        self.statusBar.showMessage("Welcome to the Main Window")  # Set initial status bar message
        self.statusBar.setStyleSheet("background-color: lightgray;")  # Set status bar style
    def open_second_window(self):
        # Create a new QMainWindow and apply the Ui_SecondWindow layout to it
        self.second_window = qtw.QMainWindow()  # This is a real window
        self.second_ui = Ui_MainWindow2()       # This is the layout/setup
        self.second_ui.setupUi(self.second_window)
        self.second_ui.pushButton.clicked.connect(self.open_third_window)  # connect second window's button
        
        self.menubar =self.second_ui.menubar
        self.menubar.setStyleSheet("background-color: lightblue;")
        self.statusbar = self.second_ui.statusbar
        self.statusbar.setStyleSheet("background-color: lightgreen;")
        self.second_window.show()  # Now it can be shown!

    def open_third_window(self):        ##  Use the new ThirdDialog class
        self.third_window = ThirdDialog(self)  # Use your new class
        self.third_window.exec_()  # Modal dialog

    def open_third_window(self):
        dialog = ThirdDialog(self)
        if dialog.exec_() == qtw.QDialog.Accepted:
            # Dialog was accepted: use returned_name
            name = dialog.returned_name
            self.statusbar.showMessage(f"User entered: {name}")
        else:
            self.statusbar.showMessage("Dialog canceled.")


    # def open_third_window(self):
    #     # Create a new QDialog  and apply the Ui_ThirdWindow layout to it
    #     self.third_window = qtw.QDialog()  # Using QDialog for the third window
    #     self.third_window.setWindowTitle("Third Window")
    #     self.third_ui = Ui_MainWindow3()
    #     self.third_ui.setupUi(self.third_window)
    #     self.third_ui.label.setText("Welcome to the Third Window!")
    #     self.third_ui.buttonBox.accepted.connect(self.third_window.accept)  # Connect buttonBox to accept
    #     self.third_ui.buttonBox.rejected.connect(self.third_window.reject)  # Connect buttonBox to reject
    #     self.third_window.exec_()  # Open modally (blocks other windows until closed)
        
        
        
    #     # OR use: self.third_window.show() for non-modal
    #     # Open modally (blocks other windows until closed)
    # def open_third_window(self): ## use this with a third window as a QDialog: Codemy/Cod_24_SecondWindow/Codemy_SecondWindow/Window4_Dialog.py
    #     self.third_window = qtw.QDialog(self)  # ✅ Create a QDialog instance, not QMainWindow
    #     self.third_ui = Ui_MainWindow3()       # ✅ This is your Ui_Dialog
    #     self.third_ui.setupUi(self.third_window)  # ✅ Apply the dialog layout to the dialog
    #     self.third_window.exec_()  # ✅ Open modally (blocks other windows until closed)
    #     # OR use: self.third_window.show() for non-modal

    
    
    # def open_third_window(self): ## use this if you want a third window as a QMainWindow :Codemy/Cod_24_SecondWindow/Codemy_SecondWindow/Window3.py
    #     # Create a new QMainWindow and apply the Ui_ThirdWindow layout to it
    #     self.third_window = qtw.QMainWindow()
    #     self.third_ui = Ui_MainWindow3()
    #     self.third_ui.setupUi(self.third_window)
    #     self.third_window.show()

from PyQt5 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
from Window4_Dialog import Ui_Dialog  # This is your pyuic5-generated dialog UI class

class ThirdDialog(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # Initialize the QDialog with an optional parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Set up the UI on this dialog

        # Example: Customize or connect signals here
        self.ui.label.setText("Welcome to the Third Window!")

        # You can connect button signals manually if needed
        self.ui.buttonBox.accepted.connect(self.accept_dialog)
        self.ui.buttonBox.rejected.connect(self.reject_dialog)

    def accept_dialog(self):
        print("Dialog accepted")
        self.ui.label.setText("Dialog Accepted!")  # Example of changing label text
        # You can add more logic here if needed
        # For example, you might want to close the dialog or perform some action
        self.accept()  # Close the dialog with Accepted result

    def reject_dialog(self):
        print("Dialog rejected")
        self.ui.label.setText("Dialog Rejected!")
        # You can add more logic here if needed
        self.reject()  # Close the dialog with Rejected result

    
    
if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    main_win = MainWindow()  # Instantiate the class-based main window
    main_win.show()  # Show the main window
    sys.exit(app.exec_())

