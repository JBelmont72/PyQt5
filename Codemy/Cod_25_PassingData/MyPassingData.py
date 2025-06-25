'''Codemy lesson 25 pass data between Windows

/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_25_PassingData/MyPassingData.py
chat:  https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Ui_LoginForm(windowTitle='My Window')
    w.show()  ## show the window, this is where the window is shown
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

from second_window import Ui_SecondWindow as Ui_NewWindow
class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# from Connect1 import Ui_MainWindow as MainWindowUI  # This is the generated UI class from the first window
# from Connect2 import Ui_SecondWindow as SecondWindowUI  # This is the generated UI class from the second window

# # Main application window (First Window)
# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = MainWindowUI()
#         self.ui.setupUi(self)  # Properly apply the generated UI to this QMainWindow instance

#         # Connect button signals to their slots
#         self.ui.Open.clicked.connect(self.open_second_window)
#         self.ui.Submit.clicked.connect(self.submit_to_second_window)

#         # Create second window instance
#         self.second_window = SecondWindow(self)  # Pass reference to main window

#     def open_second_window(self):
#         self.second_window.show()

#     def submit_to_second_window(self):
#         text = self.ui.textEdit.toPlainText()
#         self.second_window.ui.comboBox.addItem(text)  # Submit text to comboBox in second window

#     def update_label(self, text):
#         self.ui.lineEdit.setText(text)  # Update lineEdit in first window from second window


# # Second application window
# class SecondWindow(qtw.QMainWindow):
#     def __init__(self, main_window):
#         super().__init__()
#         self.ui = SecondWindowUI()
#         self.ui.setupUi(self)

#         self.main_window = main_window  # Store reference to main window

#         # Add a signal for text change in combo box to update the main window's label
#         self.ui.comboBox.currentTextChanged.connect(self.send_text_back)

#     def send_text_back(self, text):
#         # When combo box changes, update the main window's label or line edit
#         self.main_window.update_label(text)


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     window = MainWindow()
#     window.setWindowTitle('Main Window')
#     window.show()
#     sys.exit(app.exec_())

'''
Key Fixes:
Incorrect Inheritance and Setup:
❌ You were inheriting from the Ui_MainWindow class and trying to use setupUi() on the same object. That’s redundant and problematic.
✅ Now the MainWindow class inherits only from QMainWindow and uses Ui_MainWindow via composition (self.ui = MainWindowUI()), which is the clean and expected way when using pyuic5-generated UI.
Button Setup Outside UI Class:
❌ You were recreating buttons (QPushButton('Submit', self)) manually after using a .ui file — this overwrites or bypasses the .ui design.
✅ Now, you reference the UI components created in Qt Designer (e.g., self.ui.Submit) and connect signals properly.
Second Window Class Defined After Use:
❌ You defined Ui_SecondWindow after referencing it, which can confuse logic and dependency flow.
✅ The second window is now cleanly structured and passed a reference to the main window for communication.
No Mechanism to Share Data:
❌ You had no method to send or receive data between windows.
✅ The second window now calls main_window.update_label() to send data back.

