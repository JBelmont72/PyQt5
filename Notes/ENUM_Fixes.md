| 📌 Qt Designer Syntax              | ✔️ PyQt5 Replacement                         | 📦 Required Module              |
|----------------------------------|---------------------------------------------|---------------------------------|
| `Qt::AlignLeft`                  | `QtCore.Qt.AlignLeft`                        | `from PyQt5 import QtCore`      |
| `Qt::AlignRight`                 | `QtCore.Qt.AlignRight`                       | `QtCore`                        |
| `Qt::AlignTop`                   | `QtCore.Qt.AlignTop`                         | `QtCore`                        |
| `Qt::AlignBottom`                | `QtCore.Qt.AlignBottom`                      | `QtCore`                        |
| `Qt::AlignCenter`                | `QtCore.Qt.AlignCenter`                      | `QtCore`                        |
| `Qt::Horizontal`                 | `QtCore.Qt.Horizontal`                       | `QtCore`                        |
| `Qt::Vertical`                   | `QtCore.Qt.Vertical`                         | `QtCore`                        |
| `Qt::NoRole`                     | `QtWidgets.QAction.NoRole`                   | ✅ `QtWidgets` ⚠️ (extra needed) |
| `QFrame::HLine`                  | `QtWidgets.QFrame.HLine`                     | ✅ `QtWidgets` ⚠️ (extra needed) |
| `QFrame::VLine`                  | `QtWidgets.QFrame.VLine`                     | `QtWidgets`                     |
| `QFrame::Sunken`                 | `QtWidgets.QFrame.Sunken`                    | `QtWidgets`                     |
| `QAbstractItemView::NoEditTriggers` | `QtWidgets.QAbstractItemView.NoEditTriggers` | ✅ `QtWidgets` ⚠️ (extra needed) |
| `QAbstractItemView::MultiSelection` | `QtWidgets.QAbstractItemView.MultiSelection` | `QtWidgets`                     |
| `QSizePolicy::Expanding`         | `QtWidgets.QSizePolicy.Expanding`            | ✅ `QtWidgets` ⚠️ (extra needed) |
| `QSizePolicy::Preferred`         | `QtWidgets.QSizePolicy.Preferred`            | `QtWidgets`                     |
| `QIcon::Normal`                  | `QtGui.QIcon.Normal`                         | ✅ `QtGui` ⚠️ (extra needed)     |
| `QIcon::Disabled`                | `QtGui.QIcon.Disabled`                       | `QtGui`                         |
| `QIcon::On`                      | `QtGui.QIcon.On`                             | `QtGui`                         |
| `QIcon::Off`                     | `QtGui.QIcon.Off`                            | `QtGui`                         |

`Qt::NoRole`                     | `QtWidgets.QAction.NoRole`                   | ✅ `QtWidgets` ⚠️ (extra needed) |
* self.label.setFrameShape(QtWidgets.QFrame.Box)
* self.label.setFrameShadow(QtWidgets.QFrame.Raised)
# self.label.setFrameShape(QtCore.Qt.QFrame::Shape::Box)
# self.label.setFrameShadow(QtCore.Qt.QFrame::Shadow::Raised)


self.actionHome.setMenuRole(QtCore.Qt    .QAction::MenuRole             ::NoRole)              error
self.actionHome.setMenuRole(             QtWidgets.QAction              .NoRole)               corrected

self.actionHome.setMenuRole(QtCore.Qt.QAction::MenuRole::NoRole)        wrong
self.actionHome.setMenuRole(QtWidgets.QAction.NoRole)                   corrected
In PyQt5, enums like QAction.MenuRole are accessed via their class (QAction) not via Qt.
This issue commonly arises when using pyuic5 on .ui files designed with Qt Designer, especially with menu roles, alignments, frame styles, etc.


Example of correction formats to look for:
 `Qt::AlignCenter`                | `QtCore.Qt.AlignCenter`                      | `QtCore`   

self.myLabel.setAlignment(QtCore.Qt.  Qt::AlignmentFlag::AlignCenter   ) is wrong
self.myLabel.setAlignment(    QtCore.Qt.AlignmentFlag.AlignCenter   ) is correct

 # This regex looks for the pattern 'QtCore.Qt::AlignmentFlag::AlignCenter' and replaces it with 'QtCore.Qt.AlignCenter'
    code = re.sub(r'QtCore\.Qt::AlignmentFlag::(AlignCenter|AlignLeft|AlignRight|AlignTop|AlignBottom)', r'QtCore.Qt.\1', code)
### this is an additonal list of replacements
def clean_qt_enum_syntax(file_path: str) -> str:
    """Read a file, clean up Qt enum issues, and return cleaned text."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Example cleanup: remove 'QtWidgets.' prefix from enums
    content = content.replace('QtWidgets.QFrame.', 'QFrame.')
    content = content.replace('QtWidgets.QAbstractItemView.', 'QAbstractItemView.')
    content = content.replace('QtWidgets.QSizePolicy.', 'QSizePolicy.')
    content = content.replace('QtWidgets.QStyle.', 'QStyle.')

    return content
## this chat has the second go at with cleaning .ui to pyuic5 conversions. https://chatgpt.com/c/681033ae-abd4-800f-9f4c-c7f42211c4ea



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
