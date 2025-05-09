'''used qt_enum_cleaner.py to clean
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
errors:
I only had to make three changes as shown below!!!! and it worked
File "/Users/judsonbelmont/Documents/SharedFolders/Pico/PyQt5/Codemy/MyCalc_1.py", line 31
    self.ResutlLabel.setFrameShape(QtCore.Qt.QFrame::Shape::Box)    
    
 # Use QtWidgets.QFrame instead of QtCore.QFrame
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)  # Corrected line
        self.OutputLabel.setFrameShadow(QtWidgets.QFrame.Raised)  # Corrected line
        self.OutputLabel.setLineWidth(4)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)  # Corrected line
        self.OutputLabel.setObjectName("OutputLabel")
        
        # ... (rest of your button setup code remains unchanged)
        
        
        
        
        
        
        
        
        
        ## correct way to set alignment for QLabels is self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.OutputLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # self.OutputLabel.setFrameShape(QtCore.QFrame.Shape.Box)
        # self.OutputLabel.setFrameShadow(QtCore.QFrame.Shadow.Raised)
        # # self.OutputLabel.setFrameShape(QtCore.QFrame.Shape.Box)
        # # self.OutputLabel.setFrameShape(QtCore.Qt.QFrame::Shape::Box)
        # # self.OutputLabel.setFrameShadow(QtCore.Qt.QFrame::Shadow::Raised)
        # self.OutputLabel.setLineWidth(4)
        # self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)  # Corrected line
        # # self.OutputLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)##error line
        # self.OutputLabel.setObjectName("OutputLabel")    
    
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame  # I added- Import QFrame from QtWidgets recommended

class Ui_MyCalculator(object):
    def setupUi(self, MyCalculator):
        MyCalculator.setObjectName("MyCalculator")
        MyCalculator.resize(523, 642)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        MyCalculator.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MyCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.ResutlLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResutlLabel.setGeometry(QtCore.QRect(20, 20, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.ResutlLabel.setFont(font)
        
# Use QtWidgets.QFrame instead of QtCore.QFrame
        self.ResutlLabel.setFrameShape(QtWidgets.QFrame.Box)  # Corrected line
        self.ResutlLabel.setFrameShadow(QtWidgets.QFrame.Raised)  # Corrected line        
        
        # self.ResutlLabel.setFrameShape(QtCore.Qt.QFrame::Shape::Box)
        # self.ResutlLabel.setFrameShadow(QtCore.Qt.QFrame::Shadow::Raised)
        self.ResutlLabel.setLineWidth(4)
        self.ResutlLabel.setMidLineWidth(2)
        
        self.ResutlLabel.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.ResutlLabel.setAlignment(QtCore.Qt.AlignCenter)  # Corrected line
        # self.ResutlLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ResutlLabel.setObjectName("ResutlLabel")
        
        self.logButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('log'))
        self.logButton.setGeometry(QtCore.QRect(40, 90, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(False)
        self.logButton.setFont(font)
        self.logButton.setObjectName("logButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it('%'))
        self.percentButton.setGeometry(QtCore.QRect(130, 90, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(38)
        font.setBold(True)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it('C'))
        self.cButton.setGeometry(QtCore.QRect(220, 90, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(38)
        font.setBold(True)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it('4'))
        self.pushButton_4.setGeometry(QtCore.QRect(310, 90, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('9'))
        self.nineButton.setGeometry(QtCore.QRect(310, 190, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('8'))
        self.eightButton.setGeometry(QtCore.QRect(220, 190, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(False)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.squareButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it('square'))
        self.squareButton.setGeometry(QtCore.QRect(40, 190, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(30)## change from 38
        font.setBold(True)
        self.squareButton.setFont(font)
        self.squareButton.setObjectName("squareButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('7'))
        self.sevenButton.setGeometry(QtCore.QRect(130, 190, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        
        font.setPointSize(38) ## changed from 38
        font.setBold(False)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('6'))
        self.sixButton.setGeometry(QtCore.QRect(310, 290, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(False)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('5'))
        self.fiveButton.setGeometry(QtCore.QRect(220, 290, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.squareRootButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('squareRoot'))
        self.squareRootButton.setGeometry(QtCore.QRect(40, 290, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(24)
        font.setBold(True)
        self.squareRootButton.setFont(font)
        self.squareRootButton.setObjectName("squareRootButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('4'))
        self.fourButton.setGeometry(QtCore.QRect(130, 290, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('3'))
        self.threeButton.setGeometry(QtCore.QRect(310, 390, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('2'))
        self.twoButton.setGeometry(QtCore.QRect(220, 390, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(False)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.piButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('pi'))
        self.piButton.setGeometry(QtCore.QRect(40, 390, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.piButton.setFont(font)
        self.piButton.setObjectName("piButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('1'))
        self.oneButton.setGeometry(QtCore.QRect(130, 390, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(False)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.PlusMinusButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('+/-'))
        self.PlusMinusButton.setGeometry(QtCore.QRect(130, 490, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.PlusMinusButton.setFont(font)
        self.PlusMinusButton.setObjectName("PlusMinusButton")
        self.sineButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('sin'))
        self.sineButton.setGeometry(QtCore.QRect(40, 490, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.sineButton.setFont(font)
        self.sineButton.setObjectName("sineButton")
        self.pointButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('.'))
        self.pointButton.setGeometry(QtCore.QRect(310, 490, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(50)
        font.setBold(True)
        self.pointButton.setFont(font)
        self.pointButton.setObjectName("pointButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('0'))
        self.zeroButton.setGeometry(QtCore.QRect(220, 490, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('+'))
        self.plusButton.setGeometry(QtCore.QRect(400, 390, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.XButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('x'))
        self.XButton.setGeometry(QtCore.QRect(400, 190, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        self.XButton.setFont(font)
        self.XButton.setObjectName("XButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('/'))
        self.divideButton.setGeometry(QtCore.QRect(400, 90, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(38)
        font.setBold(False)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('='))
        self.equalButton.setGeometry(QtCore.QRect(400, 490, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(42)
        font.setBold(True)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget,clicked =lambda:self.press_it('-'))
        self.minusButton.setGeometry(QtCore.QRect(400, 290, 81, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(42)
        font.setBold(False)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        MyCalculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyCalculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 24))
        self.menubar.setObjectName("menubar")
        MyCalculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyCalculator)
        self.statusbar.setObjectName("statusbar")
        MyCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(MyCalculator)
        QtCore.QMetaObject.connectSlotsByName(MyCalculator)

    def retranslateUi(self, MyCalculator):
        _translate = QtCore.QCoreApplication.translate
        MyCalculator.setWindowTitle(_translate("MyCalculator", "MainWindow"))
        self.ResutlLabel.setText(_translate("MyCalculator", "0"))
        self.logButton.setText(_translate("MyCalculator", "log"))
        self.percentButton.setText(_translate("MyCalculator", "%"))
        self.cButton.setText(_translate("MyCalculator", "C"))
        self.pushButton_4.setText(_translate("MyCalculator", "<<"))
        self.nineButton.setText(_translate("MyCalculator", "9"))
        self.eightButton.setText(_translate("MyCalculator", "8"))
        self.squareButton.setText(_translate("MyCalculator", "x**y"))
        self.sevenButton.setText(_translate("MyCalculator", "7"))
        self.sixButton.setText(_translate("MyCalculator", "6"))
        self.fiveButton.setText(_translate("MyCalculator", "5"))
        self.squareRootButton.setText(_translate("MyCalculator", "SqRt"))
        self.fourButton.setText(_translate("MyCalculator", "4"))
        self.threeButton.setText(_translate("MyCalculator", "3"))
        self.twoButton.setText(_translate("MyCalculator", "2"))
        self.piButton.setText(_translate("MyCalculator", "pi"))
        self.oneButton.setText(_translate("MyCalculator", "1"))
        self.PlusMinusButton.setText(_translate("MyCalculator", "+/-"))
        self.sineButton.setText(_translate("MyCalculator", "sin"))
        self.pointButton.setText(_translate("MyCalculator", "."))
        self.zeroButton.setText(_translate("MyCalculator", "0"))
        self.plusButton.setText(_translate("MyCalculator", "+"))
        self.XButton.setText(_translate("MyCalculator", "X"))
        self.divideButton.setText(_translate("MyCalculator", "/"))
        self.equalButton.setText(_translate("MyCalculator", "="))
        self.minusButton.setText(_translate("MyCalculator", "-"))
    def press_it(self,pressed):       ## WORKS
        # self.ResutlLabel.setText(pressed)
        if pressed == 'C':
            pressed='0'
            self.ResutlLabel.setText(pressed)
        else:
            self.ResutlLabel.setText(pressed)
            ##self.ResutlLabel.setText(f'{self.ResutlLabel.setText(pressed)}')
        
        
    # def press_it(self,pressed):
    #     while True:
    #         if pressed == 'C':
    #             pressed='0'
    #             self.ResutlLabel.setText(pressed)
    #         else:
    #             self.ResutlLabel.setText(pressed)
        # else:    
        #     while True:   
        
        #         pressList=[]
        #         pressList =pressList.append(pressed)
        #         try:
        #             if pressList >1:
        #                 self.ResutlLabel.setText(f'{self.ResutlLabel.setText(pressed)}{pressed}')
                        
        #             else:
        #                 self.ResutlLabel.setText(pressed)
                        
        #         except:
        #             pass    
                
            
            
            
               

        # self.ResutlLabel.setText(f'{self.ResutlLabel.setText(pressed)}{pressed}')
            # self.ResutlLabel.setText(pressed)
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MyCalculator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())