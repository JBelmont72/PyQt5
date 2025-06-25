# hello_pyqt5.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello from PyQt5")

layout = QVBoxLayout()

label = QLabel("Press the button below:")
layout.addWidget(label)

button = QPushButton("Say Hello")
layout.addWidget(button)

def on_click():
    label.setText("Hello from PyQt5!")

button.clicked.connect(on_click)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
