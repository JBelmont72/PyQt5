'''ChatGPT
 Here's a clean mini-example that builds on your current setup. It shows three QCheckBoxes, each controlling a different label. You’ll see how to:

Connect each checkbox to the same function
Use lambda or functools.partial to pass the checkbox to that function
Avoid .sender() entirely
Reinforce how signal arguments are handled


first uses functools and second lambda
'''
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# import sys
# from functools import partial

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Multiple CheckBoxes')
#         self.setGeometry(100, 100, 400, 300)

#         layout = qtw.QVBoxLayout()
#         self.setLayout(layout)

#         # Create three labels and three checkboxes
#         self.labels = []
#         self.checkboxes = []

#         for i in range(3):
#             label = qtw.QLabel(f'Label {i+1} — initial')
#             checkbox = qtw.QCheckBox(f'CheckBox {i+1}', self)
#             checkbox.setTristate()
#             checkbox.setCheckState(qtc.Qt.Unchecked)

#             # Add to layout and store
#             layout.addWidget(checkbox)
#             layout.addWidget(label)
#             self.checkboxes.append(checkbox)
#             self.labels.append(label)

#             # Connect checkbox to handler with functools.partial
#             checkbox.stateChanged.connect(partial(self.update_label, checkbox, label))

#         layout.addStretch()

#     def update_label(self, checkbox, label, state):
#         if state == qtc.Qt.Checked:
#             label.setText(f'{checkbox.text()} is Checked')
#         elif state == qtc.Qt.Unchecked:
#             label.setText(f'{checkbox.text()} is Unchecked')
#         elif state == qtc.Qt.PartiallyChecked:
#             label.setText(f'{checkbox.text()} is Partially Checked')
#         print(f'{checkbox.text()} → state: {state}, isChecked(): {checkbox.isChecked()}')

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

### using lambda instead of functools
'''
lambda state, cb=checkbox, lbl=label: self.update_label(cb, lbl, state)
Why this works:

state comes from the stateChanged signal
cb=checkbox and lbl=label are captured at the time the lambda is created
This ensures each lambda "remembers" which checkbox and label it belongs to
If you don’t use the default argument trick, all the lambdas would end up pointing to the last checkbox and label in the loop — a common mistake!


in this example   as written, self.checkboxes and self.labels are not used afterward, so those .append() calls could be removed without breaking anything.

But in real-world applications, storing widgets in lists (or dicts) becomes extremely useful when you want to:

Iterate over them
Update them all at once
Read multiple states at once
Build forms or GUIs dynamically
Save or export settings



'''

# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# import sys

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Multiple CheckBoxes with lambda')
#         self.setGeometry(100, 100, 400, 300)

#         layout = qtw.QVBoxLayout()
#         self.setLayout(layout)

#         self.labels = []
#         self.checkboxes = []

#         for i in range(3):
#             label = qtw.QLabel(f'Label {i+1} — initial')
#             checkbox = qtw.QCheckBox(f'CheckBox {i+1}', self)
#             checkbox.setTristate()
#             checkbox.setCheckState(qtc.Qt.Unchecked)

#             layout.addWidget(checkbox)
#             layout.addWidget(label)

#             self.checkboxes.append(checkbox)
#             self.labels.append(label)

#             # Use lambda to pass checkbox and label to the handler
#             checkbox.stateChanged.connect(
#                 lambda state, cb=checkbox, lbl=label: self.update_label(cb, lbl, state)
#             )

#         layout.addStretch()

#     def update_label(self, checkbox, label, state):
#         if state == qtc.Qt.Checked:
#             label.setText(f'{checkbox.text()} is Checked')
#         elif state == qtc.Qt.Unchecked:
#             label.setText(f'{checkbox.text()} is Unchecked')
#         elif state == qtc.Qt.PartiallyChecked:
#             label.setText(f'{checkbox.text()} is Partially Checked')
#         print(f'{checkbox.text()} → state: {state}, isChecked(): {checkbox.isChecked()}')

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
##Let’s say you're creating a form where the user can select multiple "skills" using checkboxes. Later, you want to submit or display which checkboxes were selected.

##Here’s how you'd use the list of checkboxes:
# from PyQt5 import QtWidgets as qtw
# import sys

# class SkillsForm(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Select Your Skills")
#         layout = qtw.QVBoxLayout()
#         self.setLayout(layout)

#         self.skills = ["Python", "MicroPython", "PyQt5", "OpenCV", "MQTT"]
#         self.checkboxes = []

#         for skill in self.skills:
#             checkbox = qtw.QCheckBox(skill)
#             layout.addWidget(checkbox)
#             self.checkboxes.append(checkbox)

#         submit_btn = qtw.QPushButton("Submit")
#         submit_btn.clicked.connect(self.show_selected_skills)
#         layout.addWidget(submit_btn)

#     def show_selected_skills(self):
#         selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
#         msg = "You selected:\n" + "\n".join(selected) if selected else "No skills selected."
#         qtw.QMessageBox.information(self, "Selected Skills", msg)

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     form = SkillsForm()
#     form.show()
#     sys.exit(app.exec_())

## What This Teaches You
# The list self.checkboxes is crucial because you don’t want to hard-code each checkbox in show_selected_skills().
# If the skill list grows or changes, the code still works — very scalable and maintainable.
# The pattern [cb.text() for cb in self.checkboxes if cb.isChecked()] gives you all the checked ones at once.
## could use this to reset the form and erase the list:
# def reset_checkboxes(self):
#     for cb in self.checkboxes:
#         cb.setCheckState(qtc.Qt.Unchecked)


