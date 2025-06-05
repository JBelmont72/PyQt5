'''


'''
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = qtw.QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        #widget.setReadOnly(True) # uncomment this to make it read-only

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

        
        
        
if __name__ == '__main__':
    app=qtw.QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())


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
#         self.setGeometry(100, 100, 500, 400)

#         # calling method
#         self.UiComponents()

#         # showing all the widgets
#         self.show()



#     # method for components
#     def UiComponents(self):

#         # creating a QLineEdit object
#         line_edit = QLineEdit("GeeksforGeeks", self)

#         # setting geometry
#         line_edit.setGeometry(80, 80, 150, 40)

#         # creating a label
#         label = QLabel("GfG", self)

#         # setting geometry to the label
#         label.setGeometry(80, 150, 120, 60)

#         # setting word wrap property of label
#         label.setWordWrap(True)

#         # adding action to the line edit when enter key is pressed
#         line_edit.returnPressed.connect(lambda: do_action())

#         # method to do action
#         def do_action():

#             # getting text from the line edit
#             value = line_edit.text()

#             # setting text to the label
#             label.setText(value)




# # create pyqt5 app
# App = QApplication(sys.argv)

# # create the instance of our Window
# window = Window()

# # start the app
# sys.exit(App.exec())

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

#         # creating a combo box widget
#         self.combo_box = QComboBox(self)

#         # setting geometry of combo box
#         self.combo_box.setGeometry(200, 150, 150, 30)

#         # making combo box editable
#         self.combo_box.setEditable(True)

#         # geek list
#         geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]

#         # adding list of items to combo box
#         self.combo_box.addItems(geek_list)

#         # creating line edit widget
#         line_edit = QLineEdit()

#         # setting background color to the line edit widget
#         line_edit.setStyleSheet("QLineEdit"
#                                 "{"
#                                 "background : lightblue;"
#                                 "}")


#         # adding line edit widget to combo box
#         self.combo_box.setLineEdit(line_edit)


# # create pyqt5 app
# App = QApplication(sys.argv)

# # create the instance of our Window
# window = Window()

# # start the app
# sys.exit(App.exec())