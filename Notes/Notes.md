
https://github.com/alandmoore/PyQt-Videos-Examples/blob/master/HelloWorldqt/template.py
repository for Alan D Moore's tutorials

## 19 April 11 AM this is my most recent version of the calculator
# MyCalc_1.py is my most current calculator
# This is a simple calculator application using PyQt5. I am using MyCalc_backup_1.py as the UI file generated by Qt Designer.
# It includes basic arithmetic operations and a simple user interface.  
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
# from MyCalc_backup_1 import Ui_MainWindow  # assuming this file is saved as calc.py
from MyCalc_backup_1 import Ui_MyCalculator  # assuming this file is saved as calc.py

class Calculator(QMainWindow, Ui_MyCalculator):
# class Calculator(QMainWindow, Ui_MainWindow):

NOTE i am holding on to MyCalc.py in Codemy folder sicne it has some work on functions i want to preserve