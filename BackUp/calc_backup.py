'''
JBelmont72: self.OutputLabel.setFrameShape(QtCore.Qt.QFrame::Shape::Box)

GitHub.copilot-chat.github.copilot.editor: Made changes.

JBelmont72: what is the correct version of # self.OutputLabel.setFrameShape(QtCore.Qt.QFrame::Shape::Box)

GitHub.copilot-chat.github.copilot.editor: The syntax you provided is incorrect because Python does not use `::` for accessing members. Instead, Python uses the dot (`.`) operator. Here's the corrected version:

```python
self.OutputLabel.setFrameShape(QtCore.QFrame.Shape.Box)
```

### Explanation:
1. **`QtCore.QFrame.Shape.Box`**:
   - `QtCore.QFrame` refers to the `QFrame` class in the `QtCore` module.
   - `Shape` is an enumeration within `QFrame` that defines different frame shapes.
   - `Box` is one of the possible values of the `Shape` enumeration.

2. **`setFrameShape`**:
   - This method is used to set the shape of the frame for a `QFrame`-based widget (like `OutputLabel` in your case).

Make sure that `self.OutputLabel` is an instance of a `QFrame` or a subclass of it (e.g., `QLabel`), as this method is specific to `QFrame`.
```````````
  my Error:   ui.setupUi(MainWindow)
  File "/Users/judsonbelmont/Documents/SharedFolders/Pico/PyQt5/Codemy/calc.py", line 43, in setupUi
    self.OutputLabel.setFrameShape(QtCore.QFrame.Shape.Box)
                                   ^^^^^^^^^^^^^
AttributeError: module 'PyQt5.QtCore' has no attribute 'QFrame'

Response: The error you're encountering indicates that the QFrame class is not being accessed correctly. In PyQt5, QFrame is part of the QtWidgets module, not QtCore.

Correcting the Code

You need to import QFrame from QtWidgets and use it directly. Here’s how you can modify your code:

Change the import statement: Ensure you are importing QFrame from QtWidgets.
Update the usage of QFrame: Use QtWidgets.QFrame instead of QtCore.QFrame.
I need to see if i can change the qt enum cleaner to do this automatically.!!!!!!

'''
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFrame  # Import QFrame from QtWidgetsrecommended

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(10, 20, 371, 70))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        self.OutputLabel.setFont(font)
        
        
        # Use QtWidgets.QFrame instead of QtCore.QFrame
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)  # Corrected line
        self.OutputLabel.setFrameShadow(QtWidgets.QFrame.Raised)  # Corrected line
        self.OutputLabel.setLineWidth(4)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)  # Corrected line
        self.OutputLabel.setObjectName("OutputLabel")
        
        # ... (rest of your button setup code remains unchanged)
        
        
        
        
        
        
        
        
        
        ## correct way to set alignment for QLabels is self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.OutputLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # self.OutputLabel.setFrameShape(QtCore.QFrame.Shape.Box)
        # self.OutputLabel.setFrameShadow(QtCore.QFrame.Shadow.Raised)
        # # self.OutputLabel.setFrameShape(QtCore.QFrame.Shape.Box)
        # # self.OutputLabel.setFrameShape(QtCore.Qt.QFrame::Shape::Box)
        # # self.OutputLabel.setFrameShadow(QtCore.Qt.QFrame::Shadow::Raised)
        # self.OutputLabel.setLineWidth(4)
        # self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)  # Corrected line
        # # self.OutputLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)##error line
        # self.OutputLabel.setObjectName("OutputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget)
        self.percentButton.setGeometry(QtCore.QRect(20, 100, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.C_Button = QtWidgets.QPushButton(self.centralwidget)
        self.C_Button.setGeometry(QtCore.QRect(110, 100, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.C_Button.setFont(font)
        self.C_Button.setObjectName("C_Button")
        self.shiftButton = QtWidgets.QPushButton(self.centralwidget)
        self.shiftButton.setGeometry(QtCore.QRect(200, 100, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.shiftButton.setFont(font)
        self.shiftButton.setObjectName("shiftButton")
        self.slashButton = QtWidgets.QPushButton(self.centralwidget)
        self.slashButton.setGeometry(QtCore.QRect(300, 100, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.slashButton.setFont(font)
        self.slashButton.setObjectName("slashButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(200, 190, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(110, 190, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(20, 190, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.xButton = QtWidgets.QPushButton(self.centralwidget)
        self.xButton.setGeometry(QtCore.QRect(300, 190, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.xButton.setFont(font)
        self.xButton.setObjectName("xButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(200, 280, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(110, 280, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(20, 280, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(300, 280, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(200, 370, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(110, 370, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(20, 370, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget)
        self.plusButton.setGeometry(QtCore.QRect(300, 370, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.sqButton = QtWidgets.QPushButton(self.centralwidget)
        self.sqButton.setGeometry(QtCore.QRect(110, 470, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.sqButton.setFont(font)
        self.sqButton.setObjectName("sqButton")
        self.logButton = QtWidgets.QPushButton(self.centralwidget)
        self.logButton.setGeometry(QtCore.QRect(20, 470, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.logButton.setFont(font)
        self.logButton.setObjectName("logButton")
        self.cosButton = QtWidgets.QPushButton(self.centralwidget)
        self.cosButton.setGeometry(QtCore.QRect(200, 470, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.cosButton.setFont(font)
        self.cosButton.setObjectName("cosButton")
        self.sinButton = QtWidgets.QPushButton(self.centralwidget)
        self.sinButton.setGeometry(QtCore.QRect(300, 470, 74, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.sinButton.setFont(font)
        self.sinButton.setObjectName("sinButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OutputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.C_Button.setText(_translate("MainWindow", "C"))
        self.shiftButton.setText(_translate("MainWindow", "<<"))
        self.slashButton.setText(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.xButton.setText(_translate("MainWindow", "x"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.sqButton.setText(_translate("MainWindow", "sq"))
        self.logButton.setText(_translate("MainWindow", "log"))
        self.cosButton.setText(_translate("MainWindow", "cos"))
        self.sinButton.setText(_translate("MainWindow", "sin"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())