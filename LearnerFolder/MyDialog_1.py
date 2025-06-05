'''

my tutorial for this is Pythonguis.com
dialog boxes  
n
'''
# import sys

# from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)
    
#     def button_clicked(self, s):
#         print("click", s)

#         dlg = QDialog(self)
#         dlg.setWindowTitle("HELLO!")
#         dlg.exec()


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
# from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = qtw.QPushButton("Press me for a dialog!",self)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")
    # def button_clicked(self, s):
    #     print("click", s)

    #     dlg = qtw.QDialog(self)
    #     dlg.setWindowTitle("HELLO!")
    #     dlg.exec()

class CustomDialog(qtw.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = qtw.QDialogButtonBox.Ok | qtw.QDialogButtonBox.Cancel

        self.buttonBox = qtw.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout =qtw. QVBoxLayout()
        message = qtw.QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()