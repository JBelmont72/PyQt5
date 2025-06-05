

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setObjectName("actionModify")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionQuestons = QtWidgets.QAction(MainWindow)
        self.actionQuestons.setObjectName("actionQuestons")
        self.actionHome = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Codemy/../../../../ComputerSetUp/Icons/Icons_iOS/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon)
        # self.actionHome.setMenuRole(QtCore.Qt.QAction::MenuRole::NoRole)## incorrect syntax
        # The above line is incorrect in PyQt5, it should be set like this:
        
        # from PyQt5.QtCore import Qt
        # from PyQt5.QtWidgets import QAction     ##| ✅ `QtWidgets` ⚠️ (extra needed) | It was already added here
        
        # self.actionHome.setMenuRole(Qt.NoRole) ## no `Qt` prefix needed in PyQt5
        # self.actionHome.setMenuRole(QtWidgets.QAction.NoRole) ## correct syntax
        # The above line is correct in PyQt5, it sets the menu role of the action to NoRole.
        self.actionHome.setMenuRole(QtWidgets.QAction.NoRole)

        self.actionHome.setObjectName("actionHome")
        self.menuFile.addAction(self.actionHome)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionModify)
        self.menuEdit.addAction(self.actionDelete)
        self.menuHelp.addAction(self.actionQuestons)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHome)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionModify.setText(_translate("MainWindow", "Modify"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionQuestons.setText(_translate("MainWindow", "Questons"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())