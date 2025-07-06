
https://chatgpt.com/c/68602b54-be4c-800f-8a73-95fbaaa16184

When using from PyQt5 import uic to load .ui files, you can absolutely open multiple windows in a PyQt5 application. The uic module lets you dynamically load UI files created in Qt Designer without manually converting them to .py files using pyuic5.

Here’s a simple working example that demonstrates opening a second window from a main window using uic:
🧠 Concept Overview
uic.loadUi() loads a .ui file and applies it to a widget.
You can create multiple windows by creating separate classes or instances for each .ui file.
To show the second window from the first, you keep a reference to it (to prevent it from being garbage collected).
project/
├── main.py
├── main_window.ui
└── second_window.ui

🧩 main_window.ui
Add a QPushButton
Object name: pushButton
Text: Open Second Window
🧩 second_window.ui
Add any widgets you want in your second window.


import sys
from PyQt5 import QtWidgets, uic

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("second_window.ui", self)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)

        # Connect button signal to slot
        self.pushButton.clicked.connect(self.open_second_window)

        self.second_window = None

    def open_second_window(self):
        if self.second_window is None:
            self.second_window = SecondWindow()
        self.second_window.show()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
