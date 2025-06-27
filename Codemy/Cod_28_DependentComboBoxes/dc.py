'''Dependent comboBoxes   Codemy Pyqt5 gui thursdays #28
first is basic open the .ui
second is to add functionality and pass data between comboboxes
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_28_DependentComboBoxes/dc.py
'''
# from PyQt5.QtWidgets import QMainWindow,QApplication,QComboBox
# from PyQt5 import uic
# import sys

# class MainWIndow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Load the ui file
#         # uic.loadUi('dc.ui',self)
#         uic.loadUi('Codemy/Cod_28_DependentComboBoxes/dc.ui',self)
        
# # Initialize the app
# app = QApplication(sys.argv)
# UIWindow = MainWIndow()
# UIWindow.show()
# app.exec_()

from PyQt5.QtWidgets import QMainWindow,QApplication,QComboBox,QLabel
from PyQt5 import uic
import sys

class MainWIndow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                # Load the ui file
        # uic.loadUi('dc.ui',self)
        uic.loadUi('Codemy/Cod_28_DependentComboBoxes/dc.ui',self)
        self.comboBox =self.findChild(QComboBox,'comboBox')
        self.comboBox_2 =self.findChild(QComboBox,'comboBox_2')
        self.label=self.findChild(QLabel,'label')
        # add items to comboboxes
        self.comboBox.addItem('Male',['John', 'Sam','Kevin','Jon'])
        self.comboBox.addItem('Female',['Mary','Julia',"Jan",'Miriam'])
        # minute 6 add items to second box
        # click the first DropDown
        self.comboBox.activated.connect(self.clicker)
        self.comboBox_2.activated.connect(self.clicker_2)
        
        self.show()
        
    # def clicker(self,index):
    #     print(f'{index}')
    #     if index ==0:
    #         self.comboBox_2.clear()
    #         self.comboBox_2.addItems(['John', 'Sam','Kevin','Jon'])
    #         ## or
    #         self.comboBox_2.addItems(self.comboBox.itemData)
    #     else:
    #         self.comboBox_2.clear()
    #         self.comboBox_2.addItems(['Mary','Julia',"Jan",'Miriam'])
    def clicker(self,index):
            self.comboBox_2.clear() ## combBox adds theindexed data to combobox–3
            self.comboBox_2.addItems(self.comboBox.itemData(index))
            ## have comboBox2 selection show in label
            
    def clicker_2(self,index):
        print(index)
        self.label.clear()
        # self.label.setText(f'You Picked: {self.comboBox_2.currentText()}')## this also works
        self.label.setText(f'You Picked: {self.comboBox_2.currentText()} - {self.comboBox.currentText()}')## this also works
        # self.label.setText(f'You Picked: {self.comboBox_2.itemText(index)}')## i think because we are pulling from a list
# Initialize the app
app = QApplication(sys.argv)
UIWindow = MainWIndow()
# UIWindow.show()
app.exec_()