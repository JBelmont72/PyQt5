'''
geeks for keeeks and pythonGuis.com    widgets

.setCheckState   .stateChanged.connect
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
### i will combine the label and the  two checkboxes plus lambda: My most complete

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
#         # self.myCheckBox.setCheckState(qtc.Qt.Checked)  ## optional sets the value to begin the program
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

