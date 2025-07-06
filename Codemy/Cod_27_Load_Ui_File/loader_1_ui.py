'''
/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1_ui.py
 
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QMenuBar,QStatusBar
in this file i loaded two .ui files from QtDesigner directly using the uic library
then I experiemnted with fisrt passing a variable from the second window to the MainWIndow.
Then passing a variable ( var =name) from the open function to the SecondWindow 's label,
then saving a variable from the clicker function attached to the submit button to the newEntry funcrition attached tothe open button.
added an if no valuie was in the textedit, to print Stranger in the secondwindows label
'''
# from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QMenuBar,QStatusBar
# from PyQt5 import uic
# import sys

# class UI(QMainWindow):  # my memory aid 3 UIs and 3 selfs, super(UI,self)
#     def __init__(self):
#         super(UI,self).__init__()
#         # Load the ui file
#         uic.loadUi('Codemy/Cod_27_Load_Ui_File/loader_1.ui',self)
#         # uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1.ui',self)
#         ## define widgets
#         self.label=self.findChild(QLabel,'label')
#         self.textedit=self.findChild(QTextEdit,'textEdit')
#         self.open=self.findChild(QPushButton,'pushButton_2')
#         self.submit=self.findChild(QPushButton,'pushButton')
#         self.textedit.setPlaceholderText('Enter name')
#         self.submit.clicked.connect(self.clicker)
#         self.open.setText('Enter name ')
#         self.open.clicked.connect(self.enter)
        
        
#         self.show()
#     def clicker(self):
#         self.label.setText(f'Hello {self.textedit.toPlainText()}')
#         self.textedit.setText('')
#     def enter(self):
#         self.textedit.setPlainText('') ## these clear the textedit and label
#         self.label.setText('')
#         # self.textedit.setPlaceholderText('Enter another name')## these create new text messages 
#         # self.label.setText('Enter your name....')    
# ## initialize the app
# if __name__ =='__main__':
#     app = QApplication(sys.argv)
#     UIWindow = UI()
#     sys.exit(app.exec_())
# 1- import uic library
# 2- in the setup create a window name, here i used Ui =MainWindow()
# 3- Create a class with that WIndow name and designate the parent . in this case QMainWindow.
# 4- in the super( pass in the window name which is found in the .ui file, and pass in self)
# 5 use the uic.load() to load in the .ui file we created.

# from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QMenuBar,QStatusBar
# from PyQt5 import uic
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         uic.loadUi('Codemy/Cod_27_Load_Ui_File/loader_1.ui',self)
        # uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1.ui')
#         self.label=self.findChild(QLabel,'label')
        
        
        # self.label=self.findChild(QLabel,'label')
        # self.textedit=self.findChild(QTextEdit,'textEdit')
        # self.open=self.findChild(QPushButton,'pushButton_2')
        # self.submit=self.findChild(QPushButton,'pushButton')
        # self.textedit.setPlaceholderText('Enter name')
        # self.submit.clicked.connect(self.clicker)
        # self.open.setText('Enter name ')
        # self.open.clicked.connect(self.enter)
        
        
        
    #     self.show()
        
    # def clicker(self):
    #     self.label.setText(f'Hello {self.textedit.toPlainText()}')
    #     self.textedit.setText('')
    # def enter(self):
    #     self.textedit.setPlainText('') ## tthese clear the textedit and label
    #     self.label.setText('')
        # self.textedit.setPlaceholderText('Enter another name')## these create new text messages 
        # self.label.setText('Enter your name....')    


# if __name__=='__main__':
#     app =QApplication(sys.argv)
#     Ui=MainWindow()
#     sys.exit(app.exec_())


