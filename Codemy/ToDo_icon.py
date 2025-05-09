'''
ToDo_dBase.py - A simple To-Do List application adding database functionality using PyQt5.
we'll start to add a SQLite3 database to our Todo List GUI App with PyQT5 and Python
#         #         self.myList.addItem(item_text)
#         #         self.myItems.clear()
#         #         self.myItems.setFocus()
#         #         self.myTree.addTopLevelItem(QtWidgets.QTreeWidgetItem([item_text]))
#         #         self.myTree.setFocus()
#         #         self.myList.setCurrentRow(self.myList.count() - 1)
#         #         self.myItems.clear()

ToDo.py - A simple To-Do List application using PyQt5.
# This file was generated by PyQt5 UI code generator.
# It provides a user interface for adding, deleting, and clearing items in a to-do list.

In ToDo_icon.py:
 building a PyQt5-based To-Do list app and want to:
Preserve the list using sqlite3 — done ✔️
Call it using a custom desktop icon (7.png) — partly done
Restore saved list items from the DB on launch — working via grab_all() ✔️
Save new items to the DB — currently missing
Delete items from both UI and DB — currently missing
Package it into a Mac app with the icon — not yet covered
I modified the code to include database functionality, allowing items to be added, deleted, and cleared from both the UI and the database.
#1 Package as a Mac app with icon 7.png:
Use py2app or pyinstaller. Here’s how to do it with pyinstaller (recommended):
Step-by-step:
Install PyInstaller (if not yet):
pip install pyinstaller
Place 7.png in the same folder.
Create a ToDo.spec or run:
pyinstaller --windowed --onefile --icon=7.png ToDo.py
⚠️ --windowed avoids the terminal window. Use --noconfirm for repeated runs.
Your .app file will appear under dist/ToDo.app.

'''
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
# This imports the necessary modules from PyQt5 for creating a GUI application.
# It also imports the sqlite3 module for database functionality.
# The sqlite3 module is used to interact with SQLite databases.
conn = sqlite3.connect('todo_list.db')  # Connect to the SQLite database
# This line connects to a SQLite database named 'todo_list.db'.
# create a cursor object to execute SQL commands
c = conn.cursor()
## Create a table to store the to-do list items if it doesn't exist
c.execute('''
CREATE TABLE if not exists todo_list (
    list_item text  
)
''')
# c.execute('''
#     CREATE TABLE IF NOT EXISTS todo_items (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         item TEXT NOT NULL
#     )
# ''')
# This SQL command creates a table named 'todo_items' with two columns: 'id' and 'item'.
# The 'id' column is an integer that auto-increments, and the 'item' column is a text field that cannot be null.
# The 'IF NOT EXISTS' clause ensures that the table is only created if it does not already exist.
# Commit the changes to the database
conn.commit()
# This line commits the changes made to the database, ensuring that the table creation is saved.
# Close the database connection
conn.close()  # Close the database connection when done
# This line closes the database connection. It is good practice to close the connection when you are done with it.
# This is the main class for the To-Do List application.
class Ui_myListWindow(object):
    def setupUi(self, myListWindow):
        myListWindow.setObjectName("myListWindow")
        myListWindow.resize(599, 601)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        myListWindow.setFont(font)
        myListWindow.setAcceptDrops(True)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::AddressBookNew")
        myListWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(myListWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add_Item = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.add_it())
        self.Add_Item.setGeometry(QtCore.QRect(10, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Add_Item.setFont(font)
        self.Add_Item.setObjectName("Add_Item")
        self.Delete_Item = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.delete_it())
        # The lambda function is used to call the delete_it method when the button is clicked.
        self.Delete_Item.setGeometry(QtCore.QRect(140, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Delete_Item.setFont(font)
        self.Delete_Item.setObjectName("Delete_Item")
        self.Clear_Item = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.Clear_Item.setGeometry(QtCore.QRect(280, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Clear_Item.setFont(font)
        self.Clear_Item.setObjectName("Clear_Item")
        self.myItems = QtWidgets.QLineEdit(self.centralwidget)
        self.myItems.setGeometry(QtCore.QRect(20, 20, 501, 61))
        self.myItems.setObjectName("myItems")
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(65, 171, 411, 201))
        self.myList.setObjectName("myList")
        self.myTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.myTree.setGeometry(QtCore.QRect(110, 370, 311, 171))
        self.myTree.setObjectName("myTree")
        self.myTree.headerItem().setText(0, "1")
        self.Save_Button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.save_it())
        self.Save_Button.setGeometry(QtCore.QRect(420, 111, 100, 41))
        self.Save_Button.setObjectName("Save_Button")
        myListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(myListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 24))
        self.menubar.setObjectName("menubar")
        myListWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(myListWindow)
        self.statusbar.setObjectName("statusbar")
        myListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(myListWindow)
        QtCore.QMetaObject.connectSlotsByName(myListWindow)
        ## Grab all the items from the database and add them to the list widget
        # This function retrieves all items from the database and adds them to the list widget.
        # The function is called grab_all() and it is defined inside the setupUi method.
        ## This function is called when the application starts to populate the list widget with items from the database.
        self.grab_all()  # Call the function to populate the list widget with items from the database
    
    ## I modified from ToDo_dBase.py by changing add_it,delete_it,clear_it
    
    def add_it(self):
        item_text = self.myItems.text()
        if item_text:
            self.myList.addItem(QtWidgets.QListWidgetItem(item_text))
            self.myItems.clear()
            # Save to database
            conn = sqlite3.connect('todo_list.db')
            c = conn.cursor()
            c.execute("INSERT INTO todo_list (list_item) VALUES (?)", (item_text,))
            conn.commit()
            conn.close()

    def delete_it(self):
        selected_items = self.myList.selectedItems()
        if selected_items:
            for item in selected_items:
                item_text = item.text()
                # Remove from UI
                self.myList.takeItem(self.myList.row(item))
                # Remove from DB
                conn = sqlite3.connect('todo_list.db')
                c = conn.cursor()
                c.execute("DELETE FROM todo_list WHERE list_item = ?", (item_text,))
                conn.commit()
                conn.close()

    def delete_it(self):
        selected_items = self.myList.selectedItems()
        if selected_items:
            for item in selected_items:
                item_text = item.text()
                # Remove from UI
                self.myList.takeItem(self.myList.row(item))
                # Remove from DB
                conn = sqlite3.connect('todo_list.db')
                c = conn.cursor()
                c.execute("DELETE FROM todo_list WHERE list_item = ?", (item_text,))
                conn.commit()
                conn.close()

    def clear_it(self):
        self.myList.clear()
        conn = sqlite3.connect('todo_list.db')
        c = conn.cursor()
        c.execute("DELETE FROM todo_list")
        conn.commit()
        conn.close()

    ### below are the functions for the To-Do_dbase.py 
    
    def grab_all(self): 
        conn = sqlite3.connect('todo_list.db')
        c = conn.cursor()
        
        # c.execute('SELECT item FROM todo_items')
        c.execute('SELECT * FROM todo_list')  # This retrieves all items from the todo_list table in the database.
        # This line executes a SQL query to select all items from the todo_items table. 
        records = c.fetchall()
        # conn.close()
        # for item in records:
        #     self.myList.addItem(item[0])
            
        conn.commit()  # Commit the changes to the database
        conn.close()  # Close the cursor
        for record in records:
            self.myList.addItem(str(record[0]))  # Add each item to the list widget
            # self.myList.addItem(record[0])            
    # def add_it(self):
    #     item_text = self.myItems.text()
    #     if item_text:
    #         self.myList.addItem(item_text)
    #         self.myItems.clear() 
    ## NOTE myList is the name of the list widget, myItems is the name of the line edit 
    
    
    
    ## from ToDo_dBase.py
    # def add_it(self):## this takes text in the line edit and adds it to the list widget!!!
    #     item_text = self.myItems.text() ## get text from line edit
    #     # Check if the input field is not empty before adding to the list
    #     # If the input field is empty, it will not add an item to the list.
    #     # This prevents adding empty items to the list.
    #     if item_text:## both of the next two lines do the same thing
    #         # self.myList.addItem(item_text)# Add the item to the list widget!!! myList is the list widget
    #         self.myList.addItem(QtWidgets.QListWidgetItem(item_text)) # This is another way to add item to the list widget
    #         self.myItems.clear()# Clear the input field after adding the item


### i have two delete_it functions, one is commented out and the other is not-both work.
    ## Delete Item from List
    # def delete_it(self):
    #     selected_items = self.myList.selectedItems()## myList is the list widget, selectedItems() returns a list of selected items
    
    #     # This line sets the current row of the list widget to the selected item.
    #     # Check if there are any selected items before trying to remove them
    #     # If there are no selected items, it will not try to remove anything.
    #     # This prevents errors when trying to remove items that are not selected.
        
    #     if selected_items:
    #         for item in selected_items:
    #             self.myList.takeItem(self.myList.row(item))## This removes the item from the list widget
                       
    #     # takeItem() removes the item from the list widget and returns it
    #     # row(item) returns the row number of the item in the list widget
    #     # This is used to remove the item from the list widget.
        
    #      ### FOR FUN ONLY: the next four (91,98,99,100) lines are used to get the current row of the selected item in the list widget
    #     # if self.myList.currentItem() is not None:## This checks if there is a current item selected in the list widget
    #         ## If there is a current item selected, it gets the current row of the selected item
    #         ## If there is no current item selected, it will not try to get the current row.
    #         ## This prevents errors when trying to get the current row of an item that is not selected.
    #         ## This sets the text of the input field to the text of the selected item
    #         ## This sets the text of the input field to the current row of the selected item
            
    #         # selected_items = self.myList.currentRow()## This gets the current row of the selected item in the list widget
    #         # self.myItems.setText(self.myList.currentItem().text())## This sets the text of the input field to the text of the selected item            
    #         # self.myItems.setText(str(selected_items))## This sets the text of the input field to the current row of the selected item
    
    # def delete_it(self):## this did not work for the 0 index item in the list widget
#     Problem:
# If you select the first item (row 0), currentRow() returns 0, which Python treats as False.
# Then the if selected_items: fails!
    #     selected_items = self.myList.currentRow()
    #     # This line sets the current row of the list widget to the selected item.
    #     # Check if there are any selected items before trying to remove them
    #     # If there are no selected items, it will not try to remove anything.
    #     if selected_items:
    #         self.myList.takeItem(selected_items)## This removes the item from the list widget
    #     # takeItem() removes the item from the list widget and returns it
    #     # row(item) returns the row number of the item in the list widget
    #     # This is used to remove the item from the list widget.
    
    
    ## this is the delete_it function that works for the 0 index item in the list widget
    ## used in ToDo_dBase.py
    # def delete_it(self):
    #     selected_items = self.myList.selectedItems()
    #     if selected_items:
    #         for item in selected_items:
    #             self.myList.takeItem(self.myList.row(item))
    
    # def delete_it(self):## this works for the 0 index item in the list widget!!Good
    #     selected_row = self.myList.currentRow()
    #     if selected_row != -1:  # -1 means no selection
    #         self.myList.takeItem(selected_row)

    
    
    ## Clear All Items from List from ToDo_dBase.py
    # def clear_it(self):
    #     self.myList.clear()## This clears the list widget, removing all items from it.
    #     # self.myItems.clear()## This clears the input field, removing any text from it.
    #     # self.myTree.clear()## This clears the tree widget, removing all items from it.
    #     self.myItems.clear()
    
# This function clears the list and the input field.
    ## Retranslate UI   

    # def save_it(self):
    #     # This function is intended to save the current state of the to-do list.
    #     # You can implement your saving logic here, such as writing to a file or database.
    #     # For now, it will just print a message to the console.
    #     print("Save button clicked. Implement saving logic here.")
    #     # This function saves the current items in the list widget to a file named 'todo_list.txt'.
    #     # It iterates through each item in the list widget, retrieves its text, and writes it to the file.
    
    #     items=[]
    #     for index in range(self.myList.count()):
    #         items.append(self.myList.item(index).text())
    #     with open('todo_list.txt', 'w') as f:
    #         for item in items:
    #             f.write(item + '\n')
    #     # This function saves the current items in the list widget to a file named 'todo_list.txt'.
    #     # It iterates through each item in the list widget, retrieves its text, and writes it to the file.
    #     # You can modify the file name or format as needed.
    #     # self.myItems.clear()## This clears the input field, removing any text from it.
    #     self.myItems.clear()  # Clear the input field after saving
    #     # This clears the input field after saving the items to the file.
    #     # This function saves the current items in the list widget to a file named 'todo_list.txt'.
    #     # It iterates through each item in the list widget, retrieves its text, and writes it to the file.
    # def save_it(self):        ## this works but the next one is the way the instructor did it
    #     items = [] ## create an empty list to store items
    #     for index in range(self.myList.count()):
    #         print("Index:", index)  # Debugging line to see the index
    #         # This iterates through each item in the list widget and retrieves its text.
    #         # The count() method returns the number of items in the list widget.
    #         # The item() method retrieves the item at the specified index.
    #         # The text() method retrieves the text of the item.
    #         items.append(self.myList.item(index).text())
    #         # items.append(self.myList.item(index)) ## this appends 'object' to the items list
    #         print(self.myList.item(index).text()) ## Debugging line to see the item text
    #     print("Items to save:", items)
    #     ## he chose a slight alternaitve to loop through items.append(self.myList.item(index))NOT the text() method
    #     ## and then append the 'Method' of each item to the items list.
    #     ## for item in items:
    #     #   print(item.text)     
    #     # This function is intended to save the current state of the to-do list.
        
    # def save_it(self):
    #     items = [] ## create an empty list to store items
    #     for index in range(self.myList.count()):
    #         print("Index:", index)  # Debugging line to see the index
    #         items.append(self.myList.item(index))    
    #     for item in items:
    #         print(item.text())
       
        
    def save_it(self):
        conn = sqlite3.connect('todo_list.db')
        c = conn.cursor()
        
        c.execute('DELETE FROM todo_list')  # Clear old items
        
        for index in range(self.myList.count()):
            item = self.myList.item(index)
            c.execute('INSERT INTO todo_list (list_item) VALUES (?)', (item.text(),))
        
        conn.commit()
        conn.close()

        
    def retranslateUi(self, myListWindow):
        _translate = QtCore.QCoreApplication.translate
        myListWindow.setWindowTitle(_translate("myListWindow", "TO DO LIST"))
        self.Add_Item.setText(_translate("myListWindow", "Add Item to List"))
        self.Delete_Item.setText(_translate("myListWindow", "Delete Item from List"))
        self.Clear_Item.setText(_translate("myListWindow", "Clear All Items"))
        self.Save_Button.setText(_translate("myListWindow", "Save"))



       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_myListWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())