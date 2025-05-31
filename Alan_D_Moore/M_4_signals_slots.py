


## first is my version, 2d is tutorial
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
        
#         # user_label =qtw.QLabel('username')## when we use the Form layout, we can add the labels directly and do NOT need QLabel!!
#         # password_label = qtw.QLabel('password')
#         authenticated = qtc.pyqtSignal(str)  # Add this at class level
#         self.user_input = qtw.QLineEdit() ## had to make these self. to be reocgnized by the methods we will develop now
#         self.password_input = qtw.QLineEdit()
#         self.password_input.setEchoMode(qtw.QLineEdit.Password) ## uses the ACCESS METHOD
#         ## below an alternative if lots of properites to enter, but not always works, bundle properties with the QLineEdit() CONSTRUCTOR
#         # password_input=qtw.QLineEdit(echoMode=qtw.QLineEdit.Password)
        
#         check_box = qtw.QCheckBox('legalese accept')
#         check_box.setGeometry(qtc.QRect(130, 190, 85, 20))# my addition. no wffect?
#         self.login_button= qtw.QPushButton('login')

#         self.cancel_button = qtw.QPushButton('cancel')
        
#         ## need an intermiary object called a layout
#         layout = qtw.QFormLayout() ## now need to give positional arguemtns of rows and columns
        
#         ## need an intermiary object called a layout
#         # layout = qtw.QVBoxLayout() used this before but not here since we are using a grid
#         layout.addRow('user_name',self.user_input,)
#         layout.addRow('password',self.password_input,)
        
#         check_box_widget=qtw.QWidget()
#         check_box_widget.setLayout(qtw.QHBoxLayout())
#         check_box_widget.layout().addWidget(check_box)
#         layout.addRow('',check_box_widget)
        
#         ## will create for this last eaxample a button_widget =qtw.QWidget()
#         button_widget =qtw.QWidget() ## will place buttons inside
#         button_widget.setLayout(qtw.QHBoxLayout())
#         button_widget.layout().addWidget(self.cancel_button)
#         button_widget.layout().addWidget(self.login_button)
#         layout.addRow('', button_widget)
#         self.setLayout(layout) ## this is where we connect the 'layout=qtw.QFormLayout (or H or V or Grid) to the class
        
        
#         ## can add layouts to layouts,  cannot widget to layouots.  layouts can be added to either a widget or layouot
#         ## need to tell this class that this layout is for this class
#         self.setLayout(layout)
#         ## want to start adding functioanality
#         # cancel_button.clicked.connect(self.close)## close is the slot
#         # cancel_button.pressxed.connect(self.close)## close is the slot
        
#         self.cancel_button.released.connect(self.close)## close is the slot, toggle() is another option
#         # self.login_button.clicked.connect(clicked = lambda : self.authenticate()) ## wrong do not use clicked
#         self.login_button.clicked.connect(lambda: authenticate(self))

#         # self.login_button.clicked.connect(self.authenticate)
#         # Your code ends here
#         self.show() ## put it here so the window shows.

#     # def authenticate(self):

#     #     username = self.user_input.text()
#     #     password = self.password_input.text()

#     #     if username == 'user' and password == 'pass':
#     #         qtw.QMessageBox.information(self, 'Success', 'You are logged in.')
#     #         self.authenticated.emit(username)
#     #     else:
#     #         qtw.QMessageBox.critical(self, 'Failed', 'You are not logged in.')
# def authenticate(self):

#         username = self.user_input.text()
#         password = self.password_input.text()

#         if username == 'user' and password == 'pass':
#             qtw.QMessageBox.information(self, 'Success', 'You are logged in.')
#             self.authenticated.emit(username)
#         else:
#             qtw.QMessageBox.critical(self, 'Failed', 'You are not logged in.')        

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
   
