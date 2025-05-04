'''
1st QVboxLayout,  simply stack vertically (or horizontally)
2d layout.addLayout(user_name_layout)
3d form  layouts
4th grid layout

Member Type Documentation

enum QLineEdit::ActionPosition

This enum type describes how a line edit should display the action widgets to be added.

Constant	Value	Description
QLineEdit::LeadingPosition	0	The widget is displayed to the left of the text when using layout direction Qt::LeftToRight or to the right when using Qt::RightToLeft, respectively.
QLineEdit::TrailingPosition	1	The widget is displayed to the right of the text when using layout direction Qt::LeftToRight or to the left when using Qt::RightToLeft, respectively.
qtw.QLineEdit.TrailingPosition


enum Qt::AlignmentFlag
flags Qt::Alignment

'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
#         user_label =qtw.QLabel('username')
#         password_label = qtw.QLabel('password')
        
        
        
#         user_input = qtw.QLineEdit()
#         password_input = qtw.QLineEdit()
#         password_input.setEchoMode(qtw.QLineEdit.Password) ## uses the ACCESS METHOD
#         ## below an alterniative if lots of properites to enter, but not always works, bundle properties with the QLineEdit() CONSTRUCTOR
#         # password_input=qtw.QLineEdit(echoMode=qtw.QLineEdit.Password)
#         password_input.ActionPosition(qtw.QLineEdit.TrailingPosition)
#         check_box = qtw.QCheckBox('legalese accept')
        
#         login_button= qtw.QPushButton('login')
#         cancel_button = qtw.QPushButton('cancel')
        
#         ## need an intermiary object called a layout
#         layout = qtw.QVBoxLayout()
#         layout.addWidget(user_label)
#         layout.addWidget(user_input)
#         layout.addWidget(password_label)
#         layout.addWidget(password_input)
#         layout.addWidget(check_box)
#         layout.addWidget(login_button)
#         layout.addWidget(cancel_button)
        
#         ## need to tell this class that this layout is for this class
#         self.setLayout(layout)
        
#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes


#######~~~~~~~ same as above but adding better layouts
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
#         user_label =qtw.QLabel('username')
#         password_label = qtw.QLabel('password')
   
#         user_input = qtw.QLineEdit()
#         password_input = qtw.QLineEdit()
#         password_input.setEchoMode(qtw.QLineEdit.Password) ## uses the ACCESS METHOD
#         ## below an alterniative if lots of properites to enter, but not always works, bundle properties with the QLineEdit() CONSTRUCTOR
#         # password_input=qtw.QLineEdit(echoMode=qtw.QLineEdit.Password)
        
#         check_box = qtw.QCheckBox('legalese accept')
#         check_box.setGeometry(qtc.QRect(130, 190, 85, 20))# my addition. no wffect?
#         login_button= qtw.QPushButton('login')
#         cancel_button = qtw.QPushButton('cancel')
        
#         ## need an intermiary object called a layout
#         layout = qtw.QVBoxLayout()
#         user_name_layout = qtw.QHBoxLayout()
#         user_name_layout.addWidget(user_label)
#         user_name_layout.addWidget(user_input)
#         layout.addLayout(user_name_layout)## position this here to be displayed on top
#         password_layout=qtw.QHBoxLayout()
        
#         password_layout.addWidget(password_label)
#         password_layout.addWidget(password_input)
#         layout.addLayout(password_layout)
        
#         layout.addWidget(check_box)
#         button_layout = qtw.QHBoxLayout()
#         button_layout.addWidget(login_button)
#         button_layout.addWidget(cancel_button)
#         layout.addLayout(button_layout)
        
        
#         layout.addLayout(user_name_layout)## can add layouts to layouts,  cannot widget to layouots.  layouts can be added to either a widget or layouot
#         ## need to tell this class that this layout is for this class
#         self.setLayout(layout)
        
        
#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
#### same as above but tring different layouts GRID LAYOUT
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
#         user_label =qtw.QLabel('username')
#         password_label = qtw.QLabel('password')
   
#         user_input = qtw.QLineEdit()
#         password_input = qtw.QLineEdit()
#         password_input.setEchoMode(qtw.QLineEdit.Password) ## uses the ACCESS METHOD
#         ## below an alterniative if lots of properites to enter, but not always works, bundle properties with the QLineEdit() CONSTRUCTOR
#         # password_input=qtw.QLineEdit(echoMode=qtw.QLineEdit.Password)
        
#         check_box = qtw.QCheckBox('legalese accept')
#         check_box.setGeometry(qtc.QRect(130, 190, 85, 20))# my addition. no wffect?
#         login_button= qtw.QPushButton('login')
#         cancel_button = qtw.QPushButton('cancel')
        
#         ## need an intermiary object called a layout
#         layout = qtw.QGridLayout() ## now need to give positional arguemtns of rows and columns
        
#         ## need an intermiary object called a layout
#         # layout = qtw.QVBoxLayout() used this before but not here since we are using a grid
#         layout.addWidget(user_label,0,0)
#         layout.addWidget(user_input,0,1)
#         layout.addWidget(password_label)
#         layout.addWidget(password_input)
#         layout.addWidget(check_box)
#         layout.addWidget(login_button)
#         layout.addWidget(cancel_button)
        
#         ## can add layouts to layouts,  cannot widget to layouots.  layouts can be added to either a widget or layouot
#         ## need to tell this class that this layout is for this class
#         self.setLayout(layout)
        
        
#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
### same but with FORM layout
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
        
#         # user_label =qtw.QLabel('username')## when we use the Form layout, we can add the labels directly and do NOT need QLabel!!
#         # password_label = qtw.QLabel('password')
   
#         user_input = qtw.QLineEdit()
#         password_input = qtw.QLineEdit()
#         password_input.setEchoMode(qtw.QLineEdit.Password) ## uses the ACCESS METHOD
#         ## below an alternative if lots of properites to enter, but not always works, bundle properties with the QLineEdit() CONSTRUCTOR
#         # password_input=qtw.QLineEdit(echoMode=qtw.QLineEdit.Password)
        
#         check_box = qtw.QCheckBox('legalese accept')
#         check_box.setGeometry(qtc.QRect(130, 190, 85, 20))# my addition. no wffect?
#         login_button= qtw.QPushButton('login')
#         cancel_button = qtw.QPushButton('cancel')
        
#         ## need an intermiary object called a layout
#         layout = qtw.QFormLayout() ## now need to give positional arguemtns of rows and columns
        
#         ## need an intermiary object called a layout
#         # layout = qtw.QVBoxLayout() used this before but not here since we are using a grid
#         layout.addRow('     user_name',user_input)
#         layout.addRow('password',password_input)
#         layout.addRow(check_box)
#         layout.addRow(login_button,cancel_button)
        
        
#         ## can add layouts to layouts,  cannot widget to layouots.  layouts can be added to either a widget or layouot
#         ## need to tell this class that this layout is for this class
#         self.setLayout(layout)
        
        
#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

### same but with FORM layout but added  another button layout refinement
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here
        
        # user_label =qtw.QLabel('username')## when we use the Form layout, we can add the labels directly and do NOT need QLabel!!
        # password_label = qtw.QLabel('password')
   
        user_input = qtw.QLineEdit()
        password_input = qtw.QLineEdit()
        password_input.setEchoMode(qtw.QLineEdit.Password) ## uses the ACCESS METHOD
        ## below an alternative if lots of properites to enter, but not always works, bundle properties with the QLineEdit() CONSTRUCTOR
        # password_input=qtw.QLineEdit(echoMode=qtw.QLineEdit.Password)
        
        check_box = qtw.QCheckBox('legalese accept')
        check_box.setGeometry(qtc.QRect(130, 190, 85, 20))# my addition. no wffect?
        login_button= qtw.QPushButton('login')
        cancel_button = qtw.QPushButton('cancel')
        
        ## need an intermiary object called a layout
        layout = qtw.QFormLayout() ## now need to give positional arguemtns of rows and columns
        
        ## need an intermiary object called a layout
        # layout = qtw.QVBoxLayout() used this before but not here since we are using a grid
        layout.addRow('user_name',user_input,)
        layout.addRow('password',password_input,)
        
        check_box_widget=qtw.QWidget()
        check_box_widget.setLayout(qtw.QHBoxLayout())
        check_box_widget.layout().addWidget(check_box)
        layout.addRow('',check_box_widget)
        
        ## will create for this last eaxample a button_widget =qtw.QWidget()
        button_widget =qtw.QWidget() ## will place buttons inside
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(cancel_button)
        button_widget.layout().addWidget(login_button)
        layout.addRow('', button_widget)
        self.setLayout(layout) ## this is where we connect the 'layout=qtw.QFormLayout (or H or V or Grid) to the class
        
        
        ## can add layouts to layouts,  cannot widget to layouots.  layouts can be added to either a widget or layouot
        ## need to tell this class that this layout is for this class
        self.setLayout(layout)
        
        
        # Your code ends here
        self.show() ## put it here so the window shows.


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes