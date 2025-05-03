'''
https://www.book2s.com/tutorials/pyqt-qtreewidget.html
'''
import sys
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

app = QApplication(sys.argv)

# Create a QTreeWidget instance
tree_widget = QTreeWidget()
tree_widget.setColumnCount(3)  # Optional: Set the number of columns
tree_widget.setHeaderLabels(["Name", "Value","list items"])  # Optional: Set header labels
# Populate the tree with items
root_item = QTreeWidgetItem(tree_widget, ["Root"])
child_item1 = QTreeWidgetItem(root_item, ["Child 1"])
child_item2 = QTreeWidgetItem(root_item, ["Child 2"])
root2_item = QTreeWidgetItem(tree_widget, ["Root 2"])
child_item3 = QTreeWidgetItem(root2_item, ["Child 3"])
child_item4 = QTreeWidgetItem(root2_item, ["Child 4"])
# Add sub-items to the first child  
child_item1_sub1 = QTreeWidgetItem(child_item1, ["Sub Child 1.1"])
child_item1_sub2 = QTreeWidgetItem(child_item1, ["Sub Child 1.2"])
# Add items to the tree
tree_widget.addTopLevelItem(root_item)
tree_widget.addTopLevelItem(root2_item)
# Optionally, expand the root item to show its children
root_item.setExpanded(True)
root2_item.setExpanded(True)
# Show the tree widget

tree_widget.show()
sys.exit(app.exec_())