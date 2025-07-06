# '''
# tic tack toe game. lesson 31
# /Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_30_TicTackToe/ticTackToe.py

# '''
# from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QFileDialog
# import sys
# from PyQt5.QtGui import QPixmap
# from PyQt5 import uic
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_31_TicTackToe/ticTackToe.ui',self)
#         self.but1=self.findChild(QPushButton,'pushButton')
#         self.but2=self.findChild(QPushButton,'pushButton_2')
#         self.but3=self.findChild(QPushButton,'pushButton_3')
#         self.but4=self.findChild(QPushButton,'pushButton_4')
#         self.but5=self.findChild(QPushButton,'pushButton_5')
#         self.but6=self.findChild(QPushButton,'pushButton_6')
#         self.but7=self.findChild(QPushButton,'pushButton_7')
#         self.but8=self.findChild(QPushButton,'pushButton_8')
#         self.but9=self.findChild(QPushButton,'pushButton_9')
#         self.label=self.findChild(QLabel,'label')
#         self.start=self.findChild(QPushButton,'Start')
#         # click button
#         self.counter =0
#         self.but1.clicked.connect(lambda: self.clicker(self.but1))
#         self.but2.clicked.connect(lambda: self.clicker(self.but2))
#         self.but3.clicked.connect(lambda: self.clicker(self.but3))
#         self.but4.clicked.connect(lambda: self.clicker(self.but4))
#         self.but5.clicked.connect(lambda: self.clicker(self.but5))
#         self.but6.clicked.connect(lambda: self.clicker(self.but6))
#         self.but7.clicked.connect(lambda: self.clicker(self.but7))
#         self.but8.clicked.connect(lambda: self.clicker(self.but8))
#         self.but9.clicked.connect(lambda: self.clicker(self.but9))
#         self.start.clicked.connect(lambda:self.reset())
        
#     def clicker(self,b): ## b is the self.but1 etc
#         if self.counter %2 ==0:
#             mark='X'
#             self.label.setText("0's turn")
#             b.setStyleSheet("background-color: lightblue; color: navy; font-size: 38px;")
#         else:
#             mark='O'
#             self.label.setText("X's turn")
#             b.setStyleSheet("background-color: yellow; color: red; font-size: 38px;")
        
        
        
#         b.setText(mark) # when started just used b.setText('X') and then setEnabled(False)
#         b.setEnabled(False)
#         self.counter +=1
#     def reset(self):
#         self.counter=0
#         self.label.setText('')
#         self.label.setText('start')
#         button_list =[]
#         button_list = [getattr(self, f'but{i}') for i in range(1, 10)]
#         # for b in button_list:
#         #     print(b)
#         for b in button_list:
#             b.setText('')
#             b.setEnabled(True)
#         self.label.setText('Start Again')
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     w= MainWindow()
#     w.show()
#     sys.exit(app.exec_())
###########
'''
tic tack toe game. lesson 32 follow on with checking who wins
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_30_TicTackToe/ticTackToe.py

'''
# from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QFileDialog
# import sys
# from PyQt5.QtGui import QPixmap
# from PyQt5 import uic
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_31_TicTackToe/ticTackToe.ui',self)
#         self.but1=self.findChild(QPushButton,'pushButton')
#         self.but2=self.findChild(QPushButton,'pushButton_2')
#         self.but3=self.findChild(QPushButton,'pushButton_3')
#         self.but4=self.findChild(QPushButton,'pushButton_4')
#         self.but5=self.findChild(QPushButton,'pushButton_5')
#         self.but6=self.findChild(QPushButton,'pushButton_6')
#         self.but7=self.findChild(QPushButton,'pushButton_7')
#         self.but8=self.findChild(QPushButton,'pushButton_8')
#         self.but9=self.findChild(QPushButton,'pushButton_9')
#         self.label=self.findChild(QLabel,'label')
#         self.start=self.findChild(QPushButton,'Start')
#         # click button
#         self.counter =0
#         # button_list = [getattr(self, f'but{i}') for i in range(1, 10)]
#         # for but in button_list:
#         #     but.clicked.connect(lambda checked, b=but: self.clicker(b))

