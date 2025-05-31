'''codemy pyqt5 lesson17
create radioButtons for selecting toppings
'''

# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(411, 511)
#         font = QtGui.QFont()
#         font.setBold(True)
#         MainWindow.setFont(font)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.Pepperoni = QtWidgets.QRadioButton(self.centralwidget) # radioButton
#         self.Pepperoni.setGeometry(QtCore.QRect(140, 60, 121, 21))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         font.setBold(True)
#         self.Pepperoni.setFont(font)
#         self.Pepperoni.setObjectName("Pepperoni")
#         self.cheese = QtWidgets.QRadioButton(self.centralwidget)
#         self.cheese.setGeometry(QtCore.QRect(140, 110, 121, 21))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         font.setBold(True)
#         self.cheese.setFont(font)
#         self.cheese.setObjectName("cheese")
#         self.mushrooms = QtWidgets.QRadioButton(self.centralwidget)
#         self.mushrooms.setGeometry(QtCore.QRect(140, 160, 131, 31))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         font.setBold(True)
#         self.mushrooms.setFont(font)
#         self.mushrooms.setObjectName("mushrooms")
#         # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         ## want to make the pushbutton select the contents of the radiobuttons
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.select('You have selected '))
#         self.pushButton.setGeometry(QtCore.QRect(130, 210, 141, 61))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         font.setBold(True)
#         self.pushButton.setFont(font)
#         self.pushButton.setObjectName("pushButton")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(120, 300, 271, 51)) # changed 171 to 271 width
#         font = QtGui.QFont()
#         font.setFamily("Arial Rounded MT Bold")
#         font.setPointSize(16)
#         font.setUnderline(True)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 24))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.Pepperoni.setText(_translate("MainWindow", "pepperoni"))
#         self.cheese.setText(_translate("MainWindow", "cheese"))
#         self.mushrooms.setText(_translate("MainWindow", "mushrooms"))
#         self.pushButton.setText(_translate("MainWindow", "Pick Topping"))
#         self.label.setText(_translate("MainWindow", "Choose Your Topping"))
        
#     def select(self,var):
#         print(f'{var} selected')
#         self.label.setText(f'{var} an ingredient')
#         if self.Pepperoni.isChecked():
#             self.label.setText(f'{var} pepperoni')
#         if self.cheese.isChecked():
#             self.label.setText(f'{var} cheese')
#         if self.mushrooms.isChecked():
#             self.label.setText(f'{var} pepperoni')
# if __name__ == "__main__":
#     import sys
#     from PyQt5.QtWidgets import QApplication, QMainWindow
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 511)
        font = QtGui.QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Pepperoni = QtWidgets.QRadioButton(self.centralwidget) # radioButton
        self.Pepperoni.setGeometry(QtCore.QRect(140, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Pepperoni.setFont(font)
        self.Pepperoni.setObjectName("Pepperoni")
        self.cheese = QtWidgets.QRadioButton(self.centralwidget)
        self.cheese.setGeometry(QtCore.QRect(140, 110, 221, 21))## changed width from 121 to 221
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.cheese.setFont(font)
        self.cheese.setObjectName("cheese")
        self.mushrooms = QtWidgets.QRadioButton(self.centralwidget)
        self.mushrooms.setGeometry(QtCore.QRect(140, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.mushrooms.setFont(font)
        self.mushrooms.setObjectName("mushrooms")
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        ## want to make the pushbutton select the contents of the radiobuttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.select('You have selected '))
        self.pushButton.setGeometry(QtCore.QRect(130, 210, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 300, 271, 51)) # changed 171 to 271 width
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ## illustrative modifications to the original code above.
        ## changed the connectSlotsByName to connect the button to the select function, both ways work and can work at same time.!! get double print out
        self.pushButton.clicked.connect(lambda: self.select('Your new selection is ')) # using lambda to pass the argument
        # self.pushButton.clicked.connect(self.select) # this will not work as it does not pass the argument    
        ## can set a default radioButton to be checked right from the start
        self.Pepperoni.setChecked(True)  # setting pepperoni as the default topping
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Pepperoni.setText(_translate("MainWindow", "pepperoni"))
        self.cheese.setText(_translate("MainWindow", "cheese"))
        self.mushrooms.setText(_translate("MainWindow", "mushrooms"))
        self.pushButton.setText(_translate("MainWindow", "Pick Topping"))
        self.label.setText(_translate("MainWindow", "Choose Your Topping"))
## above we have only three static toppings, but we can add more dynamically if needed        
    def select(self,var):
        print(f'{var} a topping')
        self.label.setText(f'{var} an ingredient')
        if self.Pepperoni.isChecked():
            self.label.setText(f'{var} pepperoni')
            ## no reason to but if wanted to clear the text of the other two windows could:
            # self.cheese.setText('') ## clears the text of the cheese and mushroom radiobuttons
            # self.mushrooms.setText('')
            ## if wanted to make an automatic second selection when Pepperoni selcted could set the setChecked() for a second button
            self.mushrooms.setChecked(True)
            # self.Pepperoni.setChecked(True)## seems i can not add two setchecked at same time
        if self.cheese.isChecked():
            self.label.setText(f'{var} cheese')
            ## let us change the text on the radio button when it is selected
            self.cheese.setText('Cheese SELECTED')
        if self.mushrooms.isChecked():
            # self.label.setText(f'{var} pepperoni')
            self.label.setText(f'{var}'+ self.mushrooms.text()) # using the text of the radio button directly
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

