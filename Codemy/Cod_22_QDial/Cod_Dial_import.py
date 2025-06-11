'''https://www.youtube.com/watch?v=XXPNpdaK9WA&t=2016s


'''


# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# from Cod_Dial import Ui_MainWindow as GeneratedMainWindow  # Import the generated UI class
# class CustomMainWindow(qtw.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)  # Call the parent constructor
#         self.ui = GeneratedMainWindow()  # Create an instance of the UI class
        
#         self.ui.setupUi(self)  # Set up the UI in the main window
#         self.setWindowTitle('My Window')  # Set the window title
#         self.dial = self.ui.dial  # Access the dial widget from the UI
#         self.dial.valueChanged.connect(self.update_label)  # Connect the dial value change to the label update
#         self.label = self.ui.label
#         self.label.setText("Current Position: 0")  # Initialize the label with the current dial value
#         self.dial.setRange(0, 100)
#     def update_label(self, value):
#         self.label.setText(f"Current Position: {value}")  # Update the label with the current dial value        
#         self.dial.setWrapping(True)  # Enable wrapping to allow full 360-degree rotation
#         self.show()  # Show the main window
#         # self.dial.valueChanged.connect(lambda value: self.label.setText(f"Current Position: {value}"))  # Connect the dial to the label
#         # self.dial.setRange(0, 100)  # Set the range of the dial
# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)  # Create the application
#     w = CustomMainWindow(windowTitle='My Window')  # Create the main window
#     w.show()  # Show the main window
#     sys.exit(app.exec_())  # Exit the application
# The above code is a complete implementation of a PyQt5 application that uses a QDial widget.
# It creates a main window with a dial and a label that updates to show the current position of the dial.
         


# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from Cod_Dial import Ui_MainWindow  # Import the generated setup class

# class CustomMainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Create the UI object and set up the UI inside self
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         # Access widgets from the UI
#         self.dial = self.ui.dial
#         self.label = self.ui.label

#         # Initialize the dial and label
#         self.dial.setRange(0, 100)
#         self.label.setText("Current Position: 0")

#         # Connect the signal
#         self.dial.valueChanged.connect(self.update_label)

#     def update_label(self, value):
#         self.label.setText(f"Current Position: {value}")

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     window = CustomMainWindow()
#     window.show()
#     sys.exit(app.exec_())

