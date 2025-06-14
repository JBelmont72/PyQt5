


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(467, 279)
        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 361, 61))
        self.label.setObjectName("label")
        ThirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 37))
        self.menubar.setObjectName("menubar")
        ThirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "MainWindow"))
        self.label.setText(_translate("ThirdWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; vertical-align:super;\">  Third WIndow Opened. Hurray!!</span></p></body></html>"))
