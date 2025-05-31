# -*- coding: utf-8 -*-

## with radioboxes you can only have one working at a time.  the lambda functuion passes self, and a variable
## the variable will do whatever depending which radiobutton was selected.
'''
   def winter(self, state):
        sender = self.sender()  # Get the checkbox that triggered the state change
        if state == QtCore.Qt.Checked:
            print(f'{sender.text()} is Checked')
        elif state == QtCore.Qt.Unchecked:
            print(f'{sender.text()} is Unchecked')
        self.checked()  # Update the label based on the current state of the checkboxes
'''
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget,clicked=lambda: self.label.setText(f'{self.label1.text()} selected'))
        # self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget,clicked=lambda: self.label.setText(f' selected'))
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget, clicked=lambda: self.checked())
        ## set checkBox1 to checked by default
        self.checkBox1.setChecked(True)  # Set the first checkbox to be checked by default
        self.checkBox1.setGeometry(QtCore.QRect(150, 50, 185, 20))
        # self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)  
        self.checkBox1.setGeometry(QtCore.QRect(150, 50, 185, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.checkBox1.setFont(font)
        self.checkBox1.setTristate(False)## if true, then 0,1,2 is .checkState(), .checked() is still 0,1
        self.checkBox1.setObjectName("checkBox1")
        # self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget,clicked = lambda:self.checked())
        self.checkBox2.setChecked(False)
        self.checkBox2.setGeometry(QtCore.QRect(150, 120, 85, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checkBox2.setFont(font)
        self.checkBox2.setObjectName("checkBox2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 190, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.label.setFrameShape(QtCore.Qt.QFrame::Shape::Box)
        # self.label.setFrameShadow(QtCore.Qt.QFrame::Shadow::Raised)
        self.label.setObjectName("label")
        
        # QLabel *label = new QLabel(this);
        # label->setFrameStyle(QFrame::Panel | QFrame::Sunken);
        # label->setText("first line\nsecond line");
        # label->setAlignment(Qt::AlignBottom | Qt::AlignRight);
        # label=QLabel('this')

        # Python equivalent code: of the above C++ code for a second label
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setFrameShape(QtWidgets.QFrame.Panel|QtWidgets.QFrame.Sunken )
        self.label1.setGeometry(QtCore.QRect(10, 10, 241, 41))
        # label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label1.setText("first line\nsecond line")
        self.label1.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.label1.setObjectName('label1')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        ## radiobuttons  when use lamdaa function  add self,vaviable   but cannot with checkboxes
        # update check Boxes
        # self.checkBox1.stateChanged.connect(lambda :self.Mushromm)
        # self.checkBox2.toggled.connect(lambda).Mushroom)
        # self.checkBox1.stateChanged.connect(self.winter) # not so good
        # self.checkBox2.stateChanged.connect(self.winter)# not so good 
        self.checkBox1.stateChanged.connect(lambda state: self.winter(self.checkBox1, state))
        self.checkBox2.stateChanged.connect(lambda state: self.winter(self.checkBox2, state))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ## without the submit button, how to handle the check boxes, two ways
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox1.setText(_translate("MainWindow", "Red"))
        self.checkBox2.setText(_translate("MainWindow", "Blue"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Choose a color"))
    def checked(self):
        ### states: 0=not checked,1= true but if triState then half check is 1 and full check is 2
        print(self.checkBox1)   #<PyQt5.QtWidgets.QCheckBox object at 0x100c9a5f0>
        print(self.checkBox1.isChecked())
        print(self.checkBox1.checkState())
        ## can use this info for python if statements  if self.checkBox1 .isChecked() ==True:   etc
        if self.checkBox1.isChecked():
            self.red ='Red'
        else:
            self.red =''
        if self.checkBox2.isChecked():
            self.blue ='Blue'
        else:
            self.blue =''
        self.label.setText(f'{self.red}{self.blue}')
        if self.blue == 'Blue' or self.red =='Red':
            self.label1.setText(f'you chose :{self.red} {self.blue}')
        else:
            self.label1.setText(f'You have not chosen a checkbox')
        # self.label1.setText(f' \n{self.red} {self.blue}')
    def winter(self, checkbox, state):
        if state == QtCore.Qt.Checked:
            print(f'{checkbox.text()} is Checked')
        elif state == QtCore.Qt.Unchecked:
            print(f'{checkbox.text()} is Unchecked')
        elif state == QtCore.Qt.PartiallyChecked:
            print(f'{checkbox.text()} is Partially Checked')

        self.checked()  # Update label

'''JBelmont72: why this error :  typeError: Ui_MainWindow.winter() missing 1 required positional argument: 'checkbox'

GitHub.copilot-chat.github.copilot.editor: The error occurs because the `winter` method is connected to the `stateChanged` signal, which only passes the state as an argument, but your `winter` method expects both `state` and `checkbox` arguments. To fix this, modify the `winter` method to accept only the `state` argument and use `self.sender()` to identify the checkbox that triggered the signal.



Made changes.'''    
           
        #     self.label.setText(f'{self.label.text()} Red')
        # else:
        #     self.label.setText(self.label.text().replace("Red", "").strip())

        # if self.checkBox2.isChecked():
        #     self.label.setText(f'{self.label.text()} Blue')
        # else:
        #     self.label.setText(self.label.text().replace('Blue', '').strip())
        # if not self.checkBox1.isChecked() and not self.checkBox2.isChecked():
        # self.label1.setText("Choose a color")
        # self.label.setText(f'{self.label.text()} {self.checkBox1.text()} {self.checkBox2.text()}')
        # # self.label.setText(f'{self.label.text()} {self.checkBox1.isChecked()} {self.checkBox2.isChecked()}')
        
        # self.pushButton.clicked.connect(self.checked)
        # self.pushButton.clicked.connect(self.checked)
        # self.pushButton.clicked.connect(lambda: self.label.setText(f'{self.label.text()} selected'))
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
