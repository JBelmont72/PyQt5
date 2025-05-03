'''
It saves the list to data.json.
It automatically loads from data.json on startup, if the file exists.
If data.json is missing or corrupted, it just starts with an empty list.
There are no crash risks if the file doesn't exist yet — it handles it cleanly.

'''
import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QListWidget, QLineEdit,  QListWidget, QLineEdit, QLabel
)

DATA_FILE = "data.json"

class ItemSaverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Item Saver")
        self.resize(300, 400)
        self.items = []

        # Layout
        layout = QVBoxLayout()

        # Widgets
        self.label = QLabel("Enter an item:")
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Item")
        self.list_widget = QListWidget()
        self.save_button = QPushButton("Save Items")

        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Connect buttons
        self.add_button.clicked.connect(self.add_item)
        self.save_button.clicked.connect(self.save_items)

        # Load any saved items
        self.load_items()

    def add_item(self):
        text = self.input_field.text().strip()
        if text:
            self.items.append(text)
            self.list_widget.addItem(text)
            self.input_field.clear()

    def save_items(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.items, f)
        print("Items saved!")

    def load_items(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                try:
                    self.items = json.load(f)
                    self.list_widget.addItems(self.items)
                    print("Items loaded!")
                except json.JSONDecodeError:
                    print("Error: Could not load items (invalid JSON).")
        else:
            print("No saved items found.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ItemSaverApp()
    window.show()
    sys.exit(app.exec_())
