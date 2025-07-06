'''
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Chat_Uic
/Users/judsonbelmont/Documents/Shared_Folders/PyQt5/Codemy/Cod_27_Chat_Uic/main.py
'''



import sys
from PyQt5 import QtWidgets, uic

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Codemy/Cod_27_Chat_Uic/second_window.ui", self)

class ThirdWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi("third_window.ui", self)
        uic.loadUi("Codemy/Cod_27_Chat_Uic/third_window.ui", self)

## both ways of calling MainWindow work, fdor consistency I will use the first- 3 MainWindows and 3 self
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ):
        super(MainWindow,self).__init__()

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
        # uic.loadUi("main_window.ui", self)
        uic.loadUi("Codemy/Cod_27_Chat_Uic/main_window.ui", self)

        self.pushButton_second.clicked.connect(self.open_second_window)
        self.pushButton_third.clicked.connect(self.open_new_third_window)
        self.pushButton_list.clicked.connect(self.list_third_windows)

        self.second_window = None
        self.third_windows = []

    def open_second_window(self):
        if self.second_window is None:
            self.second_window = SecondWindow()
        self.second_window.show()

    def open_new_third_window(self):
        index = len(self.third_windows)
        new_win = ThirdWindow()
        new_win.setWindowTitle(f"Third Window #{index + 1}")
        new_win.myButton.clicked.connect(lambda: self.on_third_button_clicked(index))
        self.third_windows.append(new_win)
        new_win.show()

    def list_third_windows(self):
        print("Currently open third windows:")
        for i, win in enumerate(self.third_windows):
            if win.isVisible():
                print(f"  [{i}] Visible - {win.windowTitle()}")
            else:
                print(f"  [{i}] Closed - {win.windowTitle()}")

    def on_third_button_clicked(self, index):
        print(f"Button in Third Window #{index + 1} clicked")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