#         self.but1.clicked.connect(lambda: self.clicker(self.but1))
#         self.but2.clicked.connect(lambda: self.clicker(self.but2))
#         self.but3.clicked.connect(lambda: self.clicker(self.but3))
#         self.but4.clicked.connect(lambda: self.clicker(self.but4))
#         self.but5.clicked.connect(lambda: self.clicker(self.but5))
#         self.but6.clicked.connect(lambda: self.clicker(self.but6))
#         self.but7.clicked.connect(lambda: self.clicker(self.but7))
#         self.but8.clicked.connect(lambda: self.clicker(self.but8))
#         self.but9.clicked.connect(lambda: self.clicker(self.but9))
#         self.start.clicked.connect(lambda:self.reset())
#     def checkwin(self):
#         #if but1,but4,but7 ==x or equal 0. its a win ACROSS
#         # if self.but1.text() !=" " and self.but1.text()== self.but4.text() and self.but1.text() == self.but7.text():
#         #     print('WIn')
#         #     if self.but1.text()=='X':
#         #         print('x wins')
#         #         self.label.setText('X WINS!')
#         if self.but1.text() !=" " and self.but1.text()== self.but4.text() and self.but1.text() == self.but7.text():
#             print('WIn')
#             self.win(self.but1,self.but4,self.but7)
             
        # #if but1,but2,but3 ==x or equal 0. its a win
        # if self.but1.text() !=" " and self.but1.text()== self.but2.text() and self.but1.text() == self.but3.text():
        #     print('WIn1')
        #     self.win(self.but1,self.but2,self.but3)
        
        # #if but4,but5,but6 ==x or equal 0. its a win
        # if self.but4.text() !=" " and self.but4.text()== self.but5.text() and self.but4.text() == self.but6.text():
        #     print('WIn2')
        #     self.win(self.but4,self.but5,self.but6)
        
        # #if but7,but8,but9 ==x or equal 0. its a win
        # if self.but7.text() !=" " and self.but7.text()== self.but8.text() and self.but7.text() == self.but9.text():
        #     print('WIn3')
        #     self.win(self.but7,self.but8,self.but9)
        # #if but2,but5,but8 ==x or equal 0. its a win
        # if self.but2.text() !=" " and self.but2.text()== self.but5.text() and self.but2.text() == self.but8.text():
        #     print('WIn4')
        #     self.win(self.but2,self.but5,self.but8)
        # #if but3,but6,but8 ==x or equal 0. its a win
        # if self.but3.text() !=" " and self.but3.text()== self.but6.text() and self.but3.text() == self.but8.text():
        #     print('WIn5')
        #     self.win(self.but3,self.but6,self.but8)
        # #if but1,but5,but9 ==x or equal 0. its a win
        # if self.but1.text() !=" " and self.but1.text()== self.but5.text() and self.but1.text() == self.but9.text():
        #     print('Win6')
        #     self.win(self.but1,self.but5,self.but9)
        # #if but7,but5,but3 ==x or equal 0. its a win
        # if self.but7.text() !=" " and self.but7.text()== self.but5.text() and self.but7.text() == self.but3.text():
        #     print('WIn7')
        #     self.win(self.but7,self.but5,self.but3)
#     def win(self,a,b,c):
#         self.label.setText(f'{a.text()} WINS!')
            
#     def clicker(self,b): ## b is the self.but1 etc
#         if self.counter %2 ==0:
#             mark='X'
#             self.label.setText("0's turn")
#             b.setStyleSheet("background-color: lightblue; color: navy; font-size: 38px;")
#         else:
#             mark='O'
#             self.label.setText("X's turn")
#             b.setStyleSheet("background-color: yellow; color: red; font-size: 38px;")
        
        
        
#         b.setText(mark) # when started just used b.setText('X') and then setEnabled(False)
#         b.setEnabled(False)
#         self.counter +=1
        
#         ## ADDED when the def clicker is called, the def checkwin will be called
#         self.checkwin()
        
#     def reset(self):
#         self.counter=0
#         self.label.setText('')
#         self.label.setText('start')
#         button_list =[]
#         button_list = [getattr(self, f'but{i}') for i in range(1, 10)]
        
#         # for b in button_list:
#         #     print(b)
#         for b in button_list:
#             b.setStyleSheet('background-color:beige;')
#             b.setText('')
#             b.setEnabled(True)
#         self.label.setText('Start Again')
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     w= MainWindow()
#     w.show()
#     sys.exit(app.exec_())

# I have a tic tac toe game made with QtDesigner created .ui 
# I have double checked which pushbuttons correspond with the rows and columns.complex

# The middle horizontal row is pushbutton 2,5 and 8.  When these all three of these squares/ buttons are selected
# the def win(sdelf) function is called. THis happens even if the third sqare in this row is clicked by a non corresponding x or 0.
# Can you see why this one row should not function properly.  As I said, I know the buttons are correct and refer to the correct block.

