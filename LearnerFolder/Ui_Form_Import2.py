from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.username_edit = QtWidgets.QLineEdit(Form)
        self.username_edit.setGeometry(QtCore.QRect(130, 50, 140, 25))
        self.username_edit.setObjectName("username_edit")

        self.password_edit = QtWidgets.QLineEdit(Form)
        self.password_edit.setGeometry(QtCore.QRect(130, 90, 140, 25))
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")

        self.submit_button = QtWidgets.QPushButton(Form)
        self.submit_button.setGeometry(QtCore.QRect(130, 130, 140, 30))
        self.submit_button.setObjectName("submit_button")

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(130, 180, 140, 20))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Form"))
        self.submit_button.setText(_translate("Form", "Login"))
        self.checkBox.setText(_translate("Form", "Remember Me"))
