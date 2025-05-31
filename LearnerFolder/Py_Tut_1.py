'''
from python tutorial website as guide
https://www.pythontutorial.net/pyqt/pyqt-signals-slots/#introduction-to-the-pyqt-signals-and-slots
'''

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle('this is my GUI')
        self.setGeometry(12,12,600,600)
        self.setStyleSheet('background-color: yellow;')
        layout=qtw.QVBoxLayout()
        h_layout=qtw.QHBoxLayout()
        myLabel=qtw.QLabel('enter')
        myLineEdit= qtw.QLineEdit()
        h_layout.addStretch()
        h_layout.addWidget(myLabel)
        h_layout.addWidget(myLineEdit)
        h_layout.setContentsMargins(50,100,30,100)
        h_layout.addStretch()
        layout.addLayout(h_layout)
        h2_layout=qtw.QHBoxLayout()
        titles= ['Yes','No','Cancel']
        for title in titles:
            buttons =[qtw.QPushButton(title) for title in titles]## this gives a list of qtw.QPushbutton('yes) etc
            
        for button in buttons:
            button.setStyleSheet('background-color: green;')
            h2_layout.addWidget(button)
          
        
        # set the stretch factors
        h2_layout.setStretchFactor(buttons[0], 4)
        h2_layout.setStretchFactor(buttons[1], 4)
        h2_layout.setStretchFactor(buttons[2], 1)
        layout.addLayout(h2_layout)
        ## use setStretch is set pixels between buttons
        
        
        # self.setLayout(h_layout)## not needed
        self.setLayout(layout)
        layout.addStretch()

        self.show()
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window =MainWindow()
    # window.show()
    sys.exit(app.exec_())
    
    
    
    
###########
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('My Brand New GUI')
#         self.setGeometry(10,10,600,400)
#         self.setMinimumSize(200,100)
#         self.setAutoFillBackground(True)
#         self.setStyleSheet(" background-color: lightgreen;")
#         layout = qtw.QVBoxLayout()
#         h_layout = qtw.QHBoxLayout()
#         layout.addLayout(h_layout)
#         titles = ['Open','Close','Cancel']
#         h_layout.addStretch()# by adding stretch here I placed stretch at the very begining
#         buttons =[qtw.QPushButton(title) for title in titles]
#         for button in buttons:
#             button.setStyleSheet('background-color: yellow;')
        
#             h_layout.addWidget(button)
#             h_layout.addStretch()
            
#         self.setLayout(layout)
#         self.show()


# if __name__ == '__main__':
#     app =qtw.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


##########
# importing libraries I used list comprhension and .get() to retieve the value of key value paris for the comboBox
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

#         # creating a combo box widget
#         self.combo_box = QComboBox(self)

#         # setting geometry of combo box
#         self.combo_box.setGeometry(200, 150, 150, 30)

#         # geek list
#         # geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]
#         geek_list=  {1: '001', 2: '010', 3: '011'}

#         # print(d.get(4, "Not found"))
#         # making it editable
#         self.combo_box.setEditable(True)

#         # adding list of items to combo box
#         # self.combo_box.addItems(geek_list)
        
#         boxes = [self.combo_box.addItem(geek_list.get(geek)) for geek in geek_list]
#         for box in boxes:
#             box
        
#         # self.combo_box.addItems(geek_list.get)
        
        
#         self.combo_box.setStyleSheet("QComboBox"
#                                      "{"
#                                      "background-color: lightgreen;"
#                                      "}")


# # create pyqt5 app
# App = QApplication(sys.argv)

# # create the instance of our Window
# window = Window()

# # start the app
# sys.exit(App.exec())



#####
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here

#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