#########~~~~~tutorial version https://github.com/alandmoore/PyQt-Videos-Examples/blob/master/PyQtSignalsAndSlots/login_app.py

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    authenticated = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(
            qtw.QLineEdit.Password)

        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Login')

        layout = qtw.QFormLayout()
        layout.addRow('Username', self.username_input)
        layout.addRow('Password', self.password_input)

        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.submit_button)
        layout.addRow('', button_widget)
        self.setLayout(layout)

        self.cancel_button.clicked.connect(self.close)
        self.submit_button.clicked.connect(self.authenticate)

        self.username_input.textChanged.connect(self.set_button_text)
        self.authenticated.connect(self.user_logged_in)

        # Your code ends here
        self.show()

    def set_button_text(self, text):
        if text:
            self.submit_button.setText(f'Log In {text}')
        else:
            self.submit_button.setText('Log In')

    def authenticate(self):

        username = self.username_input.text()
        password = self.password_input.text()

        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'Success', 'You are logged in.')
            self.authenticated.emit(username)
        else:
            qtw.QMessageBox.critical(self, 'Failed', 'You are not logged in.')

    def user_logged_in(self, username):

        qtw.QMessageBox.information(self, 'Logged in', f'{username} is logged in.')

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
'''


1 Incorrect use of lambda with clicked.connect()
This line:
python
Copy
Edit
self.login_button.clicked.connect(clicked = lambda : self.authenticate())
is invalid Python syntax because the connect() method does not accept a keyword argument called clicked.
✅ Fix:
python
Copy
Edit
self.login_button.clicked.connect(lambda: authenticate(self))
2   You're calling the standalone authenticate() function, which needs self passed in — so your lambda must pass self.
authenticate() is outside the class, but it tries to use self.authenticated.emit()
In your current authenticate(self) function, this line will cause an error:
python
Copy
Edit
self.authenticated.emit(username)
That's because:
You never define self.authenticated in the MainWindow class.
Even in Version One, it's undefined — so that part would crash too if reached.
✅ Fix or Remove:
If you don’t use self.authenticated elsewhere, just remove this line for now:
python
Copy
Edit
# self.authenticated.emit(username)  # Remove or comment this out
Or if you want to use it later, define the signal properly inside the class:
python
Copy
Edit
class MainWindow(qtw.QWidget):
    authenticated = qtc.pyqtSignal(str)  # Add this at class level
✅ Summary of Fixes
Working Version Two (simplified):
python
Copy
Edit
def authenticate(self):
    username = self.user_input.text()
    password = self.password_input.text()

    if username == 'user' and password == 'pass':
        qtw.QMessageBox.information(self, 'Success', 'You are logged in.')
        # self.authenticated.emit(username)  # Only use if defined
    else:
        qtw.QMessageBox.critical(self, 'Failed', 'You are not logged in.')
In __init__:
python
Copy
Edit
self.login_button.clicked.connect(lambda: authenticate(self))
'''
'''
I asked about the recommnedation to add to the class level: authenticated = qtc.pyqtSignal(str)  # Add this at class level

You're absolutely right that in Python, functions must be defined before they're used, especially in cases like lambda or passing a function reference.
✅ About authenticated = qtc.pyqtSignal(str)
🔹 What it does:
This creates a custom signal named authenticated that can emit a string (e.g., a username). It's used in PyQt5 to implement communication between objects—usually from child widgets to parent widgets or other parts of the app.
🔹 Correct terminology:
This is not instantiating an object, but declaring a signal. The correct technical term is:
"Defining a signal" (or declaring a signal at class level)
In context:
python
Copy
Edit
class MainWindow(qtw.QWidget):
    authenticated = qtc.pyqtSignal(str)  # Defining a custom signal
🔹 When and why:
You’d use a signal like this if you want other parts of your application to react when a user successfully logs in.
✅ How to use it in your class:
Define the signal at class level:
python
Copy
Edit
class MainWindow(qtw.QWidget):
    authenticated = qtc.pyqtSignal(str)
Emit the signal when login is successful:
python
Copy
Edit
self.authenticated.emit(username)
Connect it to a slot or handler:
python
Copy
Edit
w = MainWindow()
w.authenticated.connect(lambda user: print(f"{user} is logged in!"))
🔗 Recommended Resources:
Here's a clear and official PyQt5 reference:
Signals and Slots in PyQt5 (official docs)
Or for a tutorial format:
Real Python: Mastering PyQt5 Signals and Slots
Would you like a minimal working example showing the signal in action?

'''
## this one below was from ChatGPT and did not work. the problem was:
# Explanation of Changes:
# self.hide() is added to hide the main window at first.
# self.show() is called in handle_login() to display the main window after login.
# The issue:
# In the example I gave, the MainApp creates and shows both:
# itself (main.show()), and
# the LoginForm as a separate popup window.
# However, since MainApp is already shown, and the login form is not modal (i.e., doesn't block interaction), the program doesn't wait for the login before showing the main app. So even after emitting the signal, the update (self.label.setText(...)) might not be visible or executed as expected.
# ✅ Fix: Hide the main window until login is complete
# Update MainApp.__init__() so that:
# It does not show itself until login is successful.
# After LoginForm emits the signal, it shows the main app.
## these fixes are in the last program after this one below

