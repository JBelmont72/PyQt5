'''
In PyQt5, the setEnabled() method is used to enable or disable a QWidget or QAction. This method takes a boolean argument: True to enable the item and False to disable it.
In this example:
A QPushButton named button is created.
Two other buttons, disable_button and enable_button, are used to control the enabled state of button.
When disable_button is clicked, self.button.setEnabled(False) is called, which greys out the button and prevents user interaction.
When enable_button is clicked, self.button.setEnabled(True) is called, which restores the button to its active state.
This method can be applied to various PyQt5 widgets and actions, such as QLineEdit, QCalendarWidget, QSpinBox, and QAction, to control user interaction with the application's elements.
'''
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enabled/Disabled Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button = QPushButton("Click Me")
        layout.addWidget(self.button)

        self.disable_button = QPushButton("Disable Button")
        self.disable_button.clicked.connect(self.disable_my_button)
        layout.addWidget(self.disable_button)

        self.enable_button = QPushButton("Enable Button")
        self.enable_button.clicked.connect(self.enable_my_button)
        layout.addWidget(self.enable_button)

        self.setLayout(layout)

    def disable_my_button(self):
        self.button.setEnabled(False)  # Disables the 'Click Me' button

    def enable_my_button(self):
        self.button.setEnabled(True)   # Enables the 'Click Me' button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