#     <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>MainWindow</class>
#  <widget class="QMainWindow" name="MainWindow">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>640</width>
#     <height>648</height>
#    </rect>
#   </property>
#   <property name="windowTitle">
#    <string>MainWindow</string>
#   </property>
#   <widget class="QWidget" name="centralwidget">
#    <widget class="QWidget" name="gridLayoutWidget">
#     <property name="geometry">
#      <rect>
#       <x>10</x>
#       <y>10</y>
#       <width>601</width>
#       <height>364</height>
#      </rect>
#     </property>
#     <property name="sizePolicy">
#      <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
#       <horstretch>100</horstretch>
#       <verstretch>100</verstretch>
#      </sizepolicy>
#     </property>
#     <property name="minimumSize">
#      <size>
#       <width>100</width>
#       <height>120</height>
#      </size>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>64</pointsize>
#      </font>
#     </property>
#     <layout class="QGridLayout" name="gridLayout">
#      <property name="spacing">
#       <number>1</number>
#      </property>
#      <item row="1" column="0">
#       <widget class="QPushButton" name="pushButton_2">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="2" column="0">
#       <widget class="QPushButton" name="pushButton_3">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="0" column="0">
#       <widget class="QPushButton" name="pushButton">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="0" column="1">
#       <widget class="QPushButton" name="pushButton_4">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="2" column="1">
#       <widget class="QPushButton" name="pushButton_6">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="1" column="1">
#       <widget class="QPushButton" name="pushButton_5">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="0" column="2">
#       <widget class="QPushButton" name="pushButton_7">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="1" column="2">
#       <widget class="QPushButton" name="pushButton_8">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#      <item row="2" column="2">
#       <widget class="QPushButton" name="pushButton_9">
#        <property name="sizePolicy">
#         <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
#          <horstretch>100</horstretch>
#          <verstretch>100</verstretch>
#         </sizepolicy>
#        </property>
#        <property name="minimumSize">
#         <size>
#          <width>100</width>
#          <height>120</height>
#         </size>
#        </property>
#        <property name="font">
#         <font>
#          <pointsize>64</pointsize>
#         </font>
#        </property>
#        <property name="text">
#         <string/>
#        </property>
#       </widget>
#      </item>
#     </layout>
#    </widget>
#    <widget class="QPushButton" name="Start">
#     <property name="geometry">
#      <rect>
#       <x>140</x>
#       <y>490</y>
#       <width>341</width>
#       <height>71</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>24</pointsize>
#      </font>
#     </property>
#     <property name="text">
#      <string>START OVER</string>
#     </property>
#    </widget>
#    <widget class="QLabel" name="label">
#     <property name="geometry">
#      <rect>
#       <x>90</x>
#       <y>410</y>
#       <width>461</width>
#       <height>61</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>36</pointsize>
#      </font>
#     </property>
#     <property name="text">
#      <string>X Goes First</string>
#     </property>
#     <property name="alignment">
#      <set>Qt::AlignCenter</set>
#     </property>
#    </widget>
#   </widget>
#   <widget class="QMenuBar" name="menubar">
#    <property name="geometry">
#     <rect>
#      <x>0</x>
#      <y>0</y>
#      <width>640</width>
#      <height>37</height>
#     </rect>
#    </property>
#   </widget>
#   <widget class="QStatusBar" name="statusbar"/>
#  </widget>
#  <resources/>
#  <connections/>
# </ui>