'''


## not using this code, but keeping it here for reference, only opens second window, not passing data
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# from Connect1 import Ui_MainWindow  as MainWindow # Import the generated UI class from your .ui file
# # This is a template for a PyQt5 application with a main window and a label.    
# # from Connect2 import Ui_SecondWindow as SecondWindow  # Import the second window UI class
# class Ui_MainWindow(qtw.QMainWindow, MainWindow):
#     ##This class inherits from QMainWindow and the generated Ui_LoginForm class.

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
#         self
#         self.Open.clicked.connect(self.open_window)  ## connect the button to the open_window method
#         self.Submit.clicked.connect(self.submit_data)  ## connect the button to the submit_data method
#         ## need to create a new window instance
        
#     def open_window(self):
#         self.new_window = SecondWindow()
#         self.new_window.setupUi(self.new_window)
#         self.new_window.setWindowTitle('Second Window')
#         self.new_window.show()

#     def submit_data(self):
#         pass
#         # This method will be called when the Submit button is clicked

# from Connect2 import Ui_SecondWindow as SecondWindow  # Import the second window UI class
# class Ui_SecondWindow(qtw.QMainWindow, SecondWindow):
#     ##This class inherits from QMainWindow and the generated Ui_SecondWindow class.

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)  ## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         self.setupUi(self)  ## call the setupUi method to set up the UI components
#         self.setWindowTitle('Second Window')  ## set the window title
#         self.label = qtw.QLabel('This is the second window', self)  ## create a label with text
#         self.label.setGeometry(qtc.QRect(50, 50, 200, 50))  ## set the geometry of the label
#         self.label.setAlignment(qtc.Qt.AlignCenter)
#         self.label.setStyleSheet("font-size: 20px; color: blue;")
#         self.setGeometry(100, 100, 400, 300)

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = Ui_MainWindow(windowTitle='My Window')
#     w.show()  ## show the window, this is where the window is shown
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# from Connect1 import Ui_MainWindow as MainWindowUI  # This is the generated UI class from the first window
# from Connect2 import Ui_SecondWindow as SecondWindowUI  # This is the generated UI class from the second window

# # Main application window (First Window)
# class MainWindow(qtw.QMainWindow, MainWindowUI):
#     def __init__(self):
#         super().__init__()
#         # self.ui = MainWindowUI()
#         self.setupUi(self)  # Properly apply the generated UI to this QMainWindow instance

#         # Connect button signals to their slots
#         self.Open.clicked.connect(self.open_second_window)
#         self.Submit.clicked.connect(self.submit_to_second_window)

#         # Create second window instance
#         self.second_window = SecondWindow(self)  # Pass reference to main window

#     def open_second_window(self):
#         self.second_window.show()

#     def submit_to_second_window(self):
#         text = self.textEdit.toPlainText()
#         self.second_window.comboBox.addItem(text)  # Submit text to comboBox in second window

#     def update_label(self, text):
#         self.lineEdit.setText(text)  # Update lineEdit in first window from second window


# # Second application window
# class SecondWindow(qtw.QMainWindow, SecondWindowUI):
#     # This class inherits from QMainWindow and the generated Ui_SecondWindow class.
#     def __init__(self, main_window):
#         super().__init__()
#         # self.ui = SecondWindowUI()
#         self.setupUi(self)

#         self.main_window = main_window  # Store reference to main window

#         # Add a signal for text change in combo box to update the main window's label
#         self.comboBox.currentTextChanged.connect(self.send_text_back)

#     def send_text_back(self, text):
#         # When combo box changes, update the main window's label or line edit
#         self.main_window.update_label(text)


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     window = MainWindow()
#     window.setWindowTitle('Main Window')
#     window.show()
#     sys.exit(app.exec_())
'''

🔁 Where is main_window coming from?
Look at this part of your MainWindow class:

self.second_window = SecondWindow(self)  # Pass reference to main window
✅ What’s happening here?

You're creating an instance of SecondWindow inside the MainWindow class.
The self in SecondWindow(self) refers to the current instance of MainWindow.
That means you're explicitly passing a reference to the current main window into the second window.
🧠 Why do we do this?
So the SecondWindow can call methods or access widgets from the MainWindow.

This line in SecondWindow saves that reference:

self.main_window = main_window
Now, inside SecondWindow, you can use:

self.main_window.update_label(text)
...to call a method in the main window — in this case, updating the text in the lineEdit.

🧩 Visual Summary
[MainWindow]
    ├─ sets up its own UI (Connect1)
    ├─ has a QPushButton called "Open"
    ├─ creates → [SecondWindow(self)]
                      └── receives and stores reference to MainWindow as self.main_window
                             └── can now call self.main_window.update_label(...)
This is a form of bidirectional communication, where each window can interact with the other



'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from Connect1 import Ui_MainWindow as MainWindowUI  # This is the generated UI class from the first window
from Connect2 import Ui_SecondWindow as SecondWindowUI  # This is the generated UI class from the second window

class MainWindow(qtw.QMainWindow,MainWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)## not MainWindowUI because I already included that in the multiple inheritance!!
        
        ## create a seoncd window instance
        self.second_window= SecondWindow(self)
        
        # Connect button signals to their slots
        self.Open.clicked.connect(self.open_second_window)
        self.Submit.clicked.connect(self.submit_to_second_window)
    def open_second_window(self):
        self.second_window.show()

    def submit_to_second_window(self):
        text = self.textEdit.toPlainText()
        self.second_window.comboBox.addItem(text)  # Submit text to comboBox in second window

    def update_label(self, text):
        self.lineEdit.setText(text)  # Update lineEdit in first window from second window


class SecondWindow(qtw.QMainWindow,SecondWindowUI):
    def __init__(self,main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window=main_window

        # Add a signal for text change in combo box to update the main window's label
        self.comboBox.currentTextChanged.connect(self.send_text_back)

    def send_text_back(self, text):
        # When combo box changes, update the main window's label or line edit
        self.main_window.update_label(text)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Main Window')
    window.show()
    sys.exit(app.exec_())