### this will follow the Codemy lesson 22
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from Cod_Dial import Ui_MainWindow as GeneratedMainWindow  # Import the generated UI class
class CustomMainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent constructor
        self.ui = GeneratedMainWindow()  # Create an instance of the UI class
        
        self.ui.setupUi(self)  # Set up the UI in the main window
        self.setWindowTitle('My Window')  # Set the window title
        self.dial = self.ui.dial  # Access the dial widget from the UI
        # self.dial.valueChanged.connect(self.update_label)  # Connect the dial value change to the label update
        ## will try a different approach following the Codemy lesson 22
        self.dial.valueChanged.connect(lambda: self.update_label(self.dial.value()))  # Connect the dial value change to the label update
        
        ## cal def dialer(self):
        self.dial.valueChanged.connect(self.dialer)  # Connect the dial value change to the dialer method
        self.label = self.ui.label
        self.label.setText("Current Position: 0")  # Initialize the label with the current dial value
        self.dial.setRange(0, 100) # self.dial.setMinimum(0) toSet the minimum value of the dial or setMaximum(100)  # Set the maximum value of the dial
        self.dial.setNotchesVisible(True)  # Show the notches on the dial
        self.dial.setWrapping(True)  # Enable wrapping to allow full 360-degree rotation
        self.dial.setPageStep(10)  # Set the page step of the dial, this is the amount the dial moves when you click on the dial
        self.dial.setSingleStep(1)  # Set the single step of the dial, this is the amount the dial moves when you click on the arrow buttons
        self.dial.setNotchTarget(10)  # Set the notch target of the dial, this is the amount the dial moves when you click on the notches
        self.dial.setTracking(True)  # Set the tracking of the dial, this is the amount the dial moves when you click on the dial
        self.dial.setCursor(qtg.QCursor(qtc.Qt.ArrowCursor))  # Set the cursor of the dial to an arrow cursor
        # self.dial.setStyleSheet("QDial { background-color: lightblue; }")  # Set the style of the dial, this is the background color of the dial
        # self.dial.setStyleSheet("QDial { background-color: #332433; }")  # i very nice shade of light purple!! used the color picker to get this color, you can use a hex color code for a nice shade of light purple
        # self.dial.setStyleSheet("QDial { background-color: #D8BFD8; }")  # Set the style of the dial, this is the background color of the dial
        # self.dial.setStyleSheet("QDial { background-color: rgb(216, 191, 216); }")  # i very nice shade of light purple!! used the color picker to get this color, you can
        ## use a hex color code for a nice shade of light purple
        # self.dial.setStyleSheet("QDial { background-color: #D8BFD8; }")  # Set the style of the dial, this is the background color of the dial
        # use rgb for red color of dial
        self.dial.setStyleSheet("QDial { background-color: rgb(255, 0, 0); }")  # i very nice shade of light purple!! Set the style of the dial, this is the background color of the dial
        self.dial.setFocusPolicy(qtc.Qt.StrongFocus)  # Set the focus policy of the dial, this is the focus policy of the dial
        self.dial.setFocus()  # Set the focus on the dial, this is the focus of the dial
        self.dial.setEnabled(True)  # Enable the dial, this is the enabled state of the dial
        self.dial.setDisabled(False)  # Disable the dial, this is the disabled state of the dial
        ## make dial resize with the window
        # Set the size policy of the dial to expanding, allowing it to resize with the window. this does not work in the final code, but it is here for reference
        self.dial.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        ######  not needed but can work with for resizing the dial with the window, i would need to add the labels to the layour
        # Ensure the dial is added to a layout that supports resizing, if i aadd a lyout and then  place the dial in it, it will resize with the window
        ## add the dial to a layout, this will allow the dial to resize with the window
        # self.ui.centralwidget = qtw.QWidget(self)  # Create a central widget for the main window, 
        # self.setCentralWidget(self.ui.centralwidget)  # Set the central widget of the main window 
        
        
        layout = qtw.QVBoxLayout(self.ui.centralwidget)
        layout.addWidget(self.dial)
        # self.ui.centralwidget.setLayout(layout)
        ###############
        self.dial.setToolTip("This is a dial")  # Set the tooltip of the dial, this is the tooltip of the dial
        self.dial.setWhatsThis("This is a dial, you can use it to change the value")  # Set the whats this of the dial, this is the whats this of the dial
        self.dial.setAccessibleName("Dial")  # Set the accessible name of the dial, this is the accessible name of the dial
        self.dial.setAccessibleDescription("This is a dial, you can use it to change the value")  # Set the accessible description of the dial, this is the accessible description of the dial
        ## i want to add a second label to display the current dial value
        ## note i used a lambda function to connect the dial value changed signal to the update_label method
        self.label2=qtw.QLabel(self)  # Create a label to display the current dial value
        self.label2.setGeometry(qtc.QRect(130, 390, 211, 51))  # Set the geometry of the label
        self.ui.label2 = self.label2  # Set the label2 in the UI
        self.label2.setText("Current Dial Value: 0")  # Initialize the label2 with the current dial value
        self.label2.setFont(qtg.QFont("Lucida Grande", 18, qtg.QFont.Bold))  # Set the font of the label2
        self.label2.setAlignment(qtc.Qt.AlignCenter)  # Center the text in the label2
        ## connect the dial value changed to the label2
        self.dial.valueChanged.connect(lambda: self.label2.setText(f"Current Dial Value: {self.dial.value()}"))
        
        self.show()
    def dialer(self):
        value = self.dial.value()
        print(f"Dial value changed to: {value}")  # Print the current dial value to the console
        ## this will print the current dial value to the console
        self.update_label(value)

    def update_label(self, value):
        self.label.setText(f"Current Position: {value}")  # Update the label with the current dial value , value is a string so could need to convert it to a string {str(value)}
        # self.label2.setText(f"Current Dial Value: {str(value)}")  # Update the label2 with the current dial value , this can be done here as well.      
        print(f"Label updated to: {value}")  # Print the updated label value to the console
        # self.dial.setWrapping(True)  # Enable wrapping to allow full 360-degree rotation, !!! handy 
        self.show()  # Show the main window
        # self.dial.valueChanged.connect(lambda value: self.label.setText(f"Current Position: {value}"))  # Connect the dial to the label
        # self.dial.setRange(0, 100)  # Set the range of the dial
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)  # Create the application
    w = CustomMainWindow(windowTitle='My Window')  # Create the main window
    w.show()  # Show the main window
    sys.exit(app.exec_())  # Exit the application










### i am saving ghis code here for future reference, this is the code that was generated by the PyQt5 UI code generator, it is not used in the final code, but it is here for reference.
# # -*- coding: utf-8 -*-   