from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextEdit,QFileDialog
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_31_TicTackToe/ticTackToe.ui',self)
        self.but1=self.findChild(QPushButton,'pushButton')
        self.but2=self.findChild(QPushButton,'pushButton_2')
        self.but3=self.findChild(QPushButton,'pushButton_3')
        self.but4=self.findChild(QPushButton,'pushButton_4')
        self.but5=self.findChild(QPushButton,'pushButton_5')
        self.but6=self.findChild(QPushButton,'pushButton_6')
        self.but7=self.findChild(QPushButton,'pushButton_7')
        self.but8=self.findChild(QPushButton,'pushButton_8')
        self.but9=self.findChild(QPushButton,'pushButton_9')
        self.label=self.findChild(QLabel,'label')
        self.start=self.findChild(QPushButton,'Start')
        # click button
        self.counter =0
        self.game_over=False
        button_list = [getattr(self, f'but{i}') for i in range(1, 10)]
        for but in button_list:
            # but.clicked.connect(lambda checked, b=but: self.clicker(b))
            but.clicked.connect(lambda checked, b=but: self.clicker(b,checked))
        ## note how the lambda construction is similar and different,    
        # self.but8.clicked.connect(lambda checked : self.clicker(self.but8,checked))  ## i included just as a reminder of other options  
        self.start.clicked.connect(lambda:self.reset())   
            
    def checkwin(self):
        winning_combinations = [
            (self.but1, self.but4, self.but7),
            (self.but1, self.but2, self.but3),
            (self.but4, self.but5, self.but6),
            (self.but7, self.but8, self.but9),
            (self.but2, self.but5, self.but8),
            (self.but3, self.but6, self.but9),
            (self.but1, self.but5, self.but9),
            (self.but7, self.but5, self.but3),
        ]
        
        
        
        
        for a, b, c in winning_combinations:
            if a.text() != "" and a.text() == b.text() == c.text():
                print(f'Checking {a.objectName()}  = {a.text()} ,{b.objectName()}  = {b.text()} ,{c.objectName()}  = {c.text()} ')
                print('Win detected')
                self.win(a, b, c)
                
                return  # stop after first win found


        # Check for draw
        all_buttons = [self.but1, self.but2, self.but3,
                    self.but4, self.but5, self.but6,
                    self.but7, self.but8, self.but9]

        if all(b.text() != "" for b in all_buttons):## cool  if all the text in the b in all_buttons is not empty ' ', the self(draw)
            print('Draw detected')
            # self.draw(a,b,c)
            self.draw()

    def draw(self):
    # def draw(self,a,b,c):
        self.label.setText('Draw')
        # a.setStyleSheet('QPushButton{background-color: red;color:gray;}')
        # b.setStyleSheet('QPushButton{background-color: red;color:gray;}')
        # c.setStyleSheet('QPushButton{background-color: red;color:gray;}')
        
        self.game_over=True ## wgeb there is a match of three in a line, the flag is set to true,  which means the clicker function will not accept another selection
        ## an alternative to having the game_over flag is to have a disable function that changes the buttons to enable(False) so that buttons cannot be used until the reset
        self.disable()  ## this works as well as using the flags. 


    def clicker(self, b,checked):
        # print(b,checked)
        if self.game_over == True: ## at the beginning of game, it is False, so the game continues
            return                  ## this is my alternaive to the disable function which setEnabled(False) all buttons after the win
        if self.counter % 2 == 0:
            mark = 'X'
            self.label.setText("O's turn")
            b.setStyleSheet("background-color: lightblue; color: navy; font-size: 38px;")
        else:
            mark = 'O'
            self.label.setText("X's turn")
            b.setStyleSheet("background-color: yellow; color: red; font-size: 38px;")

        b.setText(mark)
        b.setEnabled(False)
        self.counter += 1

        self.checkwin()
    def win(self, a, b, c):
        self.label.setText(f'{a.text()} WINS!')
        a.setStyleSheet('QPushButton{background-color: red;color:gray;}')
        b.setStyleSheet('QPushButton{background-color: red;color:gray;}')
        c.setStyleSheet('QPushButton{background-color: red;color:gray;}')
        
        self.game_over=True ## wgeb there is a match of three in a line, the flag is set to true,  which means the clicker function will not accept another selection
        ## an alternative to having the game_over flag is to have a disable function that changes the buttons to enable(False) so that buttons cannot be used until the reset
        self.disable()  ## this works as well as using the flags. 
   
    def disable(self):  # alternative to the flag 'game_over'
        button_list =[]
        button_list = [getattr(self, f'but{i}') for i in range(1, 10)]
        
        # for b in button_list:
        #     print(b)
        for b in button_list:
   
            b.setEnabled(False)
   
   
      
    def reset(self):
        self.game_over= False   ## when the reset button is selected, the game_over flag is reset to False and the the buttons cleared and set to beige, ready for a new game
        
        self.counter=0
        self.label.setText('')
        self.label.setText('start')
        button_list =[]
        button_list = [getattr(self, f'but{i}') for i in range(1, 10)]
        
        # for b in button_list:
        #     print(b)
        for b in button_list:
            b.setStyleSheet('background-color:beige;') ##  b.setStylesheet('QPushButton{color: #797979;}')
            b.setText('')
            b.setEnabled(True)
        self.label.setText('Start Again')



if __name__ =='__main__':
    app=QApplication(sys.argv)
    w= MainWindow()
    w.show()
    sys.exit(app.exec_())



''' The all() function in Python is a built-in function that takes a single argument, which must be an iterable (like a list, tuple, dictionary, or set). It returns True if all elements within the iterable evaluate to True, or if the iterable is empty. Otherwise, it returns False. 
Key characteristics of all():
Truthiness:
all() evaluates the "truthiness" of each element in the iterable. In Python, various values are considered "falsy" (evaluate to False in a boolean context), including:
False
None
Zero (0, 0.0, 0j)
Empty sequences (e.g., [], (), {}, "")
Short-circuiting:
all() short-circuits its evaluation. This means it stops processing and immediately returns False as soon as it encounters the first "falsy" element in the iterable.
Empty iterable:
If the iterable passed to all() is empty, the function returns True. This is because there are no "falsy" elements within an empty iterable to make the condition false. '''