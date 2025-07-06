'''
Robotic Maker and Code  

Chat:   https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb 
/Documents/Shared_Folders/PyQt5/LearnerFolder/Py_Tut_3_Chat_CheckBox.py
geeks for geeeks and pythonGuis.com    widgets
Chat 
.setCheckState   .stateChanged.connect
https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/LearnerFolder/Py_Tut_3_CheckBox.py


lambda  structure:      lambda argument: expression
lambda state: self.winter(self.myCheckBox2, state)
state (left side): the argument from the signal.
state (right side): the argument passed into your winter() function.
They are the same value, used to route the signal into your function with the extra checkbox reference.
Using functools instead of lambda:
from functools import partial

self.myCheckBox2.stateChanged.connect(partial(self.winter, self.myCheckBox2))

This creates a new function that always passes self.myCheckBox2 as the first argument to self.winter, and state as the second — just like your lambda.≈


'''
# import sys

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.setWindowTitle("My App")

#         widget = QCheckBox()
#         widget.setTristate(True)
#         widget.setCheckState(Qt.Checked)

#         widget.stateChanged.connect(self.show_state)

#         self.setCentralWidget(widget)

#     def show_state(self, s):
#         print(s == Qt.Checked)
#         print(s)


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()
## i will combine the label and the  two checkboxes plus lambda: My most complete

# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# import sys

# class MainWindow(qtw.QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         self.setWindowTitle('my CheckBox/Label')
#         self. setGeometry(10,10,400,600)
#         layout=qtw.QVBoxLayout()
#         self.setLayout(layout)
#         ## create QLabel and QCheckBox
#         self.myLabel=qtw.QLabel('my initial label')
        
#         self.myCheckBox=qtw.QCheckBox('myCheck Box',self)
#         self.myCheckBox.setTristate()
        
#         self.myCheckBox2=qtw.QCheckBox('number 2',self)
#         self.myCheckBox2.setGeometry(50,100,150,50)
#         self.myCheckBox2.setTristate()
#         self.myCheckBox2.stateChanged.connect(lambda state: self.winter(self.myCheckBox2, state))

        
        
#         layout.addWidget(self.myLabel)
#         layout.addWidget(self.myCheckBox)
#         layout.addWidget(self.myCheckBox2)
#         # self.myCheckBox.setChecked(qtc.Qt.Checked)  ## optional sets the value to begin the program
#         self.myCheckBox.stateChanged.connect(self.function)
#         layout.addStretch()
        
#     def winter(self,checkbox,var):
#         print(checkbox.isChecked(),var)
#         print(qtc.Qt.Checked) ## this is only useful in a conditional statement
    
         
        
        
#     # def winter(self, checkbox, state):
#     #     print(f'state argument: {state} | checkbox.isChecked(): {checkbox.isChecked()}')
#     #     if state == qtc.Qt.Checked:
#     #         print(f'{checkbox.text()} is Checked')
#     #         self.myLabel.setText('Look I\'m checked!')
#     #     elif state == qtc.Qt.Unchecked:
#     #         self.myLabel.setText('Look I\'m unchecked!')
#     #         print(f'{checkbox.text()} is Unchecked')
#     #     elif state == qtc.Qt.PartiallyChecked:
#     #         self.myLabel.setText('Look I\'m partially checked!')
#     #         print(f'{checkbox.text()} is Partially Checked')

#     # def function(self,s):
#     #     print(s)
#     #     if s==2:
#     #         self.myLabel.setText('new label')
#     #     else:
#     #         pass
        
#     def function(self,s):
#         value = qtc.Qt.CheckState(s)
#         print(value)
#         if value==qtc.Qt.CheckState.Checked:
#             print(f'Checked {value}')
#             self.myLabel.setText('value is 2')   
#         if value==qtc.Qt.CheckState.Unchecked:
#             print('UnChecked')
#             self.myLabel.setText('value is 0')   
#         if value==qtc.Qt.CheckState.PartiallyChecked:
#             print('Partially Checked')
#             self.myLabel.setText('value is 1')   
#     # def function(self,s):
#     #     print(self.myCheckBox.isChecked())## gives true or false
#     #     value =self.myCheckBox.isChecked()
#     #     print(f'value {value}')
#     #     if value== True:
#     #         self.myLabel.setText('value is true')
#     #     if value == False:
#     #         self.myLabel.setText('value is false')
            
           
        
        
        
