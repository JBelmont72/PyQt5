

https://github.com/alandmoore/PyQt-Videos-Examples/blob/master/TemplatesAndQtDesigner/loginbox.ui

https://www.youtube.com/watch?v=5QpguaNFecQ
Follow at:  https://www.alandmoore.com
Important references for finding signals and slots of classes:
the parent class of all buttons is the QAbstractButton  https://doc.qt.io/qt-6/qabstractbutton.html
will see the signals which connect to the slots 

the parent clas for all widgets is QWidgets :  https://doc.qt.io/qt-6/qwidget.html



  all the widgets have the 'Public slots' shown at this link https://doc.qt.io/qt-5/qwidget.html
QlineEdit   https://doc.qt.io/qt-6/qlineedit.html
qt documentation:    https://doc.qt.io/qt-5/qapplication.html#QApplication

qt doc qLineEdit  https://doc.qt.io/qt-6/qlineedit.html     looked at 'Properties' then selected 'echo mode'
options  are normal and password , noEcho, etc.  WIll use an 'Access Function' to set the mode or desired arguement / action 
it uses an enum
'The widget's display and the ability to copy or drag the text is affected by this setting.

By default, this property is set to Normal.

Access functions:

QLineEdit::EchoMode	echoMode() const
void	setEchoMode(QLineEdit::EchoMode)
See also EchoMode and displayText().'
 If we click on 'echoMode' we go to the 'enum QlineEdit::EchoMode'
 next window shows:
 'enum QLineEdit::EchoMode

This enum type describes how a line edit should display its contents.

Constant	Value	Description
QLineEdit::Normal	0	Display characters as they are entered. This is the default.

QLineEdit::NoEcho	1	Do not display anything. This may be appropriate for passwords where even the length of the password should be kept secret.

QLineEdit::Password	2	Display platform-dependent password mask characters instead of the characters actually entered.

QLineEdit::PasswordEchoOnEdit	3	Display characters as they are entered while editing otherwise display characters as with Password.

See also setEchoMode() and echoMode().'

of these options we want to select '        password_input = qtw.QLineEdit()
        password_input.setEchoMode(qtw.QLineEdit.Password)	2	Display platform-dependent password mask characters instead of the characters actually entered.'
So next we want to use this for Les_3_handBuild.py
        password_input = qtw.QLineEdit()
        password_input.setEchoMode(qtw.QLineEdit.Password)  ## note the change when we moved this to python!!

QLineEdit::Password	 becomes  qtw.QLineEdit.Password)     
##########
Recommended Resources:
Here's a clear and official PyQt5 reference:
Signals and Slots in PyQt5 (official docs)
Or for a tutorial format:
Real Python: Mastering PyQt5 Signals and Slots
Would you like a minimal working example showing the signal in action?


#####

https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html
https://realpython.com/lessons/applications-events-signals-pyqt/

https://realpython.com/lessons/applications-events-signals-pyqt/
https://realpython.com/lessons/implementing-model-pyqt/
https://realpython.com/videos/pyqt-layouts-overview/



he mentions pyside as an alternative to PyQt5 which is python 