##here's a clear example where checkboxes are used to enable or disable other widgets (like sliders and text inputs). This shows how checkbox state dynamically controls interactivity of other widgets — a common real-world pattern in forms, control panels, and PyQt5 dashboards.
#Example: Checkboxes Enable/Disable Other Widgets
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# import sys

# class ControlPanel(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Enable/Disable Controls with Checkboxes")
#         self.setGeometry(100, 100, 400, 250)
#         layout = qtw.QVBoxLayout()
#         self.setLayout(layout)

#         # We'll create three pairs of checkbox + control widget (QLineEdit, QSlider, QPushButton)
#         self.controls = []

#         # 1. Enable/Disable a QLineEdit
#         cb1 = qtw.QCheckBox("Enable text input")
#         input_field = qtw.QLineEdit()
#         input_field.setPlaceholderText("Type something...")
#         input_field.setEnabled(False)
#         cb1.stateChanged.connect(lambda state, w=input_field: w.setEnabled(state == qtc.Qt.Checked))

#         # 2. Enable/Disable a QSlider
#         cb2 = qtw.QCheckBox("Enable slider")
#         slider = qtw.QSlider(qtc.Qt.Horizontal)
#         slider.setRange(0, 100)
#         slider.setEnabled(False)
#         cb2.stateChanged.connect(lambda state, w=slider: w.setEnabled(state == qtc.Qt.Checked))

#         # 3. Enable/Disable a QPushButton
#         cb3 = qtw.QCheckBox("Enable button")
#         btn = qtw.QPushButton("Click Me!")
#         btn.setEnabled(False)
#         cb3.stateChanged.connect(lambda state, w=btn: w.setEnabled(state == qtc.Qt.Checked))

#         # Add widgets to layout and control list
#         for cb, control in [(cb1, input_field), (cb2, slider), (cb3, btn)]:
#             layout.addWidget(cb)
#             layout.addWidget(control)
#             self.controls.append((cb, control))  # ← for later use if needed (reset, iterate, etc.)

#         layout.addStretch()

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     window = ControlPanel()
#     window.show()
#     sys.exit(app.exec_())
##What You Learned
# Each checkbox toggles .setEnabled(True/False) on a matching widget
# We use lambda state, w=widget: w.setEnabled(state == qtc.Qt.Checked) to control which widget is enabled
# self.controls holds the pairs for easy reset, iteration, or saving state later
# 🔄 Bonus: Add a "Reset All" Button
# You could add this to the end of __init__:

# reset_btn = qtw.QPushButton("Reset All")
# reset_btn.clicked.connect(self.reset_all)
# layout.addWidget(reset_btn)

## and the accompanying definition:
# def reset_all(self):
#     for cb, widget in self.controls:
#         cb.setChecked(False)
#         widget.setEnabled(False)


# Would you like a next step where each checkbox enables a section of a form (like in preferences/settings dialogs)? Or something physical — like enabling a button that sends a command to a servo only when the checkbox is active?


### my attempt at creating multiople labels and checkBoxes and then using a lambda function as in CHAT to send state and checkbox to the def function
###  /Users/judsonbelmont/Documents/SharedFolders/Pico/PyQt5/LearnerFolder/Py_Tut_3A_CheckBox.py
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# import sys

# class SkillsForm(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Test My Skills")
#         self.setGeometry(10,10,400,600)
#         ## create layout
#         layout = qtw.QHBoxLayout()
#         self.setLayout(layout)
#         # create two vertical layouts, the first for labels and the second for checkboxes
#         Label_layout=qtw.QVBoxLayout()
#         CheckBox_layout =qtw.QVBoxLayout()
#         layout.addLayout(Label_layout)
#         layout.addLayout(CheckBox_layout)
#         ## populate the two sub-layouts, list comprehension
#         labels=['first','second','third','fourth','fifth']
#         Labels=[qtw.QLabel(label,self)for label in labels]## this created the labels on top of each other
#         for myLabel in Labels:
#             Label_layout.addWidget(myLabel)
            
#         CheckBoxNames = ['check_1', 'check_2', 'check_3', 'check_4', 'check_5']
#         CheckBoxes = [qtw.QCheckBox(name) for name in CheckBoxNames]
#         for box in CheckBoxes:
#             box.setTristate()
#             CheckBox_layout.addWidget(box)
#         # Ensure labels and checkboxes align properly
#         for label, checkbox in zip(Labels, CheckBoxes):
#             checkbox.stateChanged.connect(
#                 lambda state, lbl=label, cb=checkbox: self.update_label(lbl, cb, state)
#         )

#     def update_label(self, label, checkbox, state):
#         if state == qtc.Qt.Checked:
#             label.setText(f'{checkbox.text()} is Checked')
#             print(checkbox.text(),checkbox.isChecked())
#         elif state == qtc.Qt.Unchecked:
#             label.setText(f'{checkbox.text()} is Unchecked')
#             print(f'Checkbox that is checked: {checkbox.text()} , bool value: {checkbox.isChecked()}')
#         elif state == qtc.Qt.PartiallyChecked:
#             label.setText(f'{checkbox.text()} is Partially Checked')
# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     form = SkillsForm()
#     form.show()
#     sys.exit(app.exec_())


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox(self)
        widget.setCheckState(Qt.Unchecked)## sets it for 0,1,0r 2

        widget.stateChanged.connect(self.show_state)
        widget.stateChanged.connect(lambda state: self.show_state(state))
        

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(isinstance(Qt.Checked, int))  # Check if Qt.Checked is an integer
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

