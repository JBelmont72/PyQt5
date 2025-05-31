'''
https://www.pythontutorial.net/pyqt/pyqt-qlineedit/

'''
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBoxLayout')

#         # create a layout
#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         # create buttons
#         label_1 = QLabel()
#         # label_1.setStyleSheet('QLabel{background-color:red}')
#         label_1.setStyleSheet('background-color:red;')
#         label_2 = QLabel()
#         label_2.setStyleSheet('QLabel{background-color:green}')
#         label_3 = QLabel()
#         label_3.setStyleSheet('QLabel{background-color:blue}')

#         layout.addWidget(label_1)
#         layout.addWidget(label_2)
#         layout.addWidget(label_3)

#         # show the window
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())
#########~~~~
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         self.setWindowTitle('my Labels and LineEdits')
#         self.setGeometry(10,10,600,400)
#         layout=qtw.QVBoxLayout()
#         self.setLayout(layout)
#         colors = ['red', 'blue', 'yellow']
#         labels = ['new', 'recent', 'edit']
        
#         for label_text, color in zip(labels, colors):
#             label = qtw.QLabel(label_text)
#             label.setStyleSheet(f'background-color: {color};')
#             label.setFixedSize(100, 50)  # Set width to 100 and height to 50
#             layout.addWidget(label)
        

        
        
#         self.show()
        
# if __name__ == '__main__':
#     app =qtw.QApplication(sys.argv)
#     window =MainWindow()
#     window.show()
#     sys.exit(app.exec_())
    
    
######~~~~~~~
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         self.setWindowTitle('my Labels and LineEdits')
#         self.setGeometry(10,10,600,400)
#         layout=qtw.QVBoxLayout()
#         self.setLayout(layout)
        
#         h_layout =qtw.QHBoxLayout()
#         v1_layout=qtw.QVBoxLayout() # this wil contain the labels
#         v2_layout=qtw.QVBoxLayout() # this wii contain the lineEdits
#         layout.addLayout(h_layout)
#         h_layout.addLayout(v1_layout)
#         h_layout.addLayout(v2_layout)
        
        
        
        
#         colors = ['red', 'blue', 'yellow']
#         labels = ['new', 'recent', 'edit']
        
#         for label_text, color in zip(labels, colors):
#             label = qtw.QLabel(label_text)
#             label.setStyleSheet(f'background-color: {color};')
#             label.setFixedSize(100, 50)  # Set width to 100 and height to 50
#             v1_layout.addWidget(label)
        
#         ## create three lineEdits
#         lineEntries = ['enter your choice', 'enter prior choice', 'remove']
#         for placeholder_text in lineEntries:
#             line_edit = qtw.QLineEdit()
#             line_edit.setPlaceholderText(placeholder_text)
#             line_edit.setFixedSize(100, 50)  # Set width to 100 and height to 50
#             v2_layout.addWidget(line_edit)
            
  
#         # lineEdit=qtw.QLineEdit
        
        
#         self.show()
        
# if __name__ == '__main__':
#     app =qtw.QApplication(sys.argv)
#     window =MainWindow()
#     window.show()
#     sys.exit(app.exec_())
######~~~~~~  https://www.pythontutorial.net/pyqt/pyqt-qcheckbox/
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox,  QGridLayout
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100, 100, 320, 210)

        # create a grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        # create a tristate checkbox
        self.checkbox = QCheckBox('A Tristate Checkbox', self)
        # self.checkbox=QCheckBox('A Tristate Checkbox') ## this way does not establish the parent child relatioship
        self.checkbox.setTristate(True)
## with the parent child relationship established. I do not need to add the widget but this hel[ed the positonin and ATTRIBUTES]
        layout.addWidget(self.checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())