# if __name__ == '__main__':
#     app=qtw.QApplication(sys.argv)
#     window= MainWindow()
#     window.show()
#     sys.exit(app.exec_())

######   https://www.geeksforgeeks.org/pyqt5-ischecked-method-for-check-box/
# importing libraries
# from PyQt5.QtWidgets import * 
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import * 
# from PyQt5.QtCore import * 
# import sys


# class Window(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         # setting title
#         self.setWindowTitle("Python ")

#         # setting geometry
#         self.setGeometry(100, 100, 600, 400)

#         # calling method
#         self.UiComponents()

#         # showing all the widgets
#         self.show()

#     # method for widgets
#     def UiComponents(self):

#         # creating the check-box
#         self.checkbox = QCheckBox('Check box', self)

#         # setting geometry of check box
#         self.checkbox.setGeometry(200, 150, 100, 30)

#         self.checkbox.setChecked(False)## i have the choice of starting the program True or False, default is FALSE
#         # connecting it to function
#         self.checkbox.stateChanged.connect(self.method)

#         # checking if it checked, this gives the current state,gives the inital value
#         check = self.checkbox.isChecked()## this gives the initial state. do not really need

#         # printing the check
#         print(check)

#     def method(self):

#         # printing the checked status
#         print(self.checkbox.isChecked())



# # create pyqt5 app
# App = QApplication(sys.argv)

# # create the instance of our Window
# window = Window()

# # start the app
# sys.exit(App.exec())

##############      https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
##. /Users/judsonbelmont/Documents/Shared_Folders/PyQt5/LearnerFolder/Py_Tut_3_CheckBox.py



# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# import sys

# class MainWindow(qtw.QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         self.setWindowTitle('my CheckBox/Label')
#         self. setGeometry(10,10,400,600)
#         layout=qtw.QVBoxLayout()
#         self.setLayout(layout)
#         ## create QLabel and QCheckBox
#         self.myLabel=qtw.QLabel('my initial label')
        
#         self.myCheckBox=qtw.QCheckBox('myCheck Box',self)
#         self.myCheckBox.setTristate()
        
#         self.myCheckBox2=qtw.QCheckBox('number 2',self)
#         self.myCheckBox2.setGeometry(50,100,150,50)
#         self.myCheckBox2.setTristate()
#         self.myCheckBox2.stateChanged.connect(lambda state: self.winter(self.myCheckBox2, state))

        
        
#         layout.addWidget(self.myLabel)
#         layout.addWidget(self.myCheckBox)
#         layout.addWidget(self.myCheckBox2)
#         self.myCheckBox.setCheckState(qtc.Qt.Checked)  ## optional sets the value to begin the program
#         self.myCheckBox.stateChanged.connect(self.function)
#         layout.addStretch()
#     # def winter(self,checkState,var):
#     #     print(checkState,var) 
#     def winter(self, checkbox, state):
#         print(f'state argument: {state} | checkbox.isChecked(): {checkbox.isChecked()}')

#         if state == qtc.Qt.Checked:
#             print(f'{checkbox.text()} is Checked')
#             self.myLabel.setText('Look I\'m checked!')
#         elif state == qtc.Qt.Unchecked:
#             self.myLabel.setText('Look I\'m unchecked!')
#             print(f'{checkbox.text()} is Unchecked')
#         elif state == qtc.Qt.PartiallyChecked:
#             self.myLabel.setText('Look I\'m partially checked!')
#             print(f'{checkbox.text()} is Partially Checked')


#     # def function(self,s):
#     #     print(s)
#     #     if s==2:
#     #         self.myLabel.setText('new label')
#     #     else:
#     #         pass
        
