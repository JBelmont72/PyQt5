
### RadioButton program in Codemy Cod_18_RadioButton
#### link
* https://stackoverflow.com/questions/13050810/pyqt-button-clicked-name
``` py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QLabel, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.button_layout = QHBoxLayout()
        self.widget_layout = QVBoxLayout()

        for button_number in range(1, 11):## function creates 10 buttons and adds them to the button_layout
            button = QToolButton()
            button.setText(str(button_number))
            button.setObjectName('Button%d' % button_number)
            button.released.connect(self.button_released)
            self.button_layout.addWidget(button)

        self.status_label = QLabel('No button clicked')
        self.widget_layout.addLayout(self.button_layout)# this works also because adds a layout
        # self.widget_layout.addItem(self.button_layout) 
        # self.widget_layout.addLayout(self.status_label)# cannot use this since label is not a layout
        self.widget_layout.addWidget(self.status_label)
        # self.widget_layout.addItem(self.status_label)## not work
        self.setLayout(self.widget_layout)

    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))




if __name__ == '__main__':
  app = QApplication(sys.argv)

  widget = Widget()
  widget.show()

  sys.exit(app.exec_())
  ```