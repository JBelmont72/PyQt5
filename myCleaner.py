# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         font = QtGui.QFont()
#         font.setFamily("Comic Sans MS")
#         font.setPointSize(12)
#         MainWindow.setFont(font)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.MyPushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.MyPushButton.setGeometry(QtCore.QRect(69, 311, 321, 141))
#         font = QtGui.QFont()
#         font.setFamily("Comic Sans MS")
#         font.setPointSize(24)
#         font.setItalic(True)
#         self.MyPushButton.setFont(font)
#         self.MyPushButton.setObjectName("MyPushButton")
#         self.myLabel = QtWidgets.QLabel(self.centralwidget)
#         self.myLabel.setGeometry(QtCore.QRect(107, 55, 201, 91))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(9)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.myLabel.sizePolicy().hasHeightForWidth())
#         self.myLabel.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setFamily("Comic Sans MS")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setUnderline(True)
#         self.myLabel.setFont(font)
#         # self.myLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

#         self.myLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.myLabel.setObjectName("myLabel")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.MyPushButton.setText(_translate("MainWindow", "Click Me"))
#         self.myLabel.setText(_translate("MainWindow", "Hello everyone!"))
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
'''
Here's an improved version of the qt_enum_cleaner.py script that:
Recursively walks through a folder and its subfolders.
Cleans enum issues like QtCore.Qt.AlignCenter.
Removes redundant QtCore.Qt.QtCore prefixes.
Automatically adds a test runner block to show the window if it finds a class named Ui_MainWindow (you can easily extend this logic later).


'''
import os
import re
import sys

def clean_pyqt_enums(content):
    # Fix C++-style enums like Qt.AlignCenter
    content = re.sub(r'\bQt::([A-Za-z_]+)', r'QtCore.Qt.\1', content)

    # Remove duplicate Qt prefixes like QtCore.Qt.AlignCenter
    content = re.sub(r'(QtCore\.Qt\.)Qt\.', r'\1', content)
    content = re.sub(r'(QtCore\.Qt\.)QtCore\.', r'\1', content)

    return content

def add_runner_if_main(content):
    if "class Ui_MainWindow" in content and "if __name__ == '__main__':" not in content:
        runner_code = '''
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
        content += runner_code
    return content

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cleaned = clean_pyqt_enums(content)
    cleaned = add_runner_if_main(cleaned)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    print(f"✔ Cleaned: {filepath}")

def clean_directory_recursively(root_folder):
    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.py'):
                full_path = os.path.join(foldername, filename)
                process_file(full_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python qt_enum_cleaner.py <folder_path>")
    else:
        target_folder = sys.argv[1]
        clean_directory_recursively(target_folder)