#     # def function(self,s):
#     #     value = qtc.Qt.CheckState(s)
#     #     print(value)
#     #     if value==qtc.Qt.CheckState.Checked:
#     #         print(f'Checked {value}')
#     #         self.myLabel.setText('value is 2')   
#     #     if value==qtc.Qt.CheckState.Unchecked:
#     #         print('UnChecked')
#     #         self.myLabel.setText('value is 0')   
#     #     if value==qtc.Qt.CheckState.PartiallyChecked:
#     #         print('Partially Checked')
#     #         self.myLabel.setText('value is 1')   
#     def function(self,s):
#         print(self.myCheckBox.isChecked())## gives true or false
#         value =self.myCheckBox.isChecked()
#         print(f'value {value}')
#         if value== True:
#             self.myLabel.setText('value is true')
#         if value == False:
#             self.myLabel.setText('value is false')
            
           
        
        
        
# if __name__ == '__main__':
#     app=qtw.QApplication(sys.argv)
#     window= MainWindow()
#     window.show()
#     sys.exit(app.exec_())
    
    
 #https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb   
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# import sys

# class SkillsForm(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Select Your Skills")
#         layout = qtw.QVBoxLayout()
#         self.setLayout(layout)

#         self.skills = ["Python", "MicroPython", "PyQt5", "OpenCV", "MQTT"]
#         self.checkboxes = []

#         for skill in self.skills:
#             checkbox = qtw.QCheckBox(skill)
#             layout.addWidget(checkbox)
#             self.checkboxes.append(checkbox)

#         submit_btn = qtw.QPushButton("Submit")
#         submit_btn.clicked.connect(self.show_selected_skills)
#         layout.addWidget(submit_btn)

#     def show_selected_skills(self):
        # List =['a','b','   c','one more']## my practice with .join
        # my=''.join(List) ## this turns a list into a string
        # print('you wrote:'+my)
        # print('you wrote:'+''.join(List))## turns list into a string
        # print(type(my))
#         selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
#         msg = "You selected:\n" + "\n".join(selected) if selected else "No skills selected."
#         # msg = f"You selected: {selected}" if selected else "No skills selected."
#         qtw.QMessageBox.information(self, "Selected Skills", msg)
#         self.reset_checkboxes() ## this calls the function to reset the check boxes
#     def reset_checkboxes(self):
#         for cb in self.checkboxes:
#             cb.setCheckState(qtc.Qt.Unchecked)

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     form = SkillsForm()
#     form.show()
#     sys.exit(app.exec_())

# here's a clear example where checkboxes are used to enable or disable other widgets (like sliders and text inputs). This shows how checkbox state dynamically controls interactivity of other widgets — a common real-world pattern in forms, control panels, and PyQt5 dashboards
# ✅ Example: Checkboxes Enable/Disable Other Widgets 
# https://chatgpt.com/c/683f6685-7500-800f-9d41-d76f34d4c7fb
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys

class ControlPanel(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enable/Disable Controls with Checkboxes")
        self.setGeometry(100, 100, 400, 250)
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        # We'll create three pairs of checkbox + control widget (QLineEdit, QSlider, QPushButton)
        self.controls = []

        # 1. Enable/Disable a QLineEdit
        cb1 = qtw.QCheckBox("Enable text input")
        input_field = qtw.QLineEdit()
        input_field.setPlaceholderText("Type something...")
        input_field.setEnabled(False)
        cb1.stateChanged.connect(lambda state, w=input_field: w.setEnabled(state == qtc.Qt.Checked))

        # 2. Enable/Disable a QSlider
        cb2 = qtw.QCheckBox("Enable slider")
        slider = qtw.QSlider(qtc.Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setEnabled(False)
        cb2.stateChanged.connect(lambda state, w=slider: w.setEnabled(state == qtc.Qt.Checked))

        # 3. Enable/Disable a QPushButton
        cb3 = qtw.QCheckBox("Enable button")
        btn = qtw.QPushButton("Click Me!")
        btn.setEnabled(False)
        cb3.stateChanged.connect(lambda state, w=btn: w.setEnabled(state == qtc.Qt.Checked))

        # Add widgets to layout and control list
        for cb, control in [(cb1, input_field), (cb2, slider), (cb3, btn)]:
            layout.addWidget(cb)
            layout.addWidget(control)
            self.controls.append((cb, control))  # ← for later use if needed (reset, iterate, etc.)

        layout.addStretch()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec_())
## recreaate the above using a .ui   I will use QFormLayout
## and then another with opening another window on command by the PushButton
## make an extra checkbox and label in the .ui for later use
