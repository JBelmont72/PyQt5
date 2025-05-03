'''  This is the second and third ways to open and use the .ui file
1. copy the Template.py 
'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from myLogin import Ui_LoginForm


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here
        self.ui=Ui_LoginForm()
        self.ui.setupUi(self)
        # Your code ends here
        self.show() ## put it here so the window shows.


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
