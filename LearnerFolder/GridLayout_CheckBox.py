'''




https://www.pythontutorial.net/pyqt/pyqt-qcheckbox/'''

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
# from PyQt5.QtCore import Qt


# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QCheckBox')
#         self.setGeometry(100, 100, 320, 210)

#         # create a grid layout
#         layout = QGridLayout()
#         self.setLayout(layout)

#         # create a checkbox
#         checkbox = QCheckBox('I agree', self)

#         layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)

#         # show the window
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())
    
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100, 100, 320, 210)

        # create a grid layout
        layout = qtw.QGridLayout()
        self.setLayout(layout)

        # create a checkbox
        checkbox = qtw.QCheckBox('I agree', self)

        layout.addWidget(checkbox, 0, 0, qtc.Al)

        # show the window
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    