'''
Goal Recap:

Open SecondWindow from MainWindow ✅
In SecondWindow, click a button to:
Close the SecondWindow ✅
Update the MainWindow’s label and textEdit widgets ❌ (not working currently)
🧠 Problems in Your Code:

❌ You're creating a new MainWindow in SecondWindow.enter() — that’s not what you want.
You already have a MainWindow instance running.
You should just pass a reference to that instance into SecondWindow.
❌ self.window = MainWindow() in SecondWindow is unnecessary and undefined (self.window is never set before).
❌ You're calling self.main_window = MainWindow() instead of using the existing one
✅ Solution Plan:

Pass the existing MainWindow into SecondWindow when you open it.
Use that reference to update its widgets from SecondWindow.
Then close the SecondWindow.
✅ Fixed Code:

🔧 MainWindow class (change in newEntry()):

'''

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QTextEdit,QPushButton,QMenuBar,QStatusBar
from PyQt5 import uic
import sys
## Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1_ui.py
#https://chatgpt.com/c/68602b54-be4c-800f-8a73-95fbaaa16184 very instructional
class SecondWindow(QMainWindow):
    # def __init__(self,main_window):## without passing the variable from MainWindow
    def __init__(self,main_window,name):    ## with passing name from MainWIndow
        super(SecondWindow,self).__init__()
        uic.loadUi('Codemy/Cod_27_Load_Ui_File/SecondWindow.ui',self)
        self.button=self.findChild(QPushButton,'pushButton')
        self.label =self.findChild(QLabel,'label')
        # self.label.setText('my text')
        self.name = name  # 💡 store the name that was passed
        self.button.clicked.connect(self.enter)
        ## ChatGPT did not use self.main_window = None but used:
        self.main_window=main_window    ## Rerference to MainWindow
        self.label.setText(f'Hello {self.name}')
        self.show()
    def enter(self):
        self.label.setText('i have called def(enter)')
        if self.main_window:
            self.main_window.label.setText('MainWindow updated from SecondWindow!')

            # self.main_window.edit.setText('Hello from SecondWindow!')
            self.main_window.edit.setText('')
        self.close()
    def closeEvent(self, event):
        self.main_window.second_window = None  # reset the pointer
        super().closeEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Load_Ui_File/loader_1.ui',self)
        
        self.label=self.findChild(QLabel,'label')
        self.edit=self.findChild(QTextEdit,'textEdit')
        self.open =self.findChild(QPushButton,'pushButton')
        self.submit=self.findChild(QPushButton,'pushButton_2')
        self.menubar=self.findChild(QMenuBar,'menubar')
        self.statusbar= self.findChild(QStatusBar,'statusbar')
        
        self.edit.setPlaceholderText('please enter name here')
        
        self.label.setText('Enter Name Here:')
        
        self.open.clicked.connect(self.clicker)
        self.submit.clicked.connect(self.newEntry)
        self.second_window=None
        self.show()
        
    def clicker(self):
        self.name = self.edit.toPlainText()  # ✅ Save as instance variable
        self.label.setText(f'Hello {self.name}')
        self.edit.setText('')  # Optional: clear field
        # if not self.name:
        if not self.name.strip():
             self.name = "Stranger"

    
          
    # def clicker(self):
    #     self.label.setText('')
    #     self.label.setText(f'Hello {self.edit.toPlainText()}')
    #     name = self.edit.toPlainText()
    #     self.name =name
    #     self.edit.setText('')
        
    # def newEntry(self):   ## this works but does not share the textEdit entry with second window
    #     self.label.setText('')
    #     self.edit.setPlaceholderText('Enter another name now please:')
    #     if self.second_window==None:
    #         # IMPORTANT pass mainWindow instance into the SecondWindow()
    #         self.second_window=SecondWindow(self)   #this is done with self
    #         self.second_window.show() 
        
    # def newEntry(self):## this creates a variable 'var' for the textEdit entry so I can send it to second window
    #     name = self.edit.toPlainText()  # ✅ Capture name before clearing
    #     self.label.setText('')
    #     self.edit.setPlaceholderText('Enter another name now please:')

    #     if self.second_window is None:
    #         self.second_window = SecondWindow(self, name)  # ✅ Pass name
    #         self.second_window.show()

    #     self.edit.setText('')  # 🔄 Clear after launching SecondWindow   
    def newEntry(self): ## third approach is to grab the name in newENtry and use in def clicker even if a new name was not entered
        # Only update placeholder and clear the box
        self.label.setText('')
        self.edit.setPlaceholderText('Enter another name now please:')

        # Fallback: if no name entered before, get what's in edit box now
        name_to_use = getattr(self, "name", self.edit.toPlainText())

        if self.second_window is None:
            self.second_window = SecondWindow(self, name_to_use)
            self.second_window.show()

        self.edit.setText('')  # Clear for next entry
   
