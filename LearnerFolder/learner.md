### my attempt at creating multiople labels and checkBoxes and then using a lambda function as in CHAT to send state and checkbox to the def function
###  /Users/judsonbelmont/Documents/SharedFolders/Pico/PyQt5/LearnerFolder/Py_Tut_3A_CheckBox.py
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys

class SkillsForm(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test My Skills")
        self.setGeometry(10,10,400,600)
        ## create layout
        layout = qtw.QHBoxLayout()
        self.setLayout(layout)
        # create two vertical layouts, the first for labels and the second for checkboxes
        Label_layout=qtw.QVBoxLayout()
        CheckBox_layout =qtw.QVBoxLayout()
        layout.addLayout(Label_layout)
        layout.addLayout(CheckBox_layout)
        ## populate the two sub-layouts, list comprehension
        labels=['first','second','third','fourth','fifth']
        Labels=[qtw.QLabel(label,self)for label in labels]## this created the labels on top of each other
        for myLabel in Labels:
            Label_layout.addWidget(myLabel)
            
        CheckBoxNames = ['check_1', 'check_2', 'check_3', 'check_4', 'check_5']
        CheckBoxes = [qtw.QCheckBox(name) for name in CheckBoxNames]
        for box in CheckBoxes:
            CheckBox_layout.addWidget(box)
        # Ensure labels and checkboxes align properly
        for label, checkbox in zip(Labels, CheckBoxes):
            checkbox.stateChanged.connect(
                lambda state, lbl=label, cb=checkbox: self.update_label(lbl, cb, state)
        )

    def update_label(self, label, checkbox, state):
        if state == qtc.Qt.Checked:
            label.setText(f'{checkbox.text()} is Checked')
        elif state == qtc.Qt.Unchecked:
            label.setText(f'{checkbox.text()} is Unchecked')
        elif state == qtc.Qt.PartiallyChecked:
            label.setText(f'{checkbox.text()} is Partially Checked')
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    form = SkillsForm()
    form.show()
    sys.exit(app.exec_())