# from PyQt5 import QtWidgets as qtw, QtCore as qtc

# class LoginForm(qtw.QWidget):
#     # Define the custom signal (class-level)
#     authenticated = qtc.pyqtSignal(str)

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Login")

#         # Layout
#         layout = qtw.QVBoxLayout()
#         self.user_input = qtw.QLineEdit(self)
#         self.user_input.setPlaceholderText("Username")
#         login_button = qtw.QPushButton("Login", self)

#         layout.addWidget(self.user_input)
#         layout.addWidget(login_button)
#         self.setLayout(layout)

#         # Connect login button
#         login_button.clicked.connect(self.authenticate)

#     def authenticate(self):
#         username = self.user_input.text()
#         if username:  # pretend this is real authentication
#             self.authenticated.emit(username)  # emit the signal
#             self.close()


# class MainApp(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Main App")
#         self.resize(300, 100)
#         self.label = qtw.QLabel("Not logged in", self)
#         layout = qtw.QVBoxLayout()
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         # Show login form
#         self.login_form = LoginForm()
#         self.login_form.authenticated.connect(self.handle_login)
#         self.login_form.show()

#     def handle_login(self, username):
#         self.label.setText(f"Welcome, {username}!")


# if __name__ == "__main__":
#     app = qtw.QApplication([])
#     main = MainApp()
#     main.show()
#     app.exec_()

# from PyQt5 import QtWidgets as qtw, QtCore as qtc

# class LoginForm(qtw.QWidget):     ###Chat
#     authenticated = qtc.pyqtSignal(str)

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Login")

#         # Layout
#         layout = qtw.QVBoxLayout()
#         self.user_input = qtw.QLineEdit(self)
#         self.user_input.setPlaceholderText("Username")
#         login_button = qtw.QPushButton("Login", self)

#         layout.addWidget(self.user_input)
#         layout.addWidget(login_button)
#         self.setLayout(layout)

#         # Connect login button
#         login_button.clicked.connect(self.authenticate)

#     def authenticate(self):
#         username = self.user_input.text()
#         if username.strip():  # basic check
#             self.authenticated.emit(username)
#             self.close()


# class MainApp(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Main App")
#         self.resize(300, 100)

#         self.label = qtw.QLabel("Not logged in", self)
#         layout = qtw.QVBoxLayout()
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         # Start with login form
#         self.login_form = LoginForm()
#         self.login_form.authenticated.connect(self.handle_login)
#         self.login_form.show()
#         self.hide()  # hide main window until login completes

#     def handle_login(self, username):
#         self.label.setText(f"Welcome, {username}!")
#         self.show()  # now show main window after login


# if __name__ == "__main__":
#     app = qtw.QApplication([])
#     main = MainApp()
#     app.exec_()