# #     def enter(self):
#         self.textedit.setPlainText('') ## tthese clear the textedit and label
#         self.label.setText('')
#         # self.textedit.setPlaceholderText('Enter another name')## these create new text messages 
#         # self.label.setText('Enter your name....')    
        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    sys.exit(app.exec_())
    
#####   My next mission was to take a value from the textEdit of MainWIndow and convey it to the label 
# to show the entered name from MainWindow's textEdit inside SecondWindow, you should:
# Save it to a variable when appropriate (e.g. in clicker() or newEntry())
# Pass it as a parameter to SecondWindow when instantiating it
# Use that passed name to update the label in SecondWindow
# ✅ Step-by-Step Fix

# 🔁 Update SecondWindow to accept a name:


# class SecondWindow(QMainWindow):
#     def __init__(self, main_window, name):## note , now I am passing the name from MainWindow
#         super().__init__()
#         uic.loadUi('Codemy/Cod_27_Load_Ui_File/SecondWindow.ui', self)

#         self.button = self.findChild(QPushButton, 'pushButton')
#         self.label = self.findChild(QLabel, 'label')

#         self.main_window = main_window
#         self.name = name  # 💡 store the name that was passed

#         self.label.setText(f'Hello {self.name}')  # ✅ Set label using passed name

#         self.button.clicked.connect(self.enter)
#         self.show()

# 🔁 Update MainWindow.newEntry() to pass the name:
# Right now you're not storing the entered name before clearing the field. You should grab the name from self.edit.toPlainText() before clearing it:   
    
# def newEntry(self):
#     name = self.edit.toPlainText()  # ✅ Capture name before clearing
#     self.label.setText('')
#     self.edit.setPlaceholderText('Enter another name now please:')

#     if self.second_window is None:
#         self.second_window = SecondWindow(self, name)  # ✅ Pass name
#         self.second_window.show()

#     self.edit.setText('')  # 🔄 Clear after launching SecondWindow
# ✅ Result

# This allows the following flow:

# User types name into textEdit
# User clicks "Submit" (or whatever pushButton_2 does)
# SecondWindow opens and greets the user by name using its label
# 🔁 Optional: Keep clicker() for live updates

# If you are also using clicker() for previewing the greeting in the label, it/’s totally fine — just don't clear edit there if you need the name again in newEntry().
    
    
    
    
    
    
    
    
'''  Tutorial Example for method .closeEvent()
    In PyQt5, the closeEvent is a virtual function of QWidget that can be overridden in a subclass to handle the event of a widget being closed. This event is triggered when a user attempts to close a window, typically by clicking the "X" button in the title bar or by choosing "Close" from the window menu, or when QWidget::close() is called programmatically.
Purpose of overriding closeEvent:
Confirmation dialogs:
Prompting the user to confirm if they truly want to close the application or a specific window, especially if there are unsaved changes.
Saving data:
Performing actions like saving application settings, user preferences, or document changes before the window closes.
Resource cleanup:
Releasing resources, closing files, or stopping threads that are running in the background.
How to implement closeEvent:
Subclass QMainWindow or QWidget:
Create a custom class that inherits from QMainWindow (for main windows) or QWidget (for other widgets).
Override the closeEvent method:
Define a method named closeEvent within your custom class, which takes a QCloseEvent object as an argument.
Key points:
event.accept(): Call this method within closeEvent to allow the window to close.
event.ignore(): Call this method to prevent the window from closing, for example, if the user cancels the close operation in a confirmation dialog.
QCloseEvent: The event object passed to closeEvent is an instance of QCloseEvent, which provides methods like accept() and ignore().   
    '''
    
# from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from PyQt5.QtGui import QCloseEvent
# import sys

# class MyMainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My PyQt5 Application")
#         self.setGeometry(100, 100, 400, 300)

#     def closeEvent(self, event: QCloseEvent):
#         reply = QMessageBox.question(self, 'Message',
#                                         "Are you sure to quit?", QMessageBox.Yes |
#                                         QMessageBox.No, QMessageBox.No)

#         if reply == QMessageBox.Yes:
#             event.accept()  # Accept the close event, allowing the window to close
#         else:
#             event.ignore()  # Ignore the close event, preventing the window from closing

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MyMainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())
