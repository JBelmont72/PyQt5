
'''The main modules for Qt are QtWidgets, QtGui and QtCore
Next we create an instance of QApplication, passing in sys.argv, which is Python list containing the command line arguments passed to the application.
'In Qt all top level widgets are windows -- that is, they don't have a parent and are not nested within another widget or layout. This means you can technically create a window using any widget you like.

QMainWindow
As we discovered in the last part, in Qt any widgets can be windows. For example, if you replace QWidget with QPushButton. In the example below, you would get a window with a single push-able button in it.


'''
from PyQt5.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()


# Your application won't reach here until you exit and the event
# loop has stopped.

