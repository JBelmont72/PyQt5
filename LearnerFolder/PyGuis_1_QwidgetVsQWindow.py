'''
https://www.pythonguis.com/tutorials/pyqt-basic-widgets/#qcheckbox

/Users/judsonbelmont/Documents/SharedFolders/Pico/PyQt5/LearnerFolder/PyGuis_1_QwidgetVsQWindow.py
i took the QWindow and converted below to QWidget as the parent widget
 the difference is here:
        self.setLayout(layout)## only needed to setLayout()  when QWidget was parent
        # widget = QWidget()## for using QWindow I needed to create a 'central widget', then put the layout in the central widget, and finally link the central widget to the parent with 'self'
        # widget.setLayout(layout)

        # # Set the central widget of the Window. Widget will expand
        # # to take up all the space in the window by default.
        # self.setCentralWidget(widget)
        
        
'''







# import sys

# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateEdit,
#     QDateTimeEdit,
#     QDial,
#     QDoubleSpinBox,
#     QFontComboBox,
#     QLabel,
#     QLCDNumber,
#     QLineEdit,
#     QMainWindow,
#     QProgressBar,
#     QPushButton,
#     QRadioButton,
#     QSlider,
#     QSpinBox,
#     QTimeEdit,
#     QVBoxLayout,
#     QWidget,
# )

# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets App")

#         layout = QVBoxLayout()
#         widgets = [
#             QCheckBox,
#             QComboBox,
#             QDateEdit,
#             QDateTimeEdit,
#             QDial,
#             QDoubleSpinBox,
#             QFontComboBox,
#             QLCDNumber,
#             QLabel,
#             QLineEdit,
#             QProgressBar,
#             QPushButton,
#             QRadioButton,
#             QSlider,
#             QSpinBox,
#             QTimeEdit,
#         ]

#         for w in widgets:
#             layout.addWidget(w())

#         widget = QWidget()
#         widget.setLayout(layout)

#         # Set the central widget of the Window. Widget will expand
#         # to take up all the space in the window by default.
#         self.setCentralWidget(widget)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
#####
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())
        self.setLayout(layout)
        # widget = QWidget()
        # widget.setLayout(layout)

        # # Set the central widget of the Window. Widget will expand
        # # to take up all the space in the window by default.
        # self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()