# class LoginWindow(object):
#     def setupUi(self, MainWindow):
#         # MainWindow.setObjectName("MainWindow")
#         # MainWindow.resize(453, 475)
#         # self.centralwidget = qtw.QWidget(MainWindow)
#         # self.centralwidget.setObjectName("centralwidget")
#         # self.dial = qtw.QDial(self.centralwidget)
#         # self.dial.setGeometry(qtc.QRect(90, 30, 261, 241))
#         # self.dial.setObjectName("dial")
#         # self.label = qtw.QLabel(self.centralwidget)
#         # self.label.setGeometry(qtc.QRect(130, 290, 211, 51))
#         # font = qtg.QFont()
#         # font.setFamily("Lucida Grande")
#         # font.setPointSize(18)
#         # font.setBold(True)
#         # font.setWeight(75)
#         # self.label.setFont(font)
#         # self.label.setObjectName("label")
#         # MainWindow.setCentralWidget(self.centralwidget)
#         # self.menubar = qtw.QMenuBar(MainWindow)
#         # self.menubar.setGeometry(qtc.QRect(0, 0, 453, 24))
#         # self.menubar.setObjectName("menubar")
#         # MainWindow.setMenuBar(self.menubar)
#         # self.statusbar = qtw.QStatusBar(MainWindow)
#         # self.statusbar.setObjectName("statusbar")
#         # MainWindow.setStatusBar(self.statusbar)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here

#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = LoginWindow(windowTitle='My Window')
#     w.setupUi(w)
#     w.show()    ## this is the main window, we need to call the setupUi method to set up the window
#     # w.dial.valueChanged.connect(lambda value: w.label.setText(f"Current Position: {value}"))  ## connect the dial to the label
#     # ## this is the main window, we need to call the setupUi method to set up the window
#     # w.dial.setRange(0, 100)  ## set the range of the dial
#     # w.dial.setValue(0)  ## set the initial value of the dial
#     # w.dial.setNotchesVisible(True)  ## show the notches on the dial
#     # w.dial.setWrapping(True)  ## allow the dial to wrap around when it reaches the end of the range
#     # w.dial.setPageStep(10)  ## set the page step of the dial, this is the amount the dial moves when you click on the dial
#     # w.dial.setSingleStep(1)  ## set the single step of the dial, this is the amount the dial moves when you click on the arrow buttons
#     # w.dial.setNotchTarget(10)  ## set the notch target of the dial, this is the amount the dial moves when you click on the notches
#     # w.dial.setWrapping(True)  ## allow the dial to wrap around when it reaches the end of the range
#     # w.dial.setTracking(True)  ## set the tracking of the dial, this is the amount the dial moves when you click on the dial
#     # w.dial.setCursor(qtg.QCursor(qtg.Qt.ArrowCursor))  ## set the cursor of the dial to an arrow cursor
#     # w.dial.setStyleSheet("QDial { background-color: lightblue; }")  ## set the style of the dial, this is the background color of the dial
#     # w.dial.setFocusPolicy(qtc.Qt.StrongFocus)  ## set the focus policy of the dial, this is the focus policy of the dial
#     # w.dial.setFocus()  ## set the focus on the dial, this is the focus of the dial
#     # w.dial.setEnabled(True)  ## enable the dial, this is the enabled state of the dial
#     # w.dial.setDisabled(False)  ## disable the dial, this is the disabled state of the dial
#     # w.dial.setToolTip("This is a dial")  ## set the tooltip of the dial, this is the tooltip of the dial
#     # w.dial.setWhatsThis("This is a dial, you can use it to change the value")  ## set the whats this of the dial, this is the whats this of the dial
#     # w.dial.setAccessibleName("Dial")  ## set the accessible name of the dial, this is the accessible name of the dial
#     # w.dial.setAccessibleDescription("This is a dial, you can use it to change the value")  ## set the accessible description of the dial, this is the accessible description of the dial
#     # w.dial.setAccessibleText("This is a dial, you can use it to change the value")  ## set the accessible text of the dial, this is the accessible text of the dial
#     # w.dial.setAccessibleRole(qtc.QAccessible.Dial)  ## set the accessible role of the dial, this is the accessible role of the dial
#     # w.dial.setAccessibleDescription("This is a dial, you can use it to change the value")  ## set the accessible description of the dial, this is the accessible description of the dial
#     # w.dial.setAccessibleName("Dial")  ## set the accessible name of the dial, this is the accessible name of the dial
#     # w.dial.setAccessibleText("This is a dial, you can use it to change the value")  ## set the accessible text of the dial, this is the accessible text of the dial
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

