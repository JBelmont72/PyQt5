'''
M_5_moving_data.py
the main window is first. the qtw.QLabel s are establiehed with the first strings.

'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class DialogWindow(qtw.QWidget):

    submitted = qtc.pyqtSignal(str, str) ## this creates a SIGNAL sending two strings, submitted with be a method
                                ## WITHOUT THIS SIGNAL error: AttributeError: 'DialogWindow' object has no attribute 'submitted'
    def __init__(self,message_a,message_b): ## i had two options.  I chose to pass the messages or could have sent them stright to the set_messages method
        super().__init__()
        self.resize(640, 480)
        self.message_a_edit = qtw.QLineEdit()
        self.message_b_edit = qtw.QLineEdit()
        
        self.message_a_edit.setText(message_a)
        self.message_b_edit.setText(message_b)
        
        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Submit')
        self.setLayout(qtw.QFormLayout())
        self.layout().addRow('Message A', self.message_a_edit)
        self.layout().addRow('Message B', self.message_b_edit)
        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QHBoxLayout())
        buttons.layout().addWidget(self.cancel_button)
        buttons.layout().addWidget(self.submit_button)
        self.layout().addRow('', buttons)

        self.submit_button.clicked.connect(self.on_submit)## this is the signal created above.
        self.cancel_button.clicked.connect(self.close)

    def set_messages(self, message_a, message_b): ## this is called in the Mainwindow when the Dialog window is going to be shown.

        self.message_a_edit.setText(message_a)
        self.message_b_edit.setText(message_b)

    def on_submit(self):
        self.submitted.emit(
            self.message_a_edit.text(), ## updates the message_a and message_b
            self.message_b_edit.text()
            )
        self.close()    ## closes so the MainWindow now shows the updated messages

class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()
        self.resize(640, 480)
        # Main UI code goes here
        self.message_a = 'Hello'
        self.message_b = 'Is it me you\'re looking for?'

        self.message_a_display = qtw.QLabel(
            text=self.message_a,
            font=qtg.QFont('Sans', 20)
            )
        
        self.message_b_display = qtw.QLabel(
            text=self.message_b,
            font=qtg.QFont('Sans', 20)
            )
        self.edit_button=qtw.QPushButton('Press Me Now!!!',clicked = self.edit_messages)
        # self.edit_button = qtw.QPushButton(
        #     'Edit',
        #     clicked=self.edit_messages ## edit_messages is an instance method
        #     ) ## the 'Edit ' is in the button

        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(self.message_a_display)
        self.layout().addWidget(self.message_b_display)
        self.layout().addWidget(self.edit_button)

        # End main UI code
        self.show()

    @qtc.pyqtSlot(str, str) ## an optional step
    def update_messages(self, message_a, message_b):
        self.message_a = message_a
        self.message_b = message_b
        self.message_a_display.setText(self.message_a)## these is updating the labels above.otherwise they stay the original meassag_a, and _b from the onset!!
        self.message_b_display.setText(self.message_b)

        ## i can either use the dialog.set_messages( ) method below or just pass the two messages directly. both worked fine
    def edit_messages(self): ## not using this since I decided to pass the messages driectly to the Dialog class.
        self.dialog = DialogWindow(self.message_a,self.message_b)
        # self.dialog.set_messages(self.message_a, self.message_b)## this passes the new messages to def set_messages() in Dialog window
        self.dialog.submitted.connect(self.update_messages)## the slot is the update_messages method
        self.dialog.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())