
''' 1. one way to run the .ui file is to run pyuic5 and then add the if __name__== '__main__":
    2. second way in the tutorial is import the .ui file and use the ui functtion to convert it
    /Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Alan_D_Moore/M_4_Signals_Slots/myLogin.py
    '''



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.setEnabled(True)
        LoginForm.resize(352, 387)
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(59, 230, 251, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.loginButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.username_lineEdit = QtWidgets.QLineEdit(LoginForm)
        self.username_lineEdit.setGeometry(QtCore.QRect(170, 100, 113, 21))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_line_edit = QtWidgets.QLineEdit(LoginForm)
        self.password_line_edit.setGeometry(QtCore.QRect(170, 160, 113, 21))
        self.password_line_edit.setObjectName("password_line_edit")
        self.username_label = QtWidgets.QLabel(LoginForm)
        self.username_label.setGeometry(QtCore.QRect(70, 100, 58, 16))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(LoginForm)
        self.password_label.setGeometry(QtCore.QRect(70, 160, 58, 16))
        self.password_label.setObjectName("password_label")
        self.checkBox = QtWidgets.QCheckBox(LoginForm)
        self.checkBox.setGeometry(QtCore.QRect(130, 190, 85, 20))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.cancelButton.setText(_translate("LoginForm", "cancel"))
        self.loginButton.setText(_translate("LoginForm", "login"))
        self.username_label.setText(_translate("LoginForm", "username"))
        self.password_label.setText(_translate("LoginForm", "password"))
        self.checkBox.setText(_translate("LoginForm", "legalese"))
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
