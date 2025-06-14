


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(380, 370)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(18)
        SecondWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 60, 226, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 37))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.label.setText(_translate("SecondWindow", "Second WIndow  Opened"))
        self.pushButton.setText(_translate("SecondWindow", "Open Window